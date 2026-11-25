import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest

from eval.retrieval_ablation import rankings, summarize

ROOT = Path(__file__).resolve().parents[2]
DEPTHS = (20, 50, 100)
MODES = ("dense", "sparse", "hybrid_1_1", "hybrid_1.5_1", "hybrid_1_1.5")


@pytest.fixture
def packet(tmp_path):
    dataset = ROOT / "eval/datasets/golden_v1.jsonl"
    manifest = ROOT / "eval/datasets/golden_v1_manifest.json"
    items = [json.loads(line) for line in dataset.read_text().splitlines() if line]
    rows = []
    for item in items:
        if item["expected_abstain"]:
            continue
        ids = [f"dummy-{n}" for n in range(10)] + item["gold_evidence_sets"][0]
        branches = {depth: ids[:depth] for depth in DEPTHS}
        row = {
            key: item[key]
            for key in (
                "item_id",
                "question",
                "source",
                "question_type",
                "reviewed_by_human",
                "gold_evidence_sets",
            )
        }
        row["rankings"] = rankings(branches, branches, 60)
        rows.append(row)
    document = {
        "dataset_sha256": hashlib.sha256(dataset.read_bytes()).hexdigest(),
        "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest(),
        "input_sha256": {},
        "items": rows,
        "results_at_depth": summarize(rows, MODES, DEPTHS),
        "results_at_10": summarize(rows, MODES, DEPTHS, 10),
    }
    path = tmp_path / "packet.json"
    path.write_text(json.dumps(document))
    return path


def test_verifier_cli_displays_requested_depth(packet):
    result = subprocess.run(
        [sys.executable, "scripts/verify_retrieval_ablation.py", str(packet)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    line = next(
        line for line in result.stdout.splitlines() if line.startswith("all aggregate dense ")
    )
    assert "332/332:1.0" in line


def test_verifier_cli_rejects_tampered_depth_summary(packet):
    document = json.loads(packet.read_text())
    document["results_at_depth"]["all"]["aggregate"]["dense"]["20"]["sufficient"] = 0
    packet.write_text(json.dumps(document))
    result = subprocess.run(
        [sys.executable, "scripts/verify_retrieval_ablation.py", str(packet)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0


@pytest.mark.parametrize("field", ["source", "gold_evidence_sets", "reviewed_by_human"])
def test_verifier_cli_rejects_tampered_gold_labels(packet, field):
    document = json.loads(packet.read_text())
    document["items"][0][field] = None
    packet.write_text(json.dumps(document))
    result = subprocess.run(
        [sys.executable, "scripts/verify_retrieval_ablation.py", str(packet)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0


def test_sufficiency_requires_all_chunks_in_one_alternative():
    items = [
        {
            "source": "xbrl_auto",
            "reviewed_by_human": True,
            "gold_evidence_sets": [["a", "b"], ["c", "d"]],
            "rankings": {"dense": {2: ["a", "c"]}},
        }
    ]
    cell = summarize(items, ("dense",), (2,))["all"]["aggregate"]["dense"][2]
    assert (cell["sufficient"], cell["mean_recall"]) == (0, 0.5)


def test_sufficiency_accepts_any_complete_alternative():
    items = [
        {
            "source": "xbrl_auto",
            "reviewed_by_human": True,
            "gold_evidence_sets": [["a", "b"], ["c", "d"]],
            "rankings": {"dense": {2: ["c", "d"]}},
        }
    ]
    cell = summarize(items, ("dense",), (2,))["all"]["aggregate"]["dense"][2]
    assert (cell["sufficient"], cell["mean_recall"]) == (1, 1.0)


def test_hybrid_is_refused_from_each_depth_not_a_large_fusion_prefix():
    dense = ["a", "b", "c"]
    sparse = ["d", "e", "c"]
    result = rankings({2: dense[:2], 3: dense}, {2: sparse[:2], 3: sparse}, 60)
    assert "c" not in result["hybrid_1_1"][2]
    assert result["hybrid_1_1"][3][0] == "c"


def test_summaries_separate_reviewed_sources_and_missing_gold():
    items = [
        {
            "source": "xbrl_auto",
            "reviewed_by_human": True,
            "gold_evidence_sets": [["a", "b"]],
            "rankings": {"dense": {2: ["a", "b"]}},
        },
        {
            "source": "handwritten",
            "reviewed_by_human": False,
            "gold_evidence_sets": [],
            "rankings": {"dense": {2: ["a"]}},
        },
    ]
    result = summarize(items, ("dense",), (2,))
    assert result["all"]["aggregate"]["dense"][2] == {
        "population": 2,
        "scored": 1,
        "no_gold": 1,
        "sufficient": 1,
        "mean_recall": 1.0,
    }
    assert result["reviewed"]["handwritten"]["dense"][2]["population"] == 0
