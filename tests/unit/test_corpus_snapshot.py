"""Corpus snapshot (F-135): restore refuses an archive whose sha256 is not recorded."""

from __future__ import annotations

import hashlib
import subprocess
import sys

import pytest
import yaml

import scripts.corpus_snapshot as cs


def test_restore_refuses_a_different_archive(tmp_path, monkeypatch):
    archive = tmp_path / "corpus_snapshot.dump"
    archive.write_bytes(b"not the frozen corpus")
    freeze = tmp_path / "freeze.yaml"
    freeze.write_text(
        "parser_version: p\nchunker_version: c\nsnapshot:\n  sha256: " + "0" * 64 + "\n"
    )
    monkeypatch.setattr(cs, "FREEZE_FILE", freeze)
    ran = []
    monkeypatch.setattr(cs.subprocess, "run", lambda *a, **k: ran.append(a))
    assert cs.restore(archive) == 1 and ran == []
    assert cs.sha256(archive) == hashlib.sha256(b"not the frozen corpus").hexdigest()


def test_tools_run_through_pg_exec(monkeypatch):
    monkeypatch.setenv("PG_EXEC", "docker exec -i abc")
    monkeypatch.setenv("PG_DB", "scratch")
    assert cs.pg("pg_restore", "--data-only") == [
        "docker",
        "exec",
        "-i",
        "abc",
        "pg_restore",
        "-U",
        "filingqa",
        "-d",
        "scratch",
        "--data-only",
    ]


def test_alternate_dump_keeps_canonical_manifest_unchanged(tmp_path, monkeypatch):
    canonical = tmp_path / "canonical.yaml"
    canonical.write_text(
        "parser_version: parser\nchunker_version: chunker\nsnapshot:\n  sha256: old\n"
    )
    original = canonical.read_bytes()
    alternate = tmp_path / "alternate.yaml"
    archive = tmp_path / "alternate.dump"
    monkeypatch.setattr(cs, "FREEZE_FILE", canonical)

    def run(args, **kwargs):
        if "pg_dump" in args:
            kwargs["stdout"].write(b"dump bytes")
        return subprocess.CompletedProcess(args, 0, stdout="123456789\n")

    monkeypatch.setattr(cs.subprocess, "run", run)
    cs.dump(archive, alternate)

    record = yaml.safe_load(alternate.read_text())
    assert canonical.read_bytes() == original
    assert record["snapshot"]["sha256"] == hashlib.sha256(b"dump bytes").hexdigest()
    assert record["snapshot"]["parser_version"] == "parser"
    assert record["snapshot"]["source_system_identifier"] == "123456789"


def test_restore_refuses_bad_digest_from_alternate_before_commands(tmp_path, monkeypatch):
    archive = tmp_path / "bad.dump"
    archive.write_bytes(b"wrong")
    alternate = tmp_path / "alternate.yaml"
    alternate.write_text("snapshot:\n  sha256: " + "0" * 64 + "\n")
    monkeypatch.setattr(cs.subprocess, "run", lambda *a, **k: pytest.fail("must not write"))
    assert cs.restore(archive, alternate) == 1


def test_pguser_override_preserves_default(monkeypatch):
    monkeypatch.delenv("PGUSER", raising=False)
    assert cs.pg("psql")[-3:] == ["filingqa", "-d", "filingqa"]
    monkeypatch.setenv("PGUSER", "rebuilder")
    assert cs.pg("psql")[-3:] == ["rebuilder", "-d", "filingqa"]


def test_default_dump_updates_only_canonical_snapshot(tmp_path, monkeypatch):
    canonical = tmp_path / "canonical.yaml"
    canonical.write_text("parser_version: p\nchunker_version: c\nsnapshot:\n  sha256: old\n")
    archive = tmp_path / "archive.dump"
    monkeypatch.setattr(cs, "FREEZE_FILE", canonical)

    def run(args, **kwargs):
        kwargs["stdout"].write(b"canonical dump")
        return subprocess.CompletedProcess(args, 0)

    monkeypatch.setattr(cs.subprocess, "run", run)
    cs.dump(archive)
    record = yaml.safe_load(canonical.read_text())
    assert record["parser_version"] == "p"
    assert record["snapshot"]["sha256"] == hashlib.sha256(b"canonical dump").hexdigest()
    assert "source_system_identifier" not in record["snapshot"]


def test_cli_restore_uses_explicit_manifest_before_database_access(tmp_path):
    archive = tmp_path / "archive.dump"
    archive.write_bytes(b"bad")
    alternate = tmp_path / "alternate.yaml"
    alternate.write_text("snapshot:\n  sha256: " + "0" * 64 + "\n")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "scripts.corpus_snapshot",
            "restore",
            str(archive),
            "--manifest",
            str(alternate),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "refusing" in result.stderr
