"""Identify the frozen evaluation dataset independently of its local path."""

from pathlib import Path

from api.generate.generator import BACKENDS

GOLDEN_V1_SHA256 = "7d17972fa7e54c6f9cba64e26c5d7c27d021b58ac3a6ec355d1342a5ba4ec74a"


def is_golden(datasets: dict[str, str] | None) -> bool:
    if not datasets or len(datasets) != 1:
        return False
    name, digest = next(iter(datasets.items()))
    return Path(name).name == "golden_v1.jsonl" and digest == GOLDEN_V1_SHA256


def eligible_report(report: dict) -> bool:
    return is_golden(report.get("datasets")) and report.get("backend") in BACKENDS


def complete_golden_report(report: dict) -> bool:
    if not eligible_report(report):
        return False
    subset = report.get("subset")
    expected = subset.get("items") if subset else 392
    aggregate = (report.get("columns") or {}).get("aggregate") or {}
    return isinstance(expected, int) and expected > 0 and aggregate.get("items") == expected
