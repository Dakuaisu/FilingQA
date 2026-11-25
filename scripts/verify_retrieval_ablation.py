#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
# Run: .venv/bin/python scripts/verify_retrieval_ablation.py PATH_TO_PACKET
"""Independently check a saved ablation without loading a model or database."""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEIGHTS = {"hybrid_1_1": (1.0, 1.0), "hybrid_1.5_1": (1.5, 1.0), "hybrid_1_1.5": (1.0, 1.5)}
MODES = ("dense", "sparse", *WEIGHTS)
DEPTHS = (20, 50, 100)
SOURCES = ("aggregate", "xbrl_auto", "llm_seeded", "handwritten")


def main() -> None:
    path = Path(sys.argv[1])
    packet = json.loads(path.read_text())
    dataset_path = ROOT / "eval/datasets/golden_v1.jsonl"
    dataset_bytes = dataset_path.read_bytes()
    if hashlib.sha256(dataset_bytes).hexdigest() != packet["dataset_sha256"]:
        raise RuntimeError("dataset digest mismatch")
    manifest = ROOT / "eval/datasets/golden_v1_manifest.json"
    if hashlib.sha256(manifest.read_bytes()).hexdigest() != packet["manifest_sha256"]:
        raise RuntimeError("manifest digest mismatch")
    for name, digest in packet["input_sha256"].items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError(f"input digest mismatch: {name}")
    golden = [json.loads(line) for line in dataset_bytes.splitlines() if line]
    golden = [row for row in golden if not row["expected_abstain"]]
    rows = packet["items"]
    if len(rows) != len(golden):
        raise RuntimeError("item count mismatch")
    for row, item in zip(rows, golden, strict=True):
        for field in (
            "item_id",
            "question",
            "source",
            "question_type",
            "reviewed_by_human",
            "gold_evidence_sets",
        ):
            if row[field] != item[field]:
                raise RuntimeError(f"gold mismatch: {item['item_id']} {field}")
        for depth in DEPTHS:
            lists = [row["rankings"][mode][str(depth)] for mode in ("dense", "sparse")]
            if any(len(branch) > depth or len(set(branch)) != len(branch) for branch in lists):
                raise RuntimeError(f"invalid branch ranking: {item['item_id']} {depth}")
            for mode, weights in WEIGHTS.items():
                scores = {}
                best = {}
                for branch, weight in zip(lists, weights, strict=True):
                    for rank, cid in enumerate(branch, 1):
                        scores[cid] = scores.get(cid, 0.0) + weight / (60 + rank)
                        best[cid] = min(best.get(cid, rank), rank)
                expected = sorted(scores, key=lambda cid: (-scores[cid], best[cid], cid))[:depth]
                if row["rankings"][mode][str(depth)] != expected:
                    raise RuntimeError(f"fusion mismatch: {item['item_id']} {mode} {depth}")
    cells = 0
    for cohort in ("all", "reviewed"):
        for source in SOURCES:
            chosen = [
                r
                for r in rows
                if (cohort == "all" or r["reviewed_by_human"])
                and (source == "aggregate" or r["source"] == source)
            ]
            for mode in MODES:
                for depth in DEPTHS:
                    for key, cutoff in (("results_at_depth", depth), ("results_at_10", 10)):
                        sufficient = 0
                        recalls = []
                        for row in chosen:
                            groups = row["gold_evidence_sets"]
                            if not groups:
                                continue
                            if any(not group for group in groups):
                                raise RuntimeError("empty gold evidence group")
                            top = set(row["rankings"][mode][str(depth)][:cutoff])
                            coverages = [
                                len(top.intersection(group)) / len(set(group)) for group in groups
                            ]
                            sufficient += int(any(value == 1 for value in coverages))
                            recalls.append(max(coverages))
                        actual = packet[key][cohort][source][mode][str(depth)]
                        expected = {
                            "population": len(chosen),
                            "scored": len(recalls),
                            "no_gold": len(chosen) - len(recalls),
                            "sufficient": sufficient,
                            "mean_recall": sum(recalls) / len(recalls) if recalls else None,
                        }
                        if actual != expected:
                            raise RuntimeError(
                                f"cell mismatch: {key} {cohort} {source} {mode} {depth}"
                            )
                        if actual["mean_recall"] is not None and not math.isfinite(
                            actual["mean_recall"]
                        ):
                            raise RuntimeError("non-finite recall")
                        cells += 1
    print(
        f"PASS: {len(rows)} items, {len(rows) * len(DEPTHS) * len(WEIGHTS)} fusions, "
        f"{cells} summary cells; sha256={hashlib.sha256(path.read_bytes()).hexdigest()}"
    )
    for cohort in ("all", "reviewed"):
        for source in SOURCES:
            for mode in MODES:
                values = [packet["results_at_depth"][cohort][source][mode][str(d)] for d in DEPTHS]
                formatted = " ".join(
                    f"{v['sufficient']}/{v['scored']}:{v['mean_recall']}" for v in values
                )
                print(cohort, source, mode, formatted)


if __name__ == "__main__":
    main()
