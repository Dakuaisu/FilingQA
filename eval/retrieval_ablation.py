"""Pure, depth-specific retrieval ablation calculations."""

from __future__ import annotations

from typing import TypedDict

from api.query.retrieve import rrf_fuse
from eval.metrics.retrieval import recall_at_k, sufficiency_at_k

WEIGHTS = {"hybrid_1_1": (1.0, 1.0), "hybrid_1.5_1": (1.5, 1.0), "hybrid_1_1.5": (1.0, 1.5)}
SOURCES = ("aggregate", "xbrl_auto", "llm_seeded", "handwritten")
Rankings = dict[str, dict[int, list[str]]]


class Item(TypedDict):
    source: str
    reviewed_by_human: bool
    gold_evidence_sets: list[list[str]]
    rankings: Rankings


class Cell(TypedDict):
    population: int
    scored: int
    no_gold: int
    sufficient: int
    mean_recall: float | None


def rankings(dense: dict[int, list[str]], sparse: dict[int, list[str]], k: int) -> Rankings:
    """Fuse prefixes separately: deeper branch candidates change RRF scores."""
    result: Rankings = {name: {} for name in ("dense", "sparse", *WEIGHTS)}
    for depth in dense:
        branches = [dense[depth], sparse[depth]]
        result["dense"][depth], result["sparse"][depth] = branches
        for name, weights in WEIGHTS.items():
            result[name][depth] = rrf_fuse(branches, list(weights), k)[:depth]
    return result


def summarize(
    items: list[Item], modes: tuple[str, ...], depths: tuple[int, ...], cutoff: int | None = None
) -> dict[str, dict[str, dict[str, dict[int, Cell]]]]:
    """Score answerables, excluding missing gold and retaining empty populations."""
    result = {}
    for cohort in ("all", "reviewed"):
        result[cohort] = {}
        for source in SOURCES:
            selected = [
                item
                for item in items
                if (cohort == "all" or item["reviewed_by_human"])
                and (source == "aggregate" or item["source"] == source)
            ]
            result[cohort][source] = {}
            for mode in modes:
                result[cohort][source][mode] = {}
                for depth in depths:
                    k = depth if cutoff is None else min(cutoff, depth)
                    scoreable = [i for i in selected if i["gold_evidence_sets"]]
                    if any(not group for i in scoreable for group in i["gold_evidence_sets"]):
                        raise ValueError("empty evidence group is invalid")
                    recalls = [
                        recall_at_k(i["rankings"][mode][depth], i["gold_evidence_sets"], k)
                        for i in scoreable
                    ]
                    sufficient = sum(
                        bool(
                            sufficiency_at_k(i["rankings"][mode][depth], i["gold_evidence_sets"], k)
                        )
                        for i in scoreable
                    )
                    result[cohort][source][mode][depth] = {
                        "population": len(selected),
                        "scored": len(scoreable),
                        "no_gold": len(selected) - len(scoreable),
                        "sufficient": sufficient,
                        "mean_recall": sum(x for x in recalls if x is not None) / len(scoreable)
                        if scoreable
                        else None,
                    }
    return result
