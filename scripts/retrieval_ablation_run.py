#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["psycopg[binary]>=3.2", "PyYAML", "sentence-transformers==6.1.0"]
# ///
# golden_v1 only. Set DATABASE_URL for the target database, then run:
# PYTHONHASHSEED=0 nice -n 15 .venv/bin/python scripts/retrieval_ablation_run.py
"""Run the local retrieval ablation without changing the database or model cache."""

from __future__ import annotations

import hashlib
import json
import os
import sys
import uuid
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
for name in ("HF_HUB_OFFLINE", "TRANSFORMERS_OFFLINE", "HF_DATASETS_OFFLINE"):
    os.environ[name] = "1"
for name in (
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
):
    os.environ[name] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import torch  # noqa: E402
import yaml  # noqa: E402
from sentence_transformers import SentenceTransformer  # noqa: E402

from api.chunk.store import chunker_version  # noqa: E402
from api.config import embedding, retrieval  # noqa: E402
from api.db import connect  # noqa: E402
from api.index.embed import vector_literal  # noqa: E402
from api.query.bm25 import build, corpus_key  # noqa: E402
from api.query.retrieve import dense_exact_top_k  # noqa: E402
from eval.retrieval_ablation import WEIGHTS, rankings, summarize  # noqa: E402

DEPTHS = (20, 50, 100)
MODES = ("dense", "sparse", *WEIGHTS)
DATA_SHA = "7d17972fa7e54c6f9cba64e26c5d7c27d021b58ac3a6ec355d1342a5ba4ec74a"
MANIFEST_SHA = "1a73f3d62e8b969463b01c138570890c0fef18d632cb09ea07f18205ccd30fbc"
CORPUS_KEY = "5a33c360a77f5bdf6f47912f850dda20c5cf15d0cbc3ecc40c124a5486723a67"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if os.environ.get("PYTHONHASHSEED") != "0":
        raise RuntimeError("PYTHONHASHSEED=0 is required for reproducible BM25 summation")
    dataset = ROOT / "eval/datasets/golden_v1.jsonl"
    manifest = ROOT / "eval/datasets/golden_v1_manifest.json"
    if sha(dataset) != DATA_SHA or sha(manifest) != MANIFEST_SHA:
        raise RuntimeError("golden dataset or manifest changed")
    items = [json.loads(line) for line in dataset.read_text().splitlines() if line]
    items = [item for item in items if not item["expected_abstain"]]
    if len(items) != 332 or sum(item["reviewed_by_human"] for item in items) != 125:
        raise RuntimeError("unexpected answerable cohort")
    cfg, emb = retrieval(), embedding()
    if cfg["dense_search"] != "exact" or cfg["sparse"]["backend"] != "bm25":
        raise RuntimeError("unexpected retrieval configuration")
    inputs = [
        "api/config.yaml",
        "api/corpus_freeze.yaml",
        "api/config.py",
        "api/db.py",
        "api/chunk/store.py",
        "api/index/embed.py",
        "api/query/retrieve.py",
        "api/query/bm25.py",
        "eval/metrics/retrieval.py",
        "eval/retrieval_ablation.py",
        "scripts/retrieval_ablation_run.py",
        "scripts/verify_retrieval_ablation.py",
    ]
    fingerprints = {name: sha(ROOT / name) for name in inputs}
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    model = SentenceTransformer(
        emb["model"], revision=emb["revision"], device="cpu", local_files_only=True
    )
    questions = [item["question"] for item in items]
    if any(
        len(model.tokenizer(q, truncation=False)["input_ids"]) > emb["max_seq_length"]
        for q in questions
    ):
        raise RuntimeError("question exceeds embedding window")
    vectors = model.encode(
        questions,
        batch_size=8,
        normalize_embeddings=True,
        convert_to_numpy=True,
        show_progress_bar=False,
        device="cpu",
    )
    conn = connect()
    with conn, conn.transaction():
        conn.execute("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY")
        conn.execute("SET LOCAL max_parallel_workers_per_gather = 0")
        identity = conn.execute(
            "SELECT current_database(), current_setting('transaction_read_only'), "
            "system_identifier::text FROM pg_control_system()"
        ).fetchone()
        if identity[1] != "on":
            raise RuntimeError("database transaction is not read-only")
        counts = conn.execute("SELECT count(*), count(embedding) FROM chunks").fetchone()
        if counts != (22354, 22354):
            raise RuntimeError("corpus embeddings mismatch")
        filings = conn.execute("SELECT accession, parse_status FROM filings").fetchall()
        freeze = yaml.safe_load((ROOT / "api/corpus_freeze.yaml").read_text())
        if dict(filings) != {row["accession"]: row["status"] for row in freeze["filings"]}:
            raise RuntimeError("filing statuses mismatch")
        chunks = conn.execute("SELECT chunk_id, text FROM chunks ORDER BY chunk_id").fetchall()
        if corpus_key(chunker_version(), chunks) != CORPUS_KEY:
            raise RuntimeError("corpus text key mismatch")
        index = build(chunks, CORPUS_KEY, cfg["sparse"]["k1"], cfg["sparse"]["b"])
        ids = {cid for cid, _text in chunks}
        rows = []
        for n, (item, vector) in enumerate(zip(items, vectors, strict=True), 1):
            if any(cid not in ids for group in item["gold_evidence_sets"] for cid in group):
                raise RuntimeError("gold chunk missing from rebuild")
            q = vector_literal(vector)
            dense = {depth: dense_exact_top_k(conn, q, depth) for depth in DEPTHS}
            sparse = {
                depth: [cid for cid, _score in index.search(item["question"], depth)]
                for depth in DEPTHS
            }
            row = {
                key: item[key]
                for key in (
                    "item_id",
                    "question",
                    "source",
                    "question_type",
                    "reviewed_by_human",
                    "gold_evidence_sets",
                )
            }
            row["rankings"] = rankings(dense, sparse, cfg["rrf_k"])
            rows.append(row)
            if n % 20 == 0 or n == len(items):
                print(f"retrieved {n}/{len(items)}", flush=True)
    if (
        sha(dataset) != DATA_SHA
        or sha(manifest) != MANIFEST_SHA
        or any(sha(ROOT / name) != digest for name, digest in fingerprints.items())
    ):
        raise RuntimeError("input changed during run")
    packet = {
        "kind": "local unfiltered Config 3 retrieval ablation; not a gated baseline",
        "completed_at_utc": datetime.now(UTC).isoformat(),
        "dataset_sha256": DATA_SHA,
        "manifest_sha256": MANIFEST_SHA,
        "input_sha256": fingerprints,
        "embedding": emb,
        "retrieval_config": cfg,
        "system_identifier": identity[2],
        "database_name": identity[0],
        "corpus_key": CORPUS_KEY,
        "runtime": {
            "python": sys.version,
            "torch": torch.__version__,
            "device": "cpu",
            "threads": 1,
            "pythonhashseed": "0",
            "bm25": "built in memory from verified corpus rows",
        },
        "protocol": "CPU only; no router or metadata filters; exact dense and BM25 freshly "
        "retrieved at each depth; RRF weights are dense:sparse, k=60; tie by "
        "best branch rank then chunk ID. No reranking or generation.",
        "limitations": [
            "Original snapshot equivalence is unverified.",
            "Only 125 answerables are reviewed; none are handwritten.",
        ],
        "results_at_depth": summarize(rows, MODES, DEPTHS),
        "results_at_10": summarize(rows, MODES, DEPTHS, 10),
        "items": rows,
    }
    output = ROOT / "eval/runs" / f"retrieval-ablation-{uuid.uuid4().hex[:12]}.json"
    with output.open("x", encoding="utf-8") as fh:
        json.dump(packet, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write("\n")
    print(f"output={output.relative_to(ROOT)} sha256={sha(output)}", flush=True)


if __name__ == "__main__":
    main()
