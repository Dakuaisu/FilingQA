import hashlib
import json
from pathlib import Path

import yaml

from eval import compare
from eval.golden_policy import eligible_report, is_golden
from scripts.draw_fast import draw


def test_golden_identity_requires_pinned_hash_and_name():
    path = Path("eval/datasets/golden_v1.jsonl")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert is_golden({str(path.resolve()): digest})
    assert not is_golden({str(path.resolve()): "0" * 64})
    assert not is_golden({"other.jsonl": digest})
    assert not is_golden({"golden_v1.jsonl": digest, "other.jsonl": digest})
    assert eligible_report({"datasets": {"golden_v1.jsonl": digest}, "backend": "claude_cli"})
    assert eligible_report({"datasets": {"golden_v1.jsonl": digest}, "backend": "anthropic_api"})
    assert not eligible_report({"datasets": {"golden_v1.jsonl": digest}, "backend": "unknown"})


def test_fast_subset_v2_extends_v1_with_pinned_golden_handwritten():
    v1 = yaml.safe_load(Path("eval/fast_subset_v1.yaml").read_text())
    v2 = yaml.safe_load(Path("eval/fast_subset_v2.yaml").read_text())
    golden = {
        item["item_id"]: item
        for line in Path("eval/datasets/golden_v1.jsonl").read_text().splitlines()
        if (item := json.loads(line))
    }
    old = [i for group in v1["items"].values() for i in group]
    new = [i for group in v2["items"].values() for i in group]
    assert len(old) == 42 and len(new) == len(set(new)) == 60
    assert set(old) <= set(new) <= golden.keys()
    assert len(v2["items"]["handwritten"]) == 18
    assert all(golden[i]["source"] == source for source, ids in v2["items"].items() for i in ids)
    handwritten = {i: item for i, item in golden.items() if item["source"] == "handwritten"}
    assert (
        v2["items"]["handwritten"] == draw(handwritten, 0, 18, v1["seed"])["items"]["handwritten"]
    )


def test_fast_target_verifies_freeze_before_golden_run():
    makefile = Path("Makefile").read_text()
    recipe = makefile.split("\neval-fast:\n", 1)[1].split("\neval-gate:", 1)[0]
    assert recipe.index("scripts.verify_freeze") < recipe.index("scripts.eval_run --run")
    assert "--dataset eval/datasets/golden_v1.jsonl" in recipe
    assert "--subset eval/fast_subset_v2.yaml" in recipe
    assert recipe.index("rm -f build/eval_fast.json") < recipe.index("scripts.verify_freeze")


def test_cost_na_never_becomes_a_passing_gate():
    report = {"development_run": False, "columns": {"aggregate": {"cost_per_query": "cost n/a"}}}
    value, reason = compare.value(report, "aggregate", "cost_per_query")
    assert value is None and reason.startswith("pending")


def test_legacy_golden_classification_requires_complete_report():
    digest = hashlib.sha256(Path("eval/datasets/golden_v1.jsonl").read_bytes()).hexdigest()
    report = {
        "backend": "claude_cli",
        "development_run": True,
        "datasets": {"/old/checkout/golden_v1.jsonl": digest},
        "subset": {"items": 2, "sha256": "subset"},
        "columns": {"aggregate": {"items": 1}},
    }
    assert not compare.passed(compare.rows(report, {}, None))
    report["columns"]["aggregate"]["items"] = 2
    assert not any(r["metric"] in {"dataset", "backend"} for r in compare.rows(report, {}, None))
    assert not compare.passed(compare.rows(report, {}, None))
    assert not compare.passed(
        compare.rows(report, {}, {**report, "columns": {"aggregate": {"items": 1}}})
    )
