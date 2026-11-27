"""Unpaired natural-phrasing control gap over stored pre-rerank lists."""

from eval.metrics.retrieval import sufficiency_at_k


def natural_phrasing_gap(items: dict, results: list[dict]) -> dict:
    groups = {"generated": [], "natural": []}
    for result in results:
        item = items[result["item_id"]]
        if item["expected_abstain"]:
            continue
        if item["source"] in ("xbrl_auto", "llm_seeded"):
            group = "generated"
        elif item["source"] == "handwritten" and item["question_type"] == "natural_phrasing":
            group = "natural"
        else:
            continue
        groups[group].append(sufficiency_at_k(result["retrieved"], item["gold_evidence_sets"], 10))

    summary = {}
    for group, scores in groups.items():
        measured = [score for score in scores if score is not None]
        summary[group] = {
            "hits": sum(measured),
            "eligible": len(measured),
            "no_gold": len(scores) - len(measured),
            "sufficiency_at_10": sum(measured) / len(measured) if measured else None,
        }
    generated = summary["generated"]["sufficiency_at_10"]
    natural = summary["natural"]["sufficiency_at_10"]
    return {
        "gap": generated - natural if generated is not None and natural is not None else None,
        **summary,
    }
