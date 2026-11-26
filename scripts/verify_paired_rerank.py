#!/usr/bin/env python3
"""Verify a paired rerank packet without a model or database."""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = ("minilm", "bge")
VARIANTS = ("none", "minilm_off", "minilm_on", "bge_off", "bge_on")


def context(lists: list[list[list]], budget: int, floor: float | None) -> list[str]:
    per_query = [[cid for cid, score in ranking if floor is None or score >= floor][:budget]
                 for ranking in lists]
    output = []
    for index in range(max((len(ranking) for ranking in per_query), default=0)):
        for ranking in per_query:
            if index < len(ranking) and ranking[index] not in output:
                output.append(ranking[index])
    return output[:budget]


def check_ranking(candidates: list[str], measured: dict) -> None:
    ranked = measured["ranked"]
    seconds = measured["seconds"]
    if len(candidates) != len(ranked) or {c for c, _ in ranked} != set(candidates):
        raise ValueError("rerank candidates mismatch")
    if candidates:
        if seconds is None or not math.isfinite(seconds) or seconds < 0:
            raise ValueError("invalid latency")
    elif seconds is not None:
        raise ValueError("empty candidate list has a measured call")
    if any(not math.isfinite(score) or not 0 <= score <= 1 for _, score in ranked):
        raise ValueError("invalid score")
    if ranked != sorted(ranked, key=lambda x: (-x[1], x[0])):
        raise ValueError("score order mismatch")


def scores(baseline: list[str], result: list[str], gold: list[list[str]]) -> dict:
    found = set(result)
    union = set().union(*map(set, gold))
    return {
        "sufficient": any(set(group) <= found for group in gold) if gold else None,
        "mrr": next((1 / i for i, cid in enumerate(result, 1) if cid in union), 0.0)
        if gold else None,
        "existing_empty": not baseline,
        "induced_empty": bool(baseline) and not result,
    }


def stats(rows: list[dict], variant: str) -> dict:
    result = {}
    for key in ("source", "question_type"):
        result[key] = {}
        for label in ("aggregate", *sorted({row[key] for row in rows})):
            members = [r["outcomes"][variant]["metrics"] for r in rows
                       if label == "aggregate" or r[key] == label]
            mrrs = [m["mrr"] for m in members if m["mrr"] is not None]
            result[key][label] = {
                "population": len(members), "scored": len(mrrs),
                "sufficient": sum(m["sufficient"] is True for m in members),
                "mean_mrr": sum(mrrs) / len(mrrs) if mrrs else None,
                "existing_empty": sum(m["existing_empty"] for m in members),
                "induced_empty": sum(m["induced_empty"] for m in members),
            }
    return result


def percentile(values: list[float], fraction: float) -> float | None:
    if not values:
        return None
    values = sorted(values)
    position = (len(values) - 1) * fraction
    lower = int(position)
    upper = min(lower + 1, len(values) - 1)
    return values[lower] + (values[upper] - values[lower]) * (position - lower)


def latency(rows: list[dict], model: str) -> dict:
    per_item = [[q["measured"][model]["seconds"] for q in r["queries"]
                 if q["measured"][model]["seconds"] is not None] for r in rows]
    durations = [s for item in per_item for s in item]
    totals = [sum(item) for item in per_item if item]
    return {"calls": len(durations), "timeout_calls": sum(s > 3 for s in durations),
            "timeout_items": sum(any(s > 3 for s in item) for item in per_item),
            "p50_seconds": percentile(durations, 0.5), "p95_seconds": percentile(durations, 0.95),
            "item_p50_seconds": percentile(totals, 0.5),
            "item_p95_seconds": percentile(totals, 0.95)}


def main() -> None:
    path = Path(sys.argv[1])
    packet = json.loads(path.read_text())
    for name, digest in (packet["source_sha256"] | packet["code_sha256"]).items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest:
            raise ValueError(f"input digest mismatch: {name}")
    dataset = [json.loads(line) for line in
               (ROOT / "eval/datasets/golden_v1.jsonl").read_text().splitlines()]
    gold = {row["item_id"]: row for row in dataset if not row["expected_abstain"]}
    source = [json.loads(line) for line in
              (ROOT / "eval/runs/35b3efbbfd5d.results.jsonl").read_text().splitlines()]
    traces = {row["item_id"]: row for row in source}
    rows = packet["items"]
    if len(rows) != 332 or len(gold) != 332 or {row["item_id"] for row in rows} != set(gold):
        raise ValueError("answerable cohort mismatch")
    for row in rows:
        original, trace = gold[row["item_id"]], traces[row["item_id"]]
        for key in ("source", "question_type", "reviewed_by_human", "gold_evidence_sets"):
            if row[key] != original[key]:
                raise ValueError(f"gold mismatch {row['item_id']} {key}")
        if row["budget"] != trace["budget"] or row["intent"] != trace["intent"]:
            raise ValueError("route mismatch")
        if len(row["queries"]) != len(trace["queries"]):
            raise ValueError("subquery count mismatch")
        for q, saved in zip(row["queries"], trace["queries"], strict=True):
            if q["query"] != saved["query"] or q["retrieved"] != saved["retrieved"]:
                raise ValueError("subquery input mismatch")
            for model in MODELS:
                check_ranking(q["retrieved"], q["measured"][model])
        n = row["budget"]["top_n"] if row["budget"] is not None else 0
        base_lists = [[[cid, 1.0] for cid in q["retrieved"]] for q in row["queries"]]
        baseline = context(base_lists, n, None)
        expected = {"none": baseline}
        for model in MODELS:
            lists = [q["measured"][model]["ranked"] for q in row["queries"]]
            expected[f"{model}_off"] = context(lists, n, None)
            expected[f"{model}_on"] = context(lists, n, 0.5)
        for variant, ids in expected.items():
            if row["outcomes"][variant] != {"context": ids,
                    "metrics": scores(baseline, ids, row["gold_evidence_sets"])}:
                raise ValueError(f"outcome mismatch {row['item_id']} {variant}")
    for variant in VARIANTS:
        if packet["summaries"][variant] != stats(rows, variant):
            raise ValueError(f"summary mismatch {variant}")
    for model in MODELS:
        if packet["latencies"][model] != latency(rows, model):
            raise ValueError(f"latency mismatch {model}")
    print(f"PASS: {len(rows)} items; all labels, rankings, outcomes, summaries and latencies; "
          f"sha256={hashlib.sha256(path.read_bytes()).hexdigest()}")
    for variant in VARIANTS:
        for group in ("aggregate", "xbrl_auto", "llm_seeded", "handwritten"):
            print(variant, group, packet["summaries"][variant]["source"][group])
        print(variant, "natural_phrasing",
              packet["summaries"][variant]["question_type"].get("natural_phrasing"))
    for model in MODELS:
        print(model, "latency", packet["latencies"][model])


if __name__ == "__main__":
    main()
