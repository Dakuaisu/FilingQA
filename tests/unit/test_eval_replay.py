import copy
import hashlib
import json
import sys
from contextlib import nullcontext
from types import SimpleNamespace

import pytest

from api.query.bm25 import corpus_key
from api.verify.gate import Gate
from api.verify.verdict import verdict
from scripts import eval_run


def claims():
    checks = {
        "citation_valid": True,
        "entity_ok": True,
        "xbrl_contradiction": True,
        "xbrl": {"status": "contradiction"},
        "period_ok": False,
        "unit_ok": True,
        "numbers_grounded": True,
        "period_stated": True,
        "citations_supporting": ["stale"],
    }
    return [
        {
            "claim_id": "a",
            "text": "In 2024 revenue was 10 million.",
            "citations": ["a"],
            "figure": {"value": 10, "unit": "millions"},
            "checks": copy.deepcopy(checks),
        },
        {
            "claim_id": "b",
            "text": "In 2024 revenue was 99 million.",
            "citations": ["a"],
            "figure": {"value": 99, "unit": "millions"},
            "checks": copy.deepcopy(checks),
        },
        {
            "claim_id": "c",
            "text": "Demand rose.",
            "citations": ["a"],
            "figure": None,
            "checks": {
                **checks,
                "xbrl_contradiction": False,
                "entail": 0.8,
                "entail_by_chunk": [{"chunk_id": "a", "entail": 0.8}],
                "citations_supporting": ["a"],
            },
        },
    ]


def test_xbrl_off_rechecks_grounding_without_xbrl_or_nli(monkeypatch):
    gate = Gate.__new__(Gate)
    monkeypatch.setattr(gate, "zero_span_chunks", lambda ids: set())
    monkeypatch.setattr(gate, "xbrl_check", lambda c: pytest.fail("XBRL called"))
    original = claims()
    saved = copy.deepcopy(original)
    after = gate.recheck(original, ["a"], {"a": "Revenue 10"}, xbrl_enabled=False)
    assert original == saved
    assert after[0]["checks"]["unit_ok"] == "unknown"
    assert after[0]["checks"]["citations_supporting"] == ["a"]
    assert after[0]["checks"]["xbrl"] == {"status": "not_checked", "period_ok": None}
    assert after[0]["checks"]["period_ok"] is None
    assert not after[1]["checks"]["numbers_grounded"]
    assert after[1]["checks"]["citations_supporting"] == []
    assert after[2]["checks"]["entail"] == 0.8
    assert after[2]["checks"]["citations_supporting"] == ["a"]
    assert verdict(after, 0.7)[0] == "PARTIAL"


@pytest.mark.parametrize("threshold,expected", [(0.5, "PASS"), (0.7, "PASS"), (0.85, "ABSTAIN")])
def test_rescore_uses_saved_entailment(threshold, expected):
    c = claims()[2]
    result = {"claims_pre": [c], "answer": {"abstained": False}}
    assert eval_run.rescore_results([result], threshold)[0]["verdict"] == expected


@pytest.mark.parametrize("mode", ["rescore", "reverify"])
def test_replay_refuses_incomplete_run(tmp_path, mode):
    (tmp_path / "r.meta.json").write_text(json.dumps({"item_order": ["a"], "k": 10}))
    fn = eval_run.rescore_run if mode == "rescore" else eval_run.reverify_run
    with pytest.raises(SystemExit, match="run r"):
        fn({}, {"runs_dir": str(tmp_path)}, "r", 0.7 if mode == "rescore" else "xbrl_off")
    assert not list(tmp_path.glob("*.rescore-*.json"))
    assert not list(tmp_path.glob("*.reverify-*.json"))


