import hashlib
import json
import sys

import pytest

from api import pipeline
from scripts import eval_run


def test_override_reaches_metadata_and_pipeline_without_changing_defaults(tmp_path, monkeypatch):
    from scripts.eval_rrf_override import run_with_override

    config = tmp_path / "override.yaml"
    config.write_text("retrieval:\n  weights:\n    dense: 1.5\n    sparse: 1.0\n")
    original = {"weights": {"dense": 1.0, "sparse": 1.0}, "k_dense": 50}
    monkeypatch.setattr(eval_run, "retrieval", lambda: original)
    monkeypatch.setattr(pipeline, "retrieval", lambda: original)
    seen = []
    monkeypatch.setattr(
        eval_run, "main", lambda: seen.append((eval_run.retrieval(), pipeline.retrieval()))
    )

    run_with_override(config)

    assert seen == [({"weights": {"dense": 1.5, "sparse": 1.0}, "k_dense": 50},) * 2]
    assert original["weights"] == {"dense": 1.0, "sparse": 1.0}
    assert eval_run.retrieval() == original and pipeline.retrieval() == original


def test_override_rejects_unrelated_configuration(tmp_path):
    from scripts.eval_rrf_override import load_weights

    config = tmp_path / "override.yaml"
    config.write_text("retrieval:\n  k_dense: 99\n")
    with pytest.raises(ValueError):
        load_weights(config)


def test_override_restores_config_after_failure(tmp_path, monkeypatch):
    from scripts.eval_rrf_override import run_with_override

    config = tmp_path / "override.yaml"
    config.write_text("retrieval:\n  weights:\n    dense: 1.5\n    sparse: 1.0\n")
    original = eval_run.retrieval
    monkeypatch.setattr(eval_run, "main", lambda: (_ for _ in ()).throw(RuntimeError("halt")))
    with pytest.raises(RuntimeError):
        run_with_override(config)
    assert eval_run.retrieval is original


def test_real_context_uses_override(tmp_path, monkeypatch):
    import api.index.embed
    from scripts.eval_rrf_override import run_with_override

    config = tmp_path / "override.yaml"
    config.write_text("retrieval:\n  weights:\n    dense: 1.5\n    sparse: 1.0\n")
    monkeypatch.setattr(eval_run, "retrieval", lambda: {"weights": {"dense": 1.0, "sparse": 1.0}})
    monkeypatch.setattr(api.index.embed, "load_model", lambda: (None, None))
    monkeypatch.setattr(pipeline, "rerank", lambda: {})
    monkeypatch.setattr(pipeline, "generation", lambda: {"structured": False})
    seen = []
    monkeypatch.setattr(
        eval_run, "main", lambda: seen.append(pipeline.Context(None, "config_1_dense").rcfg)
    )
    run_with_override(config)
    assert seen == [{"weights": {"dense": 1.5, "sparse": 1.0}}]


def test_resume_rejects_different_retrieval_weights(tmp_path, monkeypatch):
    from scripts.eval_rrf_override import run_with_override

    dataset = tmp_path / "items.jsonl"
    dataset.write_text('{"item_id":"item1"}\n')
    run_dir = tmp_path / "runs"
    run_dir.mkdir()
    metadata = {
        "datasets": {str(dataset): hashlib.sha256(dataset.read_bytes()).hexdigest()},
        "retrieval": {"weights": {"dense": 1.0, "sparse": 1.0}},
        "item_order": ["item1"],
    }
    (run_dir / "testid.meta.json").write_text(json.dumps(metadata))
    override = tmp_path / "override.yaml"
    override.write_text("retrieval:\n  weights:\n    dense: 1.5\n    sparse: 1.0\n")
    monkeypatch.setattr(sys, "argv", ["eval_run", "--resume", "testid", "--dataset", str(dataset)])
    monkeypatch.setattr(eval_run, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(eval_run, "generation", lambda: {"backend": "claude_cli"})
    monkeypatch.setattr(eval_run, "eval_run", lambda: {"runs_dir": "runs"})
    monkeypatch.setattr(eval_run, "retrieval", lambda: {"weights": {"dense": 1.0, "sparse": 1.0}})
    monkeypatch.setattr(
        eval_run, "current_meta", lambda *args, **kwargs: {"retrieval": eval_run.retrieval()}
    )

    with pytest.raises(SystemExit, match=r"retrieval.*changed"):
        run_with_override(override)
