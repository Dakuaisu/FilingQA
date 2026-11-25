import copy
import hashlib
import json

import pytest

from scripts import freeze_golden


def item(iid, source, kind, reviewed=False):
    return {
        "item_id": iid,
        "source": source,
        "question_type": kind,
        "reviewed_by_human": reviewed,
        "dataset_version": "candidate",
        "gold_evidence_sets": [["old:chunk"]],
        "gold_accessions": ["old"],
        "tags": ["unit_scale_unknown"],
    }


@pytest.fixture
def inputs():
    generated = [
        item("numeric", "xbrl_auto", "xbrl_numeric"),
        item("comparison", "xbrl_auto", "comparison"),
        item("edited", "xbrl_auto", "comparison"),
        item("rejected", "xbrl_auto", "xbrl_numeric"),
        item("seeded", "llm_seeded", "table"),
        item("seeded_reviewed", "llm_seeded", "synthesis"),
    ]
    handwritten = [
        item("hand", "handwritten", "adversarial", False),
        item("hand_reviewed", "handwritten", "comparison", True),
    ]
    decisions = [
        {
            "item_id": "edited",
            "decision": "edit_evidence",
            "reviewer": "A",
            "evidence_sets": [["new:chunk"]],
            "unit_scale": "millions",
        },
        {"item_id": "rejected", "decision": "reject", "reviewer": "A"},
        {"item_id": "seeded_reviewed", "decision": "accept", "reviewer": "A"},
        {"item_id": "hand", "decision": "reject", "reviewer": "A"},
    ]
    return generated, handwritten, decisions


@pytest.mark.parametrize(
    ("require_decision", "expected"),
    [
        (False, {"numeric", "comparison", "edited", "seeded_reviewed", "hand", "hand_reviewed"}),
        (True, {"edited", "seeded_reviewed", "hand", "hand_reviewed"}),
    ],
)
def test_selection_policies(inputs, require_decision, expected):
    generated, handwritten, decisions = inputs
    result = freeze_golden.select_items(generated, handwritten, decisions, require_decision)
    assert {it["item_id"] for it in result} == expected
    assert all(it["dataset_version"] == "golden_v1" for it in result)
    handwritten_flags = {
        it["item_id"]: it["reviewed_by_human"] for it in result if it["source"] == "handwritten"
    }
    assert handwritten_flags == {
        "hand": False,
        "hand_reviewed": True,
    }


def test_effective_edits_and_inputs_are_independent(inputs):
    original = copy.deepcopy(inputs)
    result = freeze_golden.select_items(*inputs, False)
    edited = next(it for it in result if it["item_id"] == "edited")
    assert edited["gold_evidence_sets"] == [["new:chunk"]]
    assert edited["gold_accessions"] == ["new"]
    assert edited["tags"] == ["unit_scale_millions"]
    assert edited["reviewed_by_human"] is True
    result[0]["tags"].append("changed")
    assert inputs == original


def test_latest_decision_wins(inputs):
    generated, handwritten, decisions = inputs
    decisions.append({"item_id": "rejected", "decision": "accept", "reviewer": "B"})
    result = freeze_golden.select_items(generated, handwritten, decisions, True)
    assert "rejected" in {it["item_id"] for it in result}


@pytest.mark.parametrize("existing", ["dataset", "manifest"])
def test_writer_refuses_either_existing_file_without_orphan(tmp_path, existing):
    dataset, manifest = tmp_path / "gold.jsonl", tmp_path / "manifest.json"
    existing_path = dataset if existing == "dataset" else manifest
    existing_path.write_text("keep", encoding="utf-8")
    with pytest.raises(FileExistsError):
        freeze_golden.write_outputs(dataset, manifest, (b"data", b"manifest"))
    assert existing_path.read_text(encoding="utf-8") == "keep"
    assert not (manifest if existing == "dataset" else dataset).exists()


def test_writer_creates_both_outputs(tmp_path):
    dataset, manifest = tmp_path / "gold.jsonl", tmp_path / "manifest.json"
    freeze_golden.write_outputs(dataset, manifest, (b"data", b"manifest"))
    assert (dataset.read_bytes(), manifest.read_bytes()) == (b"data", b"manifest")


def test_manifest_hashes_the_loaded_bytes_and_counts(tmp_path, inputs):
    generated, handwritten, decisions = inputs
    paths = [
        tmp_path / "generated.jsonl",
        tmp_path / "handwritten.jsonl",
        tmp_path / "decisions.jsonl",
    ]
    for path, data in zip(paths, (generated, handwritten, decisions), strict=True):
        path.write_text("".join(json.dumps(row) + "\n" for row in data), encoding="utf-8")
    loaded, hashes = freeze_golden.load_inputs(paths)
    selected = freeze_golden.select_items(*loaded, False)
    manifest = freeze_golden.make_manifest(selected, hashes, len(decisions), False)
    assert hashes == {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    assert manifest["decision_record_count"] == len(decisions)
    assert manifest["counts_by_source"] == {"handwritten": 2, "llm_seeded": 1, "xbrl_auto": 3}
    assert manifest["counts_by_type"] == {
        "adversarial": 1,
        "comparison": 3,
        "synthesis": 1,
        "xbrl_numeric": 1,
    }
    assert manifest["selection_rule"]


def test_missing_input_fails(tmp_path):
    with pytest.raises(FileNotFoundError):
        freeze_golden.load_inputs([tmp_path / "missing.jsonl"])
