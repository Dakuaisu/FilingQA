"""Scoring of paired reranker replays over the served per-query lists."""

from __future__ import annotations

from typing import TypedDict

from api.query.rerank import apply_floor
from eval.metrics.retrieval import mrr, sufficiency_at_k
from eval.pipeline import interleave


class ItemMetrics(TypedDict):
    sufficient: bool | None
    mrr: float | None
    existing_empty: bool
    induced_empty: bool


class LatencySummary(TypedDict):
    calls: int
    timeout_calls: int
    timeout_items: int
    p50_seconds: float | None
    p95_seconds: float | None
    item_p50_seconds: float | None
    item_p95_seconds: float | None


class ScoredRow(TypedDict):
    source: str
    question_type: str
    metrics: ItemMetrics


class MetricSummary(TypedDict):
    population: int
    scored: int
    sufficient: int
    mean_mrr: float | None
    existing_empty: int
    induced_empty: int


def final_context(
    ranked: list[list[tuple[str, float]]], top_n: int, floor: float | None
) -> list[str]:
    per_query = [
        [cid for cid, _ in (scores if floor is None else apply_floor(scores, floor))[:top_n]]
        for scores in ranked
    ]
    return interleave(per_query, top_n)


def item_metrics(baseline: list[str], result: list[str], gold: list[list[str]]) -> ItemMetrics:
    return {
        "sufficient": sufficiency_at_k(result, gold, max(len(result), 1)),
        "mrr": mrr(result, gold),
        "existing_empty": not baseline,
        "induced_empty": bool(baseline) and not result,
    }


def latency_summary(item_calls: list[list[float]]) -> LatencySummary:
    durations = sorted(value for calls in item_calls for value in calls)

    def percentile(values: list[float], fraction: float) -> float | None:
        if not values:
            return None
        index = (len(values) - 1) * fraction
        lower = int(index)
        upper = min(lower + 1, len(values) - 1)
        return values[lower] + (values[upper] - values[lower]) * (index - lower)

    totals = sorted(sum(calls) for calls in item_calls if calls)
    return {
        "calls": len(durations),
        "timeout_calls": sum(value > 3.0 for value in durations),
        "timeout_items": sum(any(value > 3.0 for value in calls) for calls in item_calls),
        "p50_seconds": percentile(durations, 0.5),
        "p95_seconds": percentile(durations, 0.95),
        "item_p50_seconds": percentile(totals, 0.5),
        "item_p95_seconds": percentile(totals, 0.95),
    }


def summarize(rows: list[ScoredRow]) -> dict[str, dict[str, MetricSummary]]:
    result: dict[str, dict[str, MetricSummary]] = {}
    for group in ("source", "question_type"):
        result[group] = {}
        names = sorted({row[group] for row in rows})
        for name in ("aggregate", *names):
            members = [row["metrics"] for row in rows if name == "aggregate" or row[group] == name]
            scores = [m["mrr"] for m in members if m["mrr"] is not None]
            result[group][name] = {
                "population": len(members),
                "scored": len(scores),
                "sufficient": sum(m["sufficient"] is True for m in members),
                "mean_mrr": sum(scores) / len(scores) if scores else None,
                "existing_empty": sum(m["existing_empty"] for m in members),
                "induced_empty": sum(m["induced_empty"] for m in members),
            }
    return result
