"""Judge rubric, parsing, family stamp, label draw and Cohen's kappa (PRD 11.3).
Synthetic label pairs; no judge call."""

from __future__ import annotations

import pytest

from api.config import generation
from api.generate.generator import Answer
from eval.judge import judge as judge_mod
from eval.judge.agreement import cohens_kappa
from eval.judge.judge import JudgeParseError, family, parse
from eval.judge.rubrics import RUBRIC, render
from scripts.judge import active, draw, replacement


def test_kappa_on_synthetic_label_pairs():
    assert cohens_kappa([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 1.0
    # Two raters, two categories: po 0.7, pe 0.5 -> 0.4.
    a = [1] * 5 + [2] * 5
    b = [1, 1, 1, 1, 2, 2, 2, 2, 1, 1]
    assert cohens_kappa(a, b) == pytest.approx((0.7 - 0.5) / 0.5)
    # Systematic disagreement scores below zero.
    assert cohens_kappa([1, 2, 1, 2], [2, 1, 2, 1]) == pytest.approx(-1.0)
    assert cohens_kappa([], []) is None
    assert cohens_kappa([3, 3, 3], [3, 3, 3]) is None  # chance agreement 1: undefined
    with pytest.raises(ValueError):
        cohens_kappa([1], [1, 2])


def test_rubric_has_an_anchor_per_level_and_the_prompt_carries_it():
    assert sorted(RUBRIC) == [1, 2, 3, 4, 5]
    p = render("What was X?", None, "It was 7.")
    assert "Reference answer (null means the system should decline to answer):\nnull" in p
    assert all(RUBRIC[k] in p for k in RUBRIC) and '{"score": <1-5>' in p


def test_parse_is_strict():
    assert parse('{"score": 4, "rationale": "Rounded."}') == (4, "Rounded.")
    assert parse('```json\n{"score": 1, "rationale": "x"}\n```')[0] == 1
    for bad in ('Score: 4', '{"score": 6, "rationale": "x"}', '{"score": "4", "rationale": "x"}',
                '{"score": true, "rationale": "x"}', '{"score": 4}', '[4]'):  # fmt: skip
        with pytest.raises(JudgeParseError):
            parse(bad)


def test_every_verdict_is_stamped_with_backend_model_and_family(monkeypatch):
    reply = Answer('{"score": 5, "rationale": "Matches."}', "claude-sonnet-5-5", 1, 1, "claude_cli")
    monkeypatch.setattr(judge_mod, "complete", lambda p, c, t: reply)
    item = {"item_id": "x", "question": "q", "reference_answer": "r"}
    v = judge_mod.judge(item, "a", generation(), "tier_large", "claude-haiku-4-5-20251001")
    assert (v["score"], v["judge_backend"], v["judge_model"]) == (
        5,
        "claude_cli",
        "claude-sonnet-5-5",
    )
    assert v["judge_family"] == "claude" and v["same_family_as_generator"] is True
    assert family("gpt-5") == "gpt"


def test_label_draw_is_seeded_and_proportional_by_source():
    items = {f"x{i}": {"source": "xbrl_auto"} for i in range(200)}
    items |= {f"s{i}": {"source": "llm_seeded"} for i in range(83)}
    results = [{"item_id": i} for i in items]
    a = draw(results, items, 7, 50)
    assert a == draw(list(reversed(results)), items, 7, 50)
    assert sum(i.startswith("x") for i in a) == 35 and sum(i.startswith("s") for i in a) == 15
    assert a != draw(results, items, 8, 50)


def test_replacement_keeps_the_source_and_skips_drawn_and_rejected_items():
    sources = {"s1": "llm_seeded", "s2": "llm_seeded", "s3": "llm_seeded", "x1": "xbrl_auto"}
    items = {i: {"source": s} for i, s in sources.items()}
    results = [{"item_id": i} for i in items]
    for seed in range(20):
        assert replacement(results, items, {"s1"}, {"s2"}, "llm_seeded", seed) == "s3"
    assert replacement(results, items, set(), set(), "llm_seeded", 7) == replacement(
        results, items, set(), set(), "llm_seeded", 7
    )
    with pytest.raises(ValueError):
        replacement(results, items, {"s1", "s3"}, {"s2"}, "llm_seeded", 1)
    entries = [{"item_id": "a", "excluded": "reference wrong"}, {"item_id": "b"}]
    assert [e["item_id"] for e in active(entries)] == ["b"]


def test_opencode_events_give_text_and_tokens():
    from eval.judge.opencode_cli import OpencodeError, parse_events

    lines = [
        '{"type": "step_start", "part": {}}',
        '{"type": "text", "part": {"text": "{\\"score\\": 3, \\"rationale\\": \\"x\\"}"}}',
        '{"type": "step_finish", "part": {"tokens": {"input": 10, "output": 4}}}',
    ]
    assert parse_events(lines) == ('{"score": 3, "rationale": "x"}', 10, 4)
    with pytest.raises(OpencodeError):
        parse_events(['{"type": "step_start", "part": {}}'])
