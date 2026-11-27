"""GET /metrics (dashboard data): development runs never contribute a value, and the
README status section agrees with the payload. Inline run files for the first."""

from __future__ import annotations

import json
import re

import yaml

from api import metrics
from api.config import REPO_ROOT

SENTINEL = 0.123457


def _write(path, doc):
    path.write_text(json.dumps(doc), encoding="utf-8")


def _report(dev: bool):
    col = {"sufficiency@10": SENTINEL if dev else 0.9, "generation": {"status": "ok",
           "faithfulness_pre": SENTINEL if dev else 0.8}, "abstention": {}}  # fmt: skip
    return {"backend": "claude_cli" if dev else "anthropic_api", "development_run": dev,
            "columns": {"aggregate": col, "xbrl_auto": col}}  # fmt: skip


def test_development_runs_are_ids_only_and_never_values(tmp_path):
    runs = tmp_path / "runs"
    runs.mkdir()
    _write(runs / "aaaaaaaaaaaa.meta.json", {"backend": "claude_cli"})
    _write(runs / "aaaaaaaaaaaa.json", _report(dev=True))
    _write(runs / "bbbbbbbbbbbb.filter.json", {"report": {"backend": "claude_cli",
           "columns": {"filtered": {"aggregate": {"sufficiency@10": SENTINEL}}}}})  # fmt: skip
    _write(runs / "cccccccccccc.smoke.json", {"ok": True, "meta": {"backend": "claude_cli"}})
    _write(
        runs / "ffffffffffff.retrieval.json",
        {
            "report": {
                "columns": {"hybrid": {s: {"sufficiency@10": 0.5} for s in metrics.SOURCES}},
                "retrieval": {},
            }
        },
    )
    payload = metrics.build(runs=runs)
    text = json.dumps(payload)
    assert str(SENTINEL) not in text
    assert [d["run_id"] for d in payload["development_runs"]] == [
        "aaaaaaaaaaaa", "bbbbbbbbbbbb", "cccccccccccc"]  # fmt: skip
    assert all(d["banner"] == metrics.BANNER for d in payload["development_runs"])
    assert payload["gate"]["run_id"] is None and not payload["gate"]["passed"]
    assert payload["gate"]["reason"] == "no eligible evaluation run"


def test_a_gated_run_feeds_the_gate_by_the_same_rule(tmp_path):
    runs = tmp_path / "runs"
    runs.mkdir()
    _write(runs / "dddddddddddd.meta.json", {"backend": "anthropic_api"})
    _write(runs / "dddddddddddd.json", _report(dev=False))
    _write(runs / "eeeeeeeeeeee.meta.json", {"backend": "claude_cli"})
    _write(runs / "eeeeeeeeeeee.json", _report(dev=True))
    payload = metrics.build(runs=runs)
    assert payload["gate"]["run_id"] == "dddddddddddd" and payload["gated_runs"] == ["dddddddddddd"]
    suff = next(r for r in payload["gate"]["rows"]
                if r["metric"] == "sufficiency_at_10" and r["scope"] == "aggregate")  # fmt: skip
    assert suff["value"] == 0.9 and str(SENTINEL) not in json.dumps(payload)


def cfg_pending():
    cfg = yaml.safe_load((REPO_ROOT / "eval" / "dashboard.yaml").read_text(encoding="utf-8"))
    return cfg["pending_even_with_a_gated_run"]


def test_readme_status_section_agrees_with_dashboard_configuration():
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    section = readme.split("### Where the gate stands", 1)[1].split("### What waits", 1)[0]
    flat = " ".join(section.split())
    for x in cfg_pending():
        if "F-134" in x["findings"]:
            continue
        line = f"{x['metrics']} ({x['reason']}, {', '.join(x['findings'])})"
        assert line in flat, line
    rows = re.findall(r"^\| (.+?) \| (F-[\d, F-]+) \|$", readme, re.M)
    cfg = yaml.safe_load((REPO_ROOT / "eval" / "dashboard.yaml").read_text(encoding="utf-8"))
    assert rows == [
        (o["item"], ", ".join(o["findings"]))
        for o in cfg["owner_blocked"]
        if "F-134" not in o["findings"]
    ]
    assert "(eval/dashboard.yaml)" in section


def test_readme_metrics_match_frozen_run() -> None:
    runs = REPO_ROOT / "eval" / "runs"
    run = "13fc0fa4eb72"
    report = json.loads((runs / f"{run}.json").read_text(encoding="utf-8"))
    judged = json.loads((runs / f"{run}.judged.json").read_text(encoding="utf-8"))
    meta = json.loads((runs / f"{run}.meta.json").read_text(encoding="utf-8"))
    assert report["run_id"] == judged["run_id"] == run
    assert report["backend"] == judged["backend"] == meta["backend"] == "claude_cli"
    assert report["served_models"] == judged["served_models"]
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    section = readme.split("## Metrics\n", 1)[1].split("## Reproduce\n", 1)[0]
    assert f"`{run}`" in section
    for model in meta["model_requested"].values():
        assert report["served_models"][model] > 0 and f"`{model}`" in section

    header, _, *rows = [
        line.strip("|").split("|") for line in section.splitlines() if line.startswith("|")
    ]
    sources = ("xbrl_auto", "llm_seeded", "handwritten", "aggregate")
    assert [cell.strip() for cell in header] == ["Metric", *sources, "RESULTS rows"]
    fields = {
        "Sufficiency@10": ("sufficiency@10",),
        "Faithfulness (pre)": ("generation", "faithfulness_pre"),
        "Claim retention": ("generation", "claim_retention"),
        "Citation coverage": ("generation", "citation_coverage"),
        "Answer correctness": ("answer_correctness", "normalized_mean"),
        "False-answer rate": ("abstention", "false_answer_rate"),
        "Over-abstention rate": ("abstention", "over_abstention_rate"),
        "XBRL contradiction rate": ("generation", "xbrl_contradiction_rate"),
    }
    assert [row[0].strip() for row in rows] == list(fields)
    for row in rows:
        metric, *cells, _ = (cell.strip() for cell in row)
        artifact = judged if metric == "Answer correctness" else report
        for source, cell in zip(sources, cells, strict=True):
            value = artifact["columns"][source]
            for key in fields[metric]:
                value = value[key]
            assert cell == ("N/A" if value is None else f"{value:.3f}"), (metric, source)