def test_reverify_output_provenance_and_corpus_guard(tmp_path, monkeypatch):
    import api.db
    import api.verify.gate

    rows = [("a", "Revenue 10")]
    freeze = tmp_path / "freeze.yaml"
    freeze.write_text("parser_version: p\nchunker_version: c\n")
    templates = tmp_path / "templates.yaml"
    templates.write_text("company_names: {}\n")
    meta = {
        "item_order": ["i"],
        "k": 10,
        "parser_version": "p",
        "chunker_version": "c",
        "bm25_index_key": corpus_key("c", rows),
        "verification": {"nli_threshold": 0.7},
        "backend": "claude_cli",
        "run_id": "r",
        "model_requested": "test",
        "retrieval_stage": "test",
    }
    result = {
        "item_id": "i",
        "generator_input": ["a"],
        "claims_pre": claims(),
        "answer": {"text": "original", "claims": [], "abstained": False},
        "verdict": "ABSTAIN",
        "retrieved": ["a"],
        "model_served": "test",
    }
    meta_path, results_path = tmp_path / "r.meta.json", tmp_path / "r.results.jsonl"
    meta_path.write_text(json.dumps(meta))
    results_path.write_text(json.dumps(result) + "\n")
    source = (meta_path.read_bytes(), results_path.read_bytes())

    class Conn:
        def execute(self, sql):
            return self

        def fetchall(self):
            return rows

    gate = Gate.__new__(Gate)
    monkeypatch.setattr(gate, "zero_span_chunks", lambda ids: set())
    monkeypatch.setattr(gate, "xbrl_check", lambda c: pytest.fail("XBRL called"))
    monkeypatch.setattr(api.db, "connect", lambda: nullcontext(Conn()))
    monkeypatch.setattr(api.verify.gate, "Gate", lambda *args: gate)
    monkeypatch.setattr(eval_run, "FREEZE_FILE", freeze)
    monkeypatch.setattr(eval_run, "TEMPLATES", templates)
    monkeypatch.setattr(eval_run, "texts_for", lambda conn, ids: dict(rows))
    items = {
        "i": {
            "item_id": "i",
            "source": "handwritten",
            "question_type": "synthesis",
            "tags": [],
            "reference_answer": "",
            "expected_abstain": False,
            "gold_evidence_sets": [],
        }
    }
    eval_run.reverify_run(items, {"runs_dir": str(tmp_path)}, "r", "xbrl_off")
    doc = json.loads((tmp_path / "r.reverify-xbrl_off.json").read_text())
    assert (meta_path.read_bytes(), results_path.read_bytes()) == source
    assert doc["report"]["source_run"] == "r"
    assert doc["items"][0]["verdict"] == "PARTIAL"
    assert doc["report"]["columns"]["aggregate"]["generation"]["xbrl_contradiction_rate"] is None
    rows[:] = [("a", "changed")]
    with pytest.raises(SystemExit, match="corpus text differ"):
        eval_run.reverify_run(items, {"runs_dir": str(tmp_path)}, "r", "xbrl_off")


@pytest.mark.parametrize("threshold", ["0.5", "0.7", "0.85"])
def test_rescore_cli_dispatches_threshold_without_device_probe(tmp_path, monkeypatch, threshold):
    path = tmp_path / "data.jsonl"
    path.write_text('{"item_id":"i"}\n')
    identity = {str(path): hashlib.sha256(path.read_bytes()).hexdigest()}
    (tmp_path / "r.meta.json").write_text(json.dumps({"datasets": identity}))
    monkeypatch.setattr(eval_run, "eval_run", lambda: {"runs_dir": str(tmp_path)})
    monkeypatch.setattr(
        eval_run,
        "current_meta",
        lambda *args, **kwargs: {} if kwargs.get("replay") else pytest.fail("runtime preflight"),
    )
    seen = []
    monkeypatch.setattr(eval_run, "rescore_run", lambda items, cfg, run_id, t: seen.append(t))
    monkeypatch.setattr(sys, "argv", ["eval_run", "--rescore", "r", threshold])
    eval_run.main()
    assert seen == [float(threshold)]


def test_replay_preflight_keeps_database_check_without_hardware_probe(monkeypatch):
    import api.db
    import api.query.rerank
    import api.query.retrieve

    calls = []
    monkeypatch.setattr(api.db, "connect", lambda: nullcontext("db"))
    monkeypatch.setattr(
        api.query.retrieve,
        "load_bm25",
        lambda conn, cfg: (calls.append(conn) or SimpleNamespace(key="corpus"), False),
    )
    monkeypatch.setattr(api.query.rerank, "machine", lambda: pytest.fail("machine probe"))
    monkeypatch.setattr(api.query.rerank, "resolve_device", lambda device: pytest.fail("GPU probe"))
    cfg = eval_run.eval_run()
    cfg["pipeline"] = "config_4_rerank"
    meta = eval_run.current_meta(eval_run.generation(), cfg, {}, replay=True)
    assert calls == ["db"]
    assert meta["bm25_index_key"] == "corpus"
    assert "machine" not in meta
    assert "device_used" not in meta["rerank"]


def test_reverify_cli_dispatches_variant(tmp_path, monkeypatch):
    path = tmp_path / "data.jsonl"
    path.write_text('{"item_id":"i"}\n')
    identity = {str(path): hashlib.sha256(path.read_bytes()).hexdigest()}
    (tmp_path / "r.meta.json").write_text(json.dumps({"datasets": identity}))
    monkeypatch.setattr(eval_run, "eval_run", lambda: {"runs_dir": str(tmp_path)})
    monkeypatch.setattr(
        eval_run,
        "current_meta",
        lambda *args, **kwargs: {} if kwargs.get("replay") else pytest.fail("runtime preflight"),
    )
    seen = []
    monkeypatch.setattr(
        eval_run, "reverify_run", lambda items, cfg, rid, tag: seen.append((rid, tag))
    )
    monkeypatch.setattr(sys, "argv", ["eval_run", "--reverify", "r", "xbrl_off"])
    eval_run.main()
    assert seen == [("r", "xbrl_off")]
