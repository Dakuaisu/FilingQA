"""Pure cache identity and claim transformation for support replay."""

from __future__ import annotations

import copy
import hashlib
import json


def cache_key(claim: str, chunk_id: str, text: str, model: str, version: str) -> str:
    """Bind a cached verdict to every input that can change its meaning."""
    payload = json.dumps([claim, chunk_id, text, model, version], ensure_ascii=False)
    return hashlib.sha256(payload.encode()).hexdigest()


def replay_claim(claim: dict, decisions: dict[str, dict]) -> dict:
    """Replace prose checks while preserving all original figure checks."""
    result = copy.deepcopy(claim)
    if result.get("figure"):
        return result
    by_chunk = [{"chunk_id": cid, **decisions[cid]} for cid in result["citations"]]
    result["checks"].update(
        prose_check="llm_judge",
        prose_by_chunk=by_chunk,
        citations_supporting=[d["chunk_id"] for d in by_chunk if d["supported"]],
    )
    return result
