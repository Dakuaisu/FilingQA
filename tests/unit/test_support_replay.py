from api.verify.support_replay import cache_key, replay_claim


def test_cache_identity_changes_with_claim_chunk_id_text_or_model():
    base = cache_key("claim", "id", "text", "model", "version")
    assert (
        len(
            {
                base,
                cache_key("other", "id", "text", "model", "version"),
                cache_key("claim", "other", "text", "model", "version"),
                cache_key("claim", "id", "other", "model", "version"),
                cache_key("claim", "id", "text", "other", "version"),
                cache_key("claim", "id", "text", "model", "other"),
            }
        )
        == 6
    )


def test_replay_preserves_figure_checks_and_collects_only_supported_citations():
    claim = {
        "text": "claim",
        "figure": None,
        "citations": ["a", "b"],
        "checks": {"citation_valid": True, "entity_ok": True, "xbrl_contradiction": False},
    }
    decisions = {"a": {"supported": False}, "b": {"supported": True}}
    out = replay_claim(claim, decisions)
    assert out["checks"]["citations_supporting"] == ["b"]
    assert out["checks"]["prose_by_chunk"] == [
        {"chunk_id": "a", "supported": False},
        {"chunk_id": "b", "supported": True},
    ]
    assert "prose_check" not in claim["checks"]


def test_replay_keeps_figure_claim_unchanged():
    claim = {
        "text": "figure",
        "figure": {"value": 5},
        "citations": ["a"],
        "checks": {"numbers_grounded": True},
    }
    assert replay_claim(claim, {}) == claim
