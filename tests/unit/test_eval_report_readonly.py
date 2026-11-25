"""F-144: --report must not rewrite a run's files."""

from __future__ import annotations

import json
import sys

from scripts import eval_run


def test_rebuild_report_leaves_run_files_byte_identical(tmp_path, monkeypatch):
    run_id = "abc123def456"
    meta = {"run_id": run_id, "k": 10, "item_order": ["x1"], "backend": "claude_cli"}
    files = {
        f"{run_id}.meta.json": json.dumps(meta, indent=1) + "\n",
        f"{run_id}.results.jsonl": json.dumps({"item_id": "x1"}) + "\n",
        f"{run_id}.json": '{\n "older": "report"\n}\n',
    }
    for name, text in files.items():
        (tmp_path / name).write_text(text, encoding="utf-8")
    before = {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    monkeypatch.setattr(
        eval_run,
        "build_report",
        lambda *a: {"newer": "fields", "k": a[3], "columns": {"aggregate": {}}},
    )

    report = eval_run.rebuild_report(
        tmp_path,
        run_id,
        {"x1": {"source": "handwritten", "question_type": "table"}},
        {"nli_threshold": None},
    )

    assert report["answer_correctness"]["aggregate"]["complete"] is False
    assert {p.name: p.read_bytes() for p in tmp_path.iterdir()} == before


def test_report_explicit_export_is_machine_readable(tmp_path, monkeypatch):
    meta = {"datasets": {}}
    (tmp_path / "synthetic.meta.json").write_text(json.dumps(meta))
    monkeypatch.setattr(eval_run, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(eval_run, "eval_run", lambda: {"runs_dir": "."})
    monkeypatch.setattr(eval_run, "generation", lambda: {})
    monkeypatch.setattr(eval_run, "load_datasets", lambda *args: ({}, {}))
    monkeypatch.setattr(eval_run, "current_meta", lambda *args: {})
    report = {
        "columns": {"aggregate": {"answer_correctness": {"complete": True, "normalized_mean": 0.8}}}
    }
    monkeypatch.setattr(eval_run, "rebuild_report", lambda *args: report)
    monkeypatch.setattr(eval_run, "format_report", lambda _: "report")
    monkeypatch.setattr(
        sys, "argv", ["eval_run", "--report", "synthetic", "--report-out", "derived.json"]
    )
    eval_run.main()
    from eval.compare import value

    exported = json.loads((tmp_path / "derived.json").read_text())
    assert value(exported, "aggregate", "answer_correctness")[0] == 0.8
