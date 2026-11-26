#!/usr/bin/env python3
"""Replay golden_v1 routed candidates offline; set DATABASE_URL before running."""

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
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"

from api.chunk.store import chunker_version  # noqa: E402
from api.config import rerank  # noqa: E402
from api.db import connect  # noqa: E402
from api.query.bm25 import corpus_key  # noqa: E402
from eval.paired_rerank import final_context, item_metrics, latency_summary, summarize  # noqa: E402
from scripts.rerank_run import load_reranker, machine, rerank_one, resolve_device  # noqa: E402

DATA = ROOT / "eval/datasets/golden_v1.jsonl"
META = ROOT / "eval/runs/35b3efbbfd5d.meta.json"
SOURCE = ROOT / "eval/runs/35b3efbbfd5d.results.jsonl"
PINS = {
    DATA: "7d17972fa7e54c6f9cba64e26c5d7c27d021b58ac3a6ec355d1342a5ba4ec74a",
    META: "f8b8a961081453e46df98ab8410ce47e9a3e81ef113dcdb4c10e6d5b1334dbaf",
    SOURCE: "1e2549569c9b887e58944add097e568d5380ed3863e135f904a85fe7f1263262",
}
MODELS = {
    "minilm": ("cross-encoder/ms-marco-MiniLM-L-6-v2", "233902d25c440f23af6f7d6e94d2946bac0bee0a"),
    "bge": ("BAAI/bge-reranker-base", "2cfc18c9415c912f9d8155881c133215df768a70"),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def environment() -> dict:
    return {"at": datetime.now(UTC).isoformat(), "load_average": os.getloadavg(),
            "machine": machine()}


def main() -> None:
    if any(sha(path) != digest for path, digest in PINS.items()):
        raise RuntimeError("source, dataset or metadata digest mismatch")
    meta = json.loads(META.read_text())
    if meta["pipeline"] != "config_4_routed" or list(meta["datasets"].values()) != [PINS[DATA]]:
        raise RuntimeError("source metadata does not match routed golden_v1")
    dataset = load_rows(DATA)
    traces = load_rows(SOURCE)
    if len(traces) != 392 or [r["item_id"] for r in traces] != meta["item_order"]:
        raise RuntimeError("source trace is incomplete or out of order")
    gold = {item["item_id"]: item for item in dataset}
    if len(gold) != 392 or set(gold) != {r["item_id"] for r in traces}:
        raise RuntimeError("source and dataset item IDs differ")
    inputs = ["api/query/rerank.py", "api/query/bm25.py", "api/chunk/store.py", "api/pipeline.py",
              "eval/pipeline.py", "eval/metrics/retrieval.py", "eval/paired_rerank.py",
              "scripts/rerank_run.py", "scripts/paired_rerank_run.py", "api/config.yaml"]
    fingerprints = {path: sha(ROOT / path) for path in inputs}
    rows = []
    for trace in traces:
        item = gold[trace["item_id"]]
        if item["expected_abstain"]:
            continue
        budget = trace["budget"]
        queries = [{"query": q["query"], "retrieved": q["retrieved"], "measured": {}}
                   for q in trace["queries"]]
        if budget is None and (trace["intent"] != "unsupported" or queries):
            raise RuntimeError("invalid unsupported trace")
        if budget is not None and len(queries) != budget["sub_queries"]:
            raise RuntimeError("missing subquery trace")
        row = {k: item[k] for k in ("item_id", "source", "question_type", "reviewed_by_human",
                                    "gold_evidence_sets")}
        row.update({"intent": trace["intent"], "budget": budget, "queries": queries})
        rows.append(row)
    if len(rows) != 332:
        raise RuntimeError("answerable cohort mismatch")
    start = environment()
    with connect() as conn, conn.transaction():
        conn.execute("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY")
        system_id = conn.execute(
            "SELECT system_identifier::text FROM pg_control_system()"
        ).fetchone()[0]
        counts = conn.execute("SELECT count(*), count(embedding) FROM chunks").fetchone()
        chunks = conn.execute("SELECT chunk_id, text FROM chunks ORDER BY chunk_id").fetchall()
        if (counts != (22354, 22354)
                or corpus_key(chunker_version(), chunks) != meta["bm25_index_key"]):
            raise RuntimeError("live corpus does not match source retrieval corpus")
        texts = dict(chunks)
        if any(cid not in texts for row in rows for q in row["queries"] for cid in q["retrieved"]):
            raise RuntimeError("source candidate missing from live corpus")
        device = resolve_device("auto")
        for name, (model_name, revision) in MODELS.items():
            cfg = {**rerank(), "model": model_name, "revision": revision, "device": device}
            model = load_reranker(cfg)
            for number, row in enumerate(rows, 1):
                for q in row["queries"]:
                    candidates = q["retrieved"]
                    if candidates:
                        ranked, seconds = rerank_one(
                            model, q["query"], [(c, texts[c]) for c in candidates]
                        )
                        q["measured"][name] = {"ranked": ranked, "seconds": seconds}
                    else:
                        q["measured"][name] = {"ranked": [], "seconds": None}
                if number % 20 == 0 or number == len(rows):
                    print(f"{name} {number}/{len(rows)}", flush=True)
            del model
    variants = ("none", "minilm_off", "minilm_on", "bge_off", "bge_on")
    for row in rows:
        top_n = row["budget"]["top_n"] if row["budget"] is not None else 0
        base_lists = [[(cid, 1.0) for cid in q["retrieved"]] for q in row["queries"]]
        baseline = final_context(base_lists, top_n, None)
        row["outcomes"] = {"none": {
            "context": baseline,
            "metrics": item_metrics(baseline, baseline, row["gold_evidence_sets"]),
        }}
        for name in MODELS:
            ranked = [q["measured"][name]["ranked"] for q in row["queries"]]
            for suffix, floor in (("off", None), ("on", 0.5)):
                context = final_context(ranked, top_n, floor)
                row["outcomes"][f"{name}_{suffix}"] = {
                    "context": context,
                    "metrics": item_metrics(baseline, context, row["gold_evidence_sets"]),
                }
    summaries = {}
    for variant in variants:
        summaries[variant] = summarize([
            {"source": r["source"], "question_type": r["question_type"],
             "metrics": r["outcomes"][variant]["metrics"]} for r in rows
        ])
    latencies = {
        name: latency_summary([[q["measured"][name]["seconds"] for q in r["queries"]
                                if q["measured"][name]["seconds"] is not None] for r in rows])
        for name in MODELS
    }
    end = environment()
    if any(sha(path) != digest for path, digest in PINS.items()) or any(
        sha(ROOT / path) != digest for path, digest in fingerprints.items()
    ):
        raise RuntimeError("input changed while measuring")
    packet = {"source_sha256": {
        str(path.relative_to(ROOT)): digest for path, digest in PINS.items()},
              "code_sha256": fingerprints, "corpus_key": meta["bm25_index_key"],
              "system_identifier": system_id, "models": MODELS, "device": device,
              "protocol": "completed reranks regardless of time; floor off/on 0.50; "
                          "per-subquery scores, served interleave and budget; strict >3s timeout",
              "start": start, "end": end, "latencies": latencies, "summaries": summaries,
              "items": rows}
    output = ROOT / "eval/runs" / f"paired-rerank-{uuid.uuid4().hex[:12]}.json"
    with output.open("x") as fh:
        json.dump(packet, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write("\n")
    print(f"output={output.relative_to(ROOT)} sha256={sha(output)}", flush=True)


if __name__ == "__main__":
    main()
