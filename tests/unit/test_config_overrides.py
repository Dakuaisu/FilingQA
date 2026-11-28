import json
from contextlib import nullcontext
from types import SimpleNamespace

import pytest

from api import config, pipeline
from api.generate.generator import Answer
from scripts import eval_run


@pytest.fixture
def config_file(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text(
        "generation:\n  backend: claude_cli\n  tier_small: old-small\n"
        "  tier_large: old-large\nverification:\n  prose_check: llm_judge\n"
    )
    return path


def test_overrides_preserve_defaults_and_ignore_empty_values(config_file, monkeypatch):
    for name in (
        "FILINGQA_TIER_SMALL",
        "FILINGQA_TIER_LARGE",
        "FILINGQA_PROSE_CHECK",
        "FILINGQA_GENERATION_BACKEND",
    ):
        monkeypatch.setenv(name, "   ")
    assert config.generation(config_file)["tier_small"] == "old-small"
    assert config.generation(config_file)["tier_large"] == "old-large"
    assert config.verification(config_file)["prose_check"] == "llm_judge"


@pytest.mark.parametrize(
    "name,tier,other",
    [
        ("FILINGQA_TIER_SMALL", "tier_small", "tier_large"),
        ("FILINGQA_TIER_LARGE", "tier_large", "tier_small"),
    ],
)
def test_each_tier_override_is_independent(config_file, monkeypatch, name, tier, other):
    monkeypatch.delenv("FILINGQA_TIER_SMALL", raising=False)
    monkeypatch.delenv("FILINGQA_TIER_LARGE", raising=False)
    monkeypatch.setenv(name, "new-model")
    before = config_file.read_bytes()
    gen = config.generation(config_file)
    assert gen[tier] == "new-model"
    assert gen[other] == ("old-large" if other == "tier_large" else "old-small")
    assert config_file.read_bytes() == before


@pytest.mark.parametrize("prose", ["llm_judge", "nli"])
def test_effective_config_and_run_metadata_record_overrides(prose, monkeypatch):
    import api.db
    import api.query.rerank
    import api.query.retrieve

    monkeypatch.setenv("FILINGQA_TIER_SMALL", "  test-small  ")
    monkeypatch.setenv("FILINGQA_TIER_LARGE", "test-large")
    monkeypatch.setenv("FILINGQA_PROSE_CHECK", f" {prose} ")
    monkeypatch.setenv("FILINGQA_GENERATION_BACKEND", "anthropic_api")
    gen = config.generation()
    assert gen["tier_small"] == "test-small" and gen["tier_large"] == "test-large"
    assert config.verification()["prose_check"] == prose
    monkeypatch.setattr(api.db, "connect", lambda: nullcontext("db"))
    monkeypatch.setattr(
        api.query.retrieve, "load_bm25", lambda *args: (SimpleNamespace(key="fixture"), False)
    )
    monkeypatch.setattr(api.query.rerank, "machine", lambda: {})
    monkeypatch.setattr(api.query.rerank, "resolve_device", lambda *args: "test-device")
    cfg = config.eval_run()
    cfg["pipeline"] = "config_4_routed"
    meta = eval_run.current_meta(gen, cfg, {})
    assert meta["backend"] == "anthropic_api"
    assert meta["model_requested"] == {"tier_small": "test-small", "tier_large": "test-large"}
    assert meta["verification"]["prose_check"] == prose
    assert meta["router"]["tier"] == "tier_small"


def test_invalid_prose_override_is_rejected(config_file, monkeypatch):
    monkeypatch.setenv("FILINGQA_PROSE_CHECK", "not-a-check")
    with pytest.raises(config.ConfigError, match="prose_check"):
        config.verification(config_file)


def test_router_uses_effective_small_tier_without_a_model_call(monkeypatch):
    monkeypatch.setenv("FILINGQA_TIER_SMALL", "router-test-model")
    gen = config.generation()
    route = {
        "intent": "unsupported",
        "entities": [],
        "fiscal_periods": [],
        "form_types": [],
        "sub_queries": [],
        "confidence": 1.0,
    }
    seen = []

    def fake_call(prompt, question, cfg, tier):
        seen.append((tier, cfg[tier]))
        return Answer(json.dumps(route), cfg[tier], 0, 0, cfg["backend"])

    monkeypatch.setattr(pipeline, "call_model", fake_call)
    ctx = SimpleNamespace(rcfg={}, rrcfg={}, router=config.router(), companies={})
    result = pipeline.answer_question(None, ctx, "Q?", gen, {})
    assert seen == [("tier_small", "router-test-model")]
    assert result["router"]["model_served"] == "router-test-model"
