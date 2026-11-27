"""Run the existing eval CLI with an isolated RRF-weight override."""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import yaml

from api import pipeline
from scripts import eval_run


def load_weights(path: Path) -> dict[str, float]:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict) or set(document) != {"retrieval"}:
        raise ValueError("override must contain only retrieval.weights")
    retrieval = document["retrieval"]
    if not isinstance(retrieval, dict) or set(retrieval) != {"weights"}:
        raise ValueError("override must contain only retrieval.weights")
    weights = retrieval["weights"]
    if not isinstance(weights, dict) or set(weights) != {"dense", "sparse"}:
        raise ValueError("weights must contain exactly dense and sparse")
    if any(
        isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v <= 0
        for v in weights.values()
    ):
        raise ValueError("weights must be finite positive numbers")
    return {key: float(value) for key, value in weights.items()}


def run_with_override(path: Path) -> None:
    weights = load_weights(path)
    original_eval, original_pipeline = eval_run.retrieval, pipeline.retrieval

    def configured() -> dict:
        return {**original_eval(), "weights": dict(weights)}

    eval_run.retrieval = configured
    pipeline.retrieval = configured
    try:
        eval_run.main()
    finally:
        eval_run.retrieval = original_eval
        pipeline.retrieval = original_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config-override", required=True, type=Path)
    options, remaining = parser.parse_known_args()
    sys.argv = ["scripts.eval_run", *remaining]
    run_with_override(options.config_override)


if __name__ == "__main__":
    main()