def test_historical_golden_run_is_classified_without_rewriting(tmp_path):
    from eval.golden_policy import GOLDEN_V1_SHA256

    runs = tmp_path / "runs"
    runs.mkdir()
    golden = {
        "backend": "claude_cli",
        "development_run": True,
        "datasets": {"/old/golden_v1.jsonl": GOLDEN_V1_SHA256},
    }
    _write(runs / "aaaaaaaaaaaa.meta.json", golden)
    _write(runs / "aaaaaaaaaaaa.json", golden)
    before = {p.name: p.read_bytes() for p in runs.iterdir()}
    dev, gated, retrieval = metrics.classify(runs)
    assert dev == {} and gated == ["aaaaaaaaaaaa"] and retrieval == []
    assert {p.name: p.read_bytes() for p in runs.iterdir()} == before


def test_dashboard_uses_validated_saved_judgments_without_rewriting(tmp_path, monkeypatch):
    from eval.golden_policy import GOLDEN_V1_SHA256
    from eval.judge import run
    from scripts import eval_run

    runs = tmp_path / "runs"
    runs.mkdir()
    rid = "aaaaaaaaaaaa"
    datasets = {"/fixture/golden_v1.jsonl": GOLDEN_V1_SHA256}
    item = {
        "item_id": "a",
        "source": "handwritten",
        "question_type": "table",
        "question": "Q?",
        "reference_answer": "yes",
    }
    result = {
        "item_id": "a",
        "answer": {"text": "yes", "abstained": False},
        "verdict": "PASS",
        "model_served": "generator",
    }
    meta = {
        "run_id": rid,
        "backend": "claude_cli",
        "datasets": datasets,
        "item_order": ["a"],
        "k": 10,
        "subset": {"items": 1, "sha256": "s"},
    }
    _write(runs / f"{rid}.meta.json", meta)
    _write(
        runs / f"{rid}.json",
        {**_report(False), **{k: v for k, v in meta.items() if k != "item_order"}},
    )
    (runs / f"{rid}.results.jsonl").write_text(json.dumps(result) + "\n")
    monkeypatch.setattr(
        run,
        "judge",
        lambda *args: {
            "item_id": "a",
            "score": 4,
            "rationale": "ok",
            "judge_backend": "fake",
            "judge_model": "judge",
            "judge_family": "judge",
            "generator_model": "generator",
            "same_family_as_generator": False,
        },
    )
    run.score_run(
        rid, {"a": item}, [result], runs / f"{rid}.judge.jsonl", {"backend": "fake"}, "small"
    )
    monkeypatch.setattr(eval_run, "load_datasets", lambda *args: ({"a": item}, datasets))
    monkeypatch.setattr(
        eval_run,
        "build_report",
        lambda *args: {
            **_report(False),
            "columns": {"aggregate": {"items": 1}, "handwritten": {"items": 1}},
        },
    )
    before = {p.name: p.read_bytes() for p in runs.iterdir()}

    payload = metrics.build(runs=runs, baseline_path=tmp_path / "missing.json")

    row = next(r for r in payload["gate"]["rows"] if r["metric"] == "answer_correctness")
    assert row["value"] == 0.8
    assert {p.name: p.read_bytes() for p in runs.iterdir()} == before


def test_dashboard_does_not_use_stale_correctness_when_sidecar_is_invalid(tmp_path, monkeypatch):
    from eval.golden_policy import GOLDEN_V1_SHA256
    from scripts import eval_run

    runs = tmp_path / "runs"
    runs.mkdir()
    rid = "bbbbbbbbbbbb"
    datasets = {"/fixture/golden_v1.jsonl": GOLDEN_V1_SHA256}
    item = {
        "item_id": "a",
        "source": "handwritten",
        "question_type": "table",
        "reference_answer": "yes",
    }
    result = {"item_id": "a", "answer": {"abstained": False}, "verdict": "PASS"}
    meta = {
        "run_id": rid,
        "backend": "claude_cli",
        "datasets": datasets,
        "item_order": ["a"],
        "k": 10,
        "subset": {"items": 1, "sha256": "s"},
    }
    _write(runs / f"{rid}.meta.json", meta)
    report = {**_report(False), **{k: v for k, v in meta.items() if k != "item_order"}}
    report["columns"]["aggregate"]["answer_correctness"] = {
        "complete": True,
        "normalized_mean": 1.0,
    }
    _write(runs / f"{rid}.json", report)
    (runs / f"{rid}.results.jsonl").write_text(json.dumps(result) + "\n")
    (runs / f"{rid}.judge.jsonl").write_text('{"item_id":"foreign","score":5}\n')
    monkeypatch.setattr(eval_run, "load_datasets", lambda *args: ({"a": item}, datasets))
    monkeypatch.setattr(eval_run, "build_report", lambda *args: report)

    payload = metrics.build(runs=runs, baseline_path=tmp_path / "missing.json")

    row = next(r for r in payload["gate"]["rows"] if r["metric"] == "answer_correctness")
    assert row["status"] == "pending" and row["value"] is None
