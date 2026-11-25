import hashlib
import json
import sys

import pytest

from scripts import eval_run


def test_explicit_dataset_identity_and_resume(tmp_path):
    path = tmp_path / "items.jsonl"
    raw = b'{"item_id":"one","source":"handwritten","question_type":"unanswerable"}\n'
    path.write_bytes(raw)
    items, identity = eval_run.load_datasets(str(path), None)
    assert list(items) == ["one"]
    assert identity == {str(path.resolve()): hashlib.sha256(raw).hexdigest()}
    assert eval_run.load_datasets(None, identity) == (items, identity)
    assert eval_run.load_datasets(str(path), identity) == (items, identity)
    other = tmp_path / "other.jsonl"
    other.write_bytes(raw)
    with pytest.raises(SystemExit):
        eval_run.load_datasets(str(other), identity)
    path.write_bytes(raw + b"\n")
    with pytest.raises(SystemExit):
        eval_run.load_datasets(None, identity)


def test_legacy_identity_is_filename_mapping(tmp_path, monkeypatch):
    path = tmp_path / "old_candidates.jsonl"
    path.write_text('{"item_id":"old"}\n', encoding="utf-8")
    monkeypatch.setattr(eval_run, "DATASETS", [path])
    items, identity = eval_run.load_datasets(None, None)
    assert list(items) == ["old"]
    assert identity == {path.name: hashlib.sha256(path.read_bytes()).hexdigest()}
    assert eval_run.load_datasets(None, identity) == (items, identity)


@pytest.mark.parametrize("separate_files", [False, True])
def test_duplicate_item_ids_are_rejected(tmp_path, monkeypatch, separate_files):
    first = tmp_path / "first.jsonl"
    second = tmp_path / "second.jsonl"
    row = '{"item_id":"duplicate"}\n'
    first.write_text(row if separate_files else row + row, encoding="utf-8")
    if separate_files:
        second.write_text(row, encoding="utf-8")
    monkeypatch.setattr(eval_run, "DATASETS", [first, second] if separate_files else [first])
    with pytest.raises(SystemExit, match="duplicate"):
        eval_run.load_datasets(None, None)


