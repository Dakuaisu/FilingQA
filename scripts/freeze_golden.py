"""Freeze the reviewed golden dataset (PRD 11.1 Stage 6).

Run `python -m scripts.freeze_golden` for a dry run; add `--write` to freeze.
`--require-decision` additionally excludes generated items without a decision.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path

from api.config import REPO_ROOT
from eval.review_decisions import effective

CANDIDATES = REPO_ROOT / "eval" / "candidates"
HANDWRITTEN = REPO_ROOT / "eval" / "handwritten"
DECISIONS = REPO_ROOT / "eval" / "review" / "decisions_v1.jsonl"
DATASET = REPO_ROOT / "eval" / "datasets" / "golden_v1.jsonl"
MANIFEST = REPO_ROOT / "eval" / "datasets" / "golden_v1_manifest.json"
INPUTS = [
    *(
        CANDIDATES / f"{name}_candidates.jsonl"
        for name in ("xbrl_numeric", "comparison", "llm_seeded")
    ),
    *(
        HANDWRITTEN / f"{name}.jsonl"
        for name in ("comparison", "unanswerable", "adversarial", "natural_phrasing")
    ),
    DECISIONS,
]


def select_items(
    generated: list[dict], handwritten: list[dict], decisions: list[dict], require_decision: bool
) -> list[dict]:
    """Apply decisions to generated items, preserving the supplied handwritten set."""
    reviewed, _ = effective(generated, decisions)
    decided = {d["item_id"] for d in decisions}
    selected = [
        item
        for item in reviewed
        if (not require_decision or item["item_id"] in decided)
        and (item["source"] != "llm_seeded" or item["reviewed_by_human"])
    ]
    result = copy.deepcopy([*selected, *handwritten])
    for item in result:
        item["dataset_version"] = "golden_v1"
    return sorted(result, key=lambda item: item["item_id"])


def load_inputs(
    paths: list[Path],
) -> tuple[tuple[list[dict], list[dict], list[dict]], dict[str, str]]:
    """Read each file once, deriving both parsed records and hashes from those bytes.

    The final file is the review decision log; all prior files contain items.
    """
    generated, handwritten, decisions = [], [], []
    hashes = {}
    for index, path in enumerate(paths):
        raw = path.read_bytes()
        hashes[str(path)] = hashlib.sha256(raw).hexdigest()
        rows = [json.loads(line) for line in raw.splitlines() if line.strip()]
        if index == len(paths) - 1:
            decisions.extend(rows)
        else:
            for row in rows:
                (handwritten if row["source"] == "handwritten" else generated).append(row)
    return (generated, handwritten, decisions), hashes


def make_manifest(
    items: list[dict], hashes: dict[str, str], decision_count: int, require_decision: bool
) -> dict:
    rule = (
        "Latest review decisions applied; rejected generated items excluded; "
        "LLM-seeded items require human review; handwritten items always included; "
        + (
            "all generated items require a decision"
            if require_decision
            else "undecided XBRL-generated items included"
        )
    )
    return {
        "dataset_version": "golden_v1",
        "selection_rule": rule,
        "require_decision": require_decision,
        "input_sha256": dict(sorted(hashes.items())),
        "decision_record_count": decision_count,
        "item_count": len(items),
        "counts_by_source": dict(sorted(Counter(i["source"] for i in items).items())),
        "counts_by_type": dict(sorted(Counter(i["question_type"] for i in items).items())),
    }


def write_outputs(dataset: Path, manifest: Path, contents: tuple[bytes, bytes]) -> None:
    """Exclusively create both outputs; roll back only files this call created."""
    data_created = False
    manifest_created = False
    try:
        with dataset.open("xb") as data_file:
            data_created = True
            with manifest.open("xb") as manifest_file:
                manifest_created = True
                data_file.write(contents[0])
                manifest_file.write(contents[1])
    except OSError:
        if manifest_created:
            manifest.unlink()
        if data_created:
            dataset.unlink()
        raise


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the immutable dataset")
    parser.add_argument("--require-decision", action="store_true")
    args = parser.parse_args()
    (generated, handwritten, decisions), hashes = load_inputs(INPUTS)
    items = select_items(generated, handwritten, decisions, args.require_decision)
    manifest = make_manifest(items, hashes, len(decisions), args.require_decision)
    counts = Counter((item["source"], item["question_type"]) for item in items)
    print(f"{'source':16} {'question_type':20} {'count':>5}")
    for (source, kind), count in sorted(counts.items()):
        print(f"{source:16} {kind:20} {count:5}")
    print(f"{'total':37} {len(items):5}")
    if args.write:
        dataset_bytes = "".join(json.dumps(i, ensure_ascii=False) + "\n" for i in items).encode()
        manifest_bytes = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()
        DATASET.parent.mkdir(parents=True, exist_ok=True)
        write_outputs(DATASET, MANIFEST, (dataset_bytes, manifest_bytes))
        print(f"wrote {DATASET} and {MANIFEST}")
    else:
        print("dry run; pass --write to freeze")


if __name__ == "__main__":
    main()
