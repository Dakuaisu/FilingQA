import pytest

from api.generate.generator import Answer
from api.verify import prose_judge
from api.verify.gate import Gate
from api.verify.verdict import supported, verdict
from eval.runner import _generation


@pytest.mark.parametrize(
    "text",
    [
        '{"supported": true, "rationale": "yes"}',
        '{"supports": 1, "rationale": "yes"}',
        '{"supports": "true", "rationale": "yes"}',
        '{"supports": true, "rationale": " "}',
        '{"supports": true, "rationale": 1}',
        '{"supports": true, "rationale": "yes", "extra": 1}',
        "not json",
    ],
)
def test_invalid_judge_response_is_recorded_as_unsupported(monkeypatch, text):
    monkeypatch.setattr(
        prose_judge.opencode_cli,
        "run",
        lambda prompt, model: Answer(text, "served-model", 2, 3, "opencode_cli"),
    )
    result = prose_judge.check_support("claim", "one chunk", "provider/model")
    assert result["supported"] is False
    assert result["error"]
    assert result["model_served"] == "served-model"


@pytest.mark.parametrize("value", [True, False])
def test_judge_response_accepts_supports_boolean(monkeypatch, value):
    text = '{"supports": ' + str(value).lower() + ', "rationale": "reason"}'
    monkeypatch.setattr(
        prose_judge.opencode_cli,
        "run",
        lambda prompt, model: Answer(text, "served-model", 2, 3, "opencode_cli"),
    )
    result = prose_judge.check_support("claim", "one chunk", "provider/model")
    assert result["supported"] is value
    assert result["rationale"] == "reason"
    assert result["error"] is None


def test_judge_decision_drives_verdict_and_metrics_without_threshold():
    claim = {
        "claim_id": "p",
        "figure": None,
        "citations": ["a"],
        "checks": {
            "citation_valid": True,
            "entity_ok": True,
            "xbrl_contradiction": False,
            "prose_check": "llm_judge",
            "citations_supporting": ["a"],
        },
    }
    assert supported(claim, None)
    assert verdict([claim], None)[0] == "PASS"
    metrics = _generation([{"claims_pre": [claim], "claims_post": [claim]}], None)
    assert metrics["faithfulness_pre"] == 1.0


def test_figure_only_judge_run_metrics_do_not_require_nli_threshold():
    claim = {
        "claim_id": "f",
        "figure": {"value": 1},
        "citations": ["a"],
        "checks": {
            "citation_valid": True,
            "entity_ok": True,
            "numbers_grounded": True,
            "unit_ok": True,
            "period_stated": True,
            "period_ok": True,
            "xbrl_contradiction": False,
            "citations_supporting": ["a"],
        },
    }
    metrics = _generation([{"claims_pre": [claim], "claims_post": [claim]}], None, "llm_judge")
    assert metrics["faithfulness_pre"] == 1.0


def test_gate_checks_each_available_citation_independently(monkeypatch):
    gate = Gate.__new__(Gate)
    gate.prose_check, gate.prose_judge_model, gate.nli = "llm_judge", "provider/model", None
    gate.names, gate.ticker_of = {}, {}
    gate.figure_checks = lambda claims, given, texts: [
        {"xbrl_contradiction": False} for _ in claims
    ]
    seen = []

    def fake(claim, chunk, model):
        seen.append(chunk)
        return {"supported": chunk == "support", "error": None}

    monkeypatch.setattr(prose_judge, "check_support", fake)
    claim = {"claim_id": "p", "text": "claim", "figure": None, "citations": ["a", "b"]}
    out = gate.verify("question", [claim], ["a", "b"], {"a": "no", "b": "support"}, None)
    assert seen == ["no", "support"]
    assert out["verify_verdict"] == "PASS"
    assert out["claims_pre"][0]["checks"]["citations_supporting"] == ["b"]
