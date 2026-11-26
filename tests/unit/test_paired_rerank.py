import pytest

from eval.paired_rerank import final_context, item_metrics, latency_summary, summarize
from scripts.verify_paired_rerank import check_ranking, context, scores


def test_context_interleaves_per_query_and_caps_router_budget():
    ranked = [[("a", 0.9), ("b", 0.8)], [("a", 0.9), ("c", 0.7)]]
    assert final_context(ranked, 3, None) == ["a", "b", "c"]


def test_floor_is_applied_before_interleaving():
    ranked = [[("a", 0.49)], [("b", 0.5), ("c", 0.3)]]
    assert final_context(ranked, 3, 0.5) == ["b"]


def test_empty_distinguishes_existing_and_induced():
    assert item_metrics([], [], [["a"]])["existing_empty"] is True
    assert item_metrics(["a"], [], [["a"]])["induced_empty"] is True
    assert item_metrics([], [], [["a"]])["induced_empty"] is False


def test_metrics_use_and_or_and_reciprocal_rank():
    result = item_metrics(["b", "a"], ["b", "a"], [["a", "b"], ["c"]])
    assert result["sufficient"] is True
    assert result["mrr"] == 1.0


def test_timeouts_count_actual_queries_and_affected_items():
    result = latency_summary([[3.0, 3.001], [], [2.0]])
    assert result["calls"] == 3
    assert result["timeout_calls"] == 1
    assert result["timeout_items"] == 1
    assert result["p50_seconds"] == pytest.approx(3.0)
    assert result["item_p50_seconds"] == pytest.approx(4.0005)


def test_summary_counts_natural_phrasing_and_empty_by_source():
    rows = [
        {
            "source": "handwritten",
            "question_type": "natural_phrasing",
            "metrics": item_metrics(["a"], [], [["a"]]),
        }
    ]
    result = summarize(rows)
    assert result["source"]["handwritten"]["induced_empty"] == 1
    assert result["question_type"]["natural_phrasing"]["sufficient"] == 0


def test_independent_verifier_rejects_missing_candidate():
    with pytest.raises(ValueError, match="candidates mismatch"):
        check_ranking(["a", "b"], {"ranked": [["a", 0.7]], "seconds": 0.1})


def test_independent_verifier_rejects_invalid_score_order():
    with pytest.raises(ValueError, match="order mismatch"):
        check_ranking(["a", "b"], {"ranked": [["a", 0.5], ["b", 0.8]], "seconds": 0.1})


def test_independent_verifier_interleaves_and_respects_alternative_gold():
    ranked = [[["a", 0.9], ["b", 0.2]], [["c", 0.8], ["d", 0.5]]]
    result = context(ranked, 3, 0.5)
    assert result == ["a", "c", "d"]
    assert scores(result, result, [["a", "b"], ["c", "d"]])["sufficient"] is True
