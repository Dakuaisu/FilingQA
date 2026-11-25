"""Judge calls through the `opencode` CLI, for judge models outside the Claude family
(PRD 11.3 asks for a judge of a different family than the generator; F-14).

The child runs with --pure in a fresh empty temp directory, so it loads no
project plugins and cannot read the repository's label files.
"""

from __future__ import annotations

import json
import subprocess
import tempfile

from api.generate.generator import Answer

TIMEOUT_S = 300


class OpencodeError(RuntimeError):
    """The CLI exited non-zero, timed out, or returned no text."""


def parse_events(lines: list[str]) -> tuple[str, int, int]:
    text, tokens = [], {}
    for line in lines:
        if not line.strip():
            continue
        event = json.loads(line)
        part = event.get("part", {})
        if event.get("type") == "text":
            text.append(part.get("text", ""))
        elif event.get("type") == "step_finish":
            tokens = part.get("tokens") or {}
        elif event.get("type") == "error":
            raise OpencodeError(f"opencode error event: {event}")
    if not "".join(text).strip():
        raise OpencodeError("opencode returned no text")
    return "".join(text), int(tokens.get("input", 0)), int(tokens.get("output", 0))


def run(prompt: str, model: str) -> Answer:
    with tempfile.TemporaryDirectory() as cwd:
        try:
            p = subprocess.run(
                ["opencode", "run", "--pure", "-m", model, "--format", "json", prompt],
                cwd=cwd, capture_output=True, text=True, timeout=TIMEOUT_S, check=False,
            )  # fmt: skip
        except subprocess.TimeoutExpired as e:
            raise OpencodeError(f"opencode timed out after {TIMEOUT_S}s") from e
    if p.returncode != 0:
        raise OpencodeError(f"opencode exit {p.returncode}: {p.stderr.strip()[-500:]}")
    text, tin, tout = parse_events(p.stdout.splitlines())
    return Answer(text, model.split("/", 1)[-1], tin, tout, "opencode_cli")