@pytest.mark.parametrize(
    "mode,extra",
    [
        ("--report", []),
        ("--rescore", ["0.5"]),
        ("--reverify", ["tag"]),
    ],
)
def test_saved_mode_refuses_when_corpus_preflight_fails(tmp_path, monkeypatch, mode, extra):
    path = tmp_path / "data.jsonl"
    path.write_text('{"item_id":"chosen"}\n', encoding="utf-8")
    identity = {str(path.resolve()): hashlib.sha256(path.read_bytes()).hexdigest()}
    (tmp_path / "r.meta.json").write_text(json.dumps({"datasets": identity}), encoding="utf-8")
    before = {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    monkeypatch.setattr(eval_run, "eval_run", lambda: {"runs_dir": str(tmp_path)})

    def fail_preflight(gen, run_cfg, datasets, **kwargs):
        assert datasets == identity
        raise SystemExit("corpus preflight failed")

    monkeypatch.setattr(eval_run, "current_meta", fail_preflight)
    monkeypatch.setattr(eval_run, "rebuild_report", lambda *args: pytest.fail("report executed"))
    monkeypatch.setattr(eval_run, "rescore_run", lambda *args: pytest.fail("rescore executed"))
    monkeypatch.setattr(eval_run, "reverify_run", lambda *args: pytest.fail("reverify executed"))
    monkeypatch.setattr(sys, "argv", ["eval_run", mode, "r", *extra])
    with pytest.raises(SystemExit, match="corpus preflight failed"):
        eval_run.main()
    assert {p.name: p.read_bytes() for p in tmp_path.iterdir()} == before


def test_plan_never_builds_runtime_metadata(tmp_path, monkeypatch, capsys):
    path = tmp_path / "items.jsonl"
    path.write_text(
        json.dumps({"item_id": "h", "source": "handwritten", "question_type": "natural_phrasing"})
        + "\n"
    )
    monkeypatch.setattr(sys, "argv", ["eval_run", "--dataset", str(path)])
    monkeypatch.setattr(eval_run, "current_meta", lambda *args: pytest.fail("runtime metadata"))
    eval_run.main()
    out = capsys.readouterr().out
    assert str(path.resolve()) in out and "handwritten" in out and "natural_phrasing" in out


@pytest.mark.parametrize("mode", ["--resume", "--report", "--rescore", "--reverify"])
def test_saved_run_loads_selected_dataset_before_work(tmp_path, monkeypatch, mode):
    path = tmp_path / "data.jsonl"
    path.write_text('{"item_id":"chosen"}\n', encoding="utf-8")
    identity = {str(path.resolve()): hashlib.sha256(path.read_bytes()).hexdigest()}
    (tmp_path / "r.meta.json").write_text(
        json.dumps({"datasets": identity, "item_order": [], "run_id": "r", "k": 10})
    )
    monkeypatch.setattr(
        eval_run, "eval_run", lambda: {"runs_dir": str(tmp_path), "k": 10, "nli_threshold": None}
    )
    monkeypatch.setattr(eval_run, "current_meta", lambda *args, **kwargs: {"datasets": args[2]})
    seen = []
    monkeypatch.setattr(
        eval_run, "rebuild_report", lambda runs, run_id, items, cfg: seen.append(items)
    )
    monkeypatch.setattr(eval_run, "format_report", lambda report: "report")
    monkeypatch.setattr(eval_run, "rescore_run", lambda items, *args: seen.append(items))
    monkeypatch.setattr(eval_run, "reverify_run", lambda items, *args: seen.append(items))
    monkeypatch.setattr(eval_run, "build_report", lambda items, *args: seen.append(items) or {})
    extra = {"--rescore": ["0.5"], "--reverify": ["tag"]}.get(mode, [])
    argv = ["eval_run", mode, "r", *extra]
    monkeypatch.setattr(sys, "argv", argv)
    eval_run.main()
    assert list(seen[0]) == ["chosen"]


@pytest.mark.parametrize(
    "mode,extra",
    [
        ("--resume", []),
        ("--report", []),
        ("--rescore", ["0.5"]),
        ("--reverify", ["tag"]),
    ],
)
def test_dataset_mismatch_exits_before_runtime_and_writes(tmp_path, monkeypatch, mode, extra):
    path = tmp_path / "data.jsonl"
    path.write_text('{"item_id":"chosen"}\n', encoding="utf-8")
    (tmp_path / "r.meta.json").write_text(json.dumps({"datasets": {str(path): "old"}}))
    before = {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    monkeypatch.setattr(eval_run, "eval_run", lambda: {"runs_dir": str(tmp_path)})
    monkeypatch.setattr(eval_run, "current_meta", lambda *args: pytest.fail("runtime metadata"))
    monkeypatch.setattr(sys, "argv", ["eval_run", mode, "r", *extra])
    with pytest.raises(SystemExit):
        eval_run.main()
    assert {p.name: p.read_bytes() for p in tmp_path.iterdir()} == before


def test_plan_subset_counts_only_selected_items(tmp_path, monkeypatch, capsys):
    path = tmp_path / "data.jsonl"
    path.write_text(
        "\n".join(
            json.dumps({"item_id": i, "source": "handwritten", "question_type": i})
            for i in ("a", "b")
        )
        + "\n"
    )
    subset = tmp_path / "subset.yaml"
    subset.write_text("items:\n  handwritten: [b]\n", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["eval_run", "--dataset", str(path), "--subset", str(subset)])
    eval_run.main()
    assert "items 1;" in capsys.readouterr().out


def test_pending_verdict_does_not_enter_abstention_matrix():
    from eval.runner import _abstention

    abstention = _abstention([(True, "PENDING_NLI"), (False, "PASS")])
    assert abstention["counts"]["pending"] == 1
    assert abstention["counts"]["answered_answerable"] == 1
    assert abstention["false_answer_rate"] == "pending NLI threshold (F-125)"


def test_handwritten_report_has_counts_and_pending_gap():
    from eval.runner import build_report, format_report

    items = {}
    results = []
    for i, (kind, expected, verdict) in enumerate(
        [
            ("unanswerable", True, "PASS"),
            ("adversarial", True, "ABSTAIN"),
            ("natural_phrasing", False, "ABSTAIN"),
            ("comparison", False, "PASS"),
        ]
    ):
        iid = str(i)
        items[iid] = {
            "item_id": iid,
            "source": "handwritten",
            "question_type": kind,
            "reference_answer": "1, 2, 3" if kind == "comparison" else "",
            "tags": [],
            "gold_evidence_sets": [],
            "expected_abstain": expected,
        }
        results.append(
            {
                "item_id": iid,
                "retrieved": [],
                "answer": {"text": "", "claims": [], "abstained": verdict == "ABSTAIN"},
                "verdict": verdict,
                "model_served": "test",
            }
        )
    report = build_report(
        items,
        results,
        {
            "run_id": "test",
            "backend": "claude_cli",
            "model_requested": "test",
            "retrieval_stage": "test",
        },
        10,
    )
    assert report["columns"]["handwritten"]["abstention"]["counts"] == {
        "answered_answerable": 1,
        "abstained_answerable": 1,
        "answered_unanswerable": 1,
        "abstained_unanswerable": 1,
        "pending": 0,
    }
    assert report["natural_phrasing_gap"] == "pending definition (F-20)"
    text = format_report(report)
    for value in ("unanswerable", "adversarial", "natural_phrasing", "answered_unanswerable"):
        assert value in text
