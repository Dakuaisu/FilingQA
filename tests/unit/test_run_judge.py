import hashlib
import json
import sys

import pytest

from eval.judge.run import aggregate, eligible, score_run


def fake_verdict():
    return {
        "item_id": "a",
        "score": 5,
        "rationale": "ok",
        "judge_backend": "fake",
        "judge_model": "judge",
        "judge_family": "judge",
        "generator_model": "generator",
        "same_family_as_generator": False,
    }


def test_eligibility_excludes_both_abstentions_and_null_reference():
    item = {"reference_answer": "yes"}
    result = {"answer": {"abstained": False}, "verdict": "PASS"}
    assert eligible(item, result)
    assert not eligible({"reference_answer": None}, result)
    assert not eligible(item, {**result, "answer": {"abstained": True}})
    assert not eligible(item, {**result, "verdict": "ABSTAIN"})


def test_aggregate_reports_incomplete_and_normalized_mean():
    items = {
        "a": {"source": "handwritten", "question_type": "table", "reference_answer": "yes"},
        "b": {"source": "handwritten", "question_type": "table", "reference_answer": "yes"},
    }
    results = [{"item_id": i, "answer": {"abstained": False}, "verdict": "PASS"} for i in items]
    partial = aggregate(items, results, [{"item_id": "a", "score": 4}])
    assert partial["aggregate"]["normalized_mean"] is None
    assert partial["aggregate"]["mean_score"] == 4
    complete = aggregate(
        items, results, [{"item_id": "a", "score": 4}, {"item_id": "b", "score": 2}]
    )
    assert complete["aggregate"]["normalized_mean"] == 0.6
    assert complete["aggregate"]["mean_score"] == 3
    assert complete["aggregate"]["share_at_least_4"] == 0.5


def test_score_cli_resumes_without_calling_judge_again(tmp_path, monkeypatch):
    from eval.judge import run
    from scripts import judge as cli

    items = [
        {
            "item_id": "a",
            "source": "handwritten",
            "question_type": "table",
            "question": "Q?",
            "reference_answer": "yes",
        }
    ]
    result = {
        "item_id": "a",
        "answer": {"text": "yes", "abstained": False},
        "verdict": "PASS",
        "model_served": "generator",
    }
    dataset = tmp_path / "dataset.jsonl"
    dataset.write_text(json.dumps(items[0]) + "\n")
    meta = {
        "datasets": {str(dataset): hashlib.sha256(dataset.read_bytes()).hexdigest()},
        "item_order": ["a"],
    }
    (tmp_path / "synthetic.meta.json").write_text(json.dumps(meta))
    (tmp_path / "synthetic.results.jsonl").write_text(json.dumps(result) + "\n")
    monkeypatch.setattr(cli, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(cli, "eval_run", lambda: {"runs_dir": "."})
    monkeypatch.setattr(cli, "eval_judge", lambda: {"tier": "small"})
    monkeypatch.setattr(cli, "generation", lambda: {"backend": "claude_cli", "small": "fake"})
    calls = []
    monkeypatch.setattr(run, "judge", lambda *args: calls.append(args) or fake_verdict())
    monkeypatch.setattr(sys, "argv", ["judge", "score", "synthetic"])
    cli.main()
    cli.main()
    assert len(calls) == 1
    assert len((tmp_path / "synthetic.judge.jsonl").read_text().splitlines()) == 1


def test_score_rejects_foreign_records_without_judge_call(tmp_path, monkeypatch):
    from eval.judge import run

    path = tmp_path / "judge.jsonl"
    path.write_text(json.dumps({"item_id": "foreign", "score": 5}) + "\n")
    monkeypatch.setattr(run, "judge", lambda *args: pytest.fail("judge called"))
    with pytest.raises(ValueError):
        score_run("synthetic", {}, [], path, {"backend": "fake"}, "small")


def test_restart_repairs_interrupted_record(tmp_path, monkeypatch):
    from eval.judge import run

    item = {"item_id": "a", "reference_answer": "yes"}
    result = {
        "item_id": "a",
        "answer": {"text": "yes", "abstained": False},
        "verdict": "PASS",
        "model_served": "generator",
    }
    path = tmp_path / "judge.jsonl"
    path.write_text('{"item_id":')
    monkeypatch.setattr(run, "judge", lambda *args: fake_verdict())
    score_run("synthetic", {"a": item}, [result], path, {"backend": "fake"}, "small")
    assert json.loads(path.read_text())["score"] == 5


def test_compare_uses_only_complete_correctness():
    from eval.compare import value

    report = {
        "columns": {
            "aggregate": {"answer_correctness": {"complete": False, "normalized_mean": 0.9}}
        }
    }
    assert value(report, "aggregate", "answer_correctness")[0] is None
    report["columns"]["aggregate"]["answer_correctness"]["complete"] = True
    assert value(report, "aggregate", "answer_correctness")[0] == 0.9


def test_scored_sidecar_flows_through_rebuilt_report_to_compare(tmp_path, monkeypatch):
    from eval.compare import value
    from eval.judge import run
    from scripts import eval_run

    items = {
        "a": {
            "item_id": "a",
            "question": "Q?",
            "reference_answer": "yes",
            "source": "handwritten",
            "question_type": "table",
        }
    }
    result = {
        "item_id": "a",
        "answer": {"text": "yes", "abstained": False},
        "verdict": "PASS",
        "model_served": "generator",
    }
    meta = {"item_order": ["a"], "run_id": "synthetic", "k": 10}
    (tmp_path / "synthetic.meta.json").write_text(json.dumps(meta))
    (tmp_path / "synthetic.results.jsonl").write_text(json.dumps(result) + "\n")
    monkeypatch.setattr(run, "judge", lambda *args: fake_verdict())
    monkeypatch.setattr(
        eval_run, "build_report", lambda *args: {"columns": {"aggregate": {}, "handwritten": {}}}
    )
    score_run(
        "synthetic",
        items,
        [result],
        tmp_path / "synthetic.judge.jsonl",
        {"backend": "fake"},
        "small",
    )

    report = eval_run.rebuild_report(tmp_path, "synthetic", items, {"nli_threshold": None})

    assert report["answer_correctness"]["aggregate"]["mean_score"] == 5
    assert value(report, "aggregate", "answer_correctness") == (1.0, None)
    assert value(report, "handwritten", "answer_correctness") == (1.0, None)
