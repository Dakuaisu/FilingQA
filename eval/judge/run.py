"""Scoring and aggregation of saved answers without changing the source run."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from eval.judge.judge import judge


def eligible(item: dict, result: dict) -> bool:
    return (
        item.get("reference_answer") is not None
        and not result["answer"].get("abstained", False)
        and result.get("verdict") != "ABSTAIN"
    )


def identity(run_id: str, item: dict, result: dict) -> str:
    raw = json.dumps([run_id, item, result], sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def validate_records(records: list[dict], expected: dict[str, str], run_id: str) -> set[str]:
    done = set()
    for row in records:
        iid = row.get("item_id")
        score = row.get("score")
        if (
            iid not in expected
            or iid in done
            or row.get("run_id") != run_id
            or row.get("input_sha256") != expected[iid]
            or not isinstance(row.get("judge_config_sha256"), str)
            or not row.get("judge_backend")
            or not row.get("judge_model")
            or not row.get("judge_family")
            or not row.get("generator_model")
            or not isinstance(row.get("same_family_as_generator"), bool)
            or isinstance(score, bool)
            or not isinstance(score, int)
            or not 1 <= score <= 5
        ):
            raise ValueError(f"invalid, duplicate, foreign or mismatched judge record: {iid!r}")
        done.add(iid)
    return done


def score_run(run_id: str, items: dict, results: list[dict], path: Path,
              backend: dict, tier: str) -> None:  # fmt: skip
    selected = [r for r in results if eligible(items[r["item_id"]], r)]
    expected = {r["item_id"]: identity(run_id, items[r["item_id"]], r)
                for r in selected}  # fmt: skip
    config_hash = hashlib.sha256(json.dumps([backend, tier], sort_keys=True).encode()).hexdigest()
    records = []
    repair_size = None
    add_newline = False
    if path.exists():
        raw = path.read_bytes()
        lines = raw.splitlines(keepends=True)
        if lines and not lines[-1].endswith(b"\n"):
            try:
                json.loads(lines[-1])
            except json.JSONDecodeError:
                repair_size = len(raw) - len(lines.pop())
            else:
                add_newline = True
        records = [json.loads(line) for line in lines if line.strip()]
    done = validate_records(records, expected, run_id)
    if any(r.get("judge_config_sha256") != config_hash for r in records):
        raise ValueError("judge configuration changed since scoring began")
    if repair_size is not None:
        with path.open("r+b") as fh:
            fh.truncate(repair_size)
    elif add_newline:
        with path.open("ab") as fh:
            fh.write(b"\n")
    from scripts.eval_run import append

    for result in selected:
        iid = result["item_id"]
        if iid not in done:
            verdict = judge(
                items[iid], result["answer"]["text"], backend, tier, result["model_served"]
            )
            record = {
                **verdict,
                "run_id": run_id,
                "input_sha256": expected[iid],
                "judge_config_sha256": config_hash,
                "judge_tier": tier,
            }
            validate_records([record], {iid: expected[iid]}, run_id)
            append(path, record)


def aggregate(items: dict, results: list[dict], records: list[dict]) -> dict:
    scores = {r["item_id"]: r["score"] for r in records}

    def summarize(rows: list[dict]) -> dict:
        selected = [r for r in rows if eligible(items[r["item_id"]], r)]
        values = [scores[r["item_id"]] for r in selected if r["item_id"] in scores]
        complete = bool(selected) and len(values) == len(selected)
        return {
            "eligible": len(selected),
            "judged": len(values),
            "complete": complete,
            "mean_score": sum(values) / len(values) if values else None,
            "normalized_mean": sum(values) / (5 * len(values)) if complete else None,
            "share_at_least_4": sum(v >= 4 for v in values) / len(values) if values else None,
        }

    return {
        "scale": "mean score / 5",
        "aggregate": summarize(results),
        "by_source": {
            s: summarize([r for r in results if items[r["item_id"]]["source"] == s])
            for s in sorted({items[r["item_id"]]["source"] for r in results})
        },
        "by_type": {
            t: summarize([r for r in results if items[r["item_id"]]["question_type"] == t])
            for t in sorted({items[r["item_id"]]["question_type"] for r in results})
        },
    }
