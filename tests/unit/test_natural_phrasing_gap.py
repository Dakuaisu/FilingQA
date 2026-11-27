import pytest

from eval.compare import rows, value
from eval.metrics.natural_phrasing import natural_phrasing_gap


def item(source, kind="table", gold=True, answerable=True):
    return {
        "source": source,
        "question_type": kind,
        "expected_abstain": not answerable,
        "gold_evidence_sets": [["gold"]] if gold else [],
    }


def test_pooled_sources_are_weighted_by_items_and_exclude_no_gold():
    items = {
        "x1": item("xbrl_auto"),
        "x2": item("xbrl_auto"),
        "x3": item("xbrl_auto"),
        "s": item("llm_seeded"),
        "n": item("handwritten", "natural_phrasing"),
        "missing": item("xbrl_auto", gold=False),
        "declined": item("llm_seeded", answerable=False),
        "other": item("handwritten", "comparison"),
    }
    results = [
        {"item_id": i, "retrieved": ["gold"] if i in {"x1", "x2", "s"} else []} for i in items
    ]
    summary = natural_phrasing_gap(items, results)
    assert summary["generated"] == {
        "hits": 3,
        "eligible": 4,
        "no_gold": 1,
        "sufficiency_at_10": 0.75,
    }
    assert summary["natural"]["eligible"] == 1
    assert summary["gap"] == 0.75


def test_negative_gap_and_fixed_top_ten():
    items = {"x": item("xbrl_auto"), "n": item("handwritten", "natural_phrasing")}
    results = [
        {"item_id": "x", "retrieved": [str(i) for i in range(10)] + ["gold"]},
        {"item_id": "n", "retrieved": ["gold"]},
    ]
    assert natural_phrasing_gap(items, results)["gap"] == -1.0


@pytest.mark.parametrize("source", ["xbrl_auto", "handwritten"])
def test_missing_cohort_is_pending(source):
    it = item(source, "natural_phrasing" if source == "handwritten" else "table")
    assert natural_phrasing_gap({"a": it}, [{"item_id": "a", "retrieved": []}])["gap"] is None


def test_compare_regression_uses_maximum_delta_and_legacy_is_pending():
    def report(gap):
        return {
            "columns": {"aggregate": {}},
            "subset": {"sha256": "same"},
            "natural_phrasing_gap": {"gap": gap},
        }

    thresholds = {"regression_tolerance": {"natural_phrasing_gap": 0.05}}
    assert rows(report(0.2), thresholds, report(0.16))[0]["status"] == "pass"
    assert rows(report(0.22), thresholds, report(0.16))[0]["status"] == "fail"
    assert value({"columns": {"aggregate": {}}}, "aggregate", "natural_phrasing_gap")[0] is None
