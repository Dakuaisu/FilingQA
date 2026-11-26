"""Resume a support-only replay of the frozen golden-v1 development run."""

from __future__ import annotations

import fcntl
import hashlib
import json
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from api.config import REPO_ROOT, verification
from api.db import connect
from api.query.bm25 import corpus_key
from api.verify.prose_judge import check_support
from api.verify.support_replay import cache_key, replay_claim
from api.verify.verdict import item_verdict, verdict
from eval.runner import build_report
from scripts.eval_run import finished_results, read_jsonl, verdict_summary

RUN = "35b3efbbfd5d"
ROOT = REPO_ROOT
RUNS = ROOT / "eval/runs"
META = RUNS / f"{RUN}.meta.json"
SOURCE = RUNS / f"{RUN}.results.jsonl"
DATASET = ROOT / "eval/datasets/golden_v1.jsonl"
OUTPUT = RUNS / f"{RUN}.reverify-support_judge_v1.json"
CACHE = ROOT / "build/support_replay_v1.sqlite3"
LOCK = ROOT / "build/support_replay_v1.lock"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    with LOCK.open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        run()


def run() -> None:
    if OUTPUT.exists():
        raise SystemExit(f"refusing to overwrite {OUTPUT}")
    pins = {str(p.relative_to(ROOT)): digest(p) for p in (META, SOURCE, DATASET)}
    saved = json.loads(META.read_text(encoding="utf-8"))
    if digest(DATASET) not in saved["datasets"].values():
        raise SystemExit("dataset does not match the historical run")
    before = finished_results(RUNS, RUN, saved)
    items = {row["item_id"]: row for row in read_jsonl(DATASET)}
    model = verification()["prose_judge_model"]
    judge_version = digest(ROOT / "api/verify/prose_judge.py")
    with connect() as conn:
        rows = conn.execute("SELECT chunk_id, text FROM chunks ORDER BY chunk_id").fetchall()
    if corpus_key(saved["chunker_version"], rows) != saved["bm25_index_key"]:
        raise SystemExit("live chunk corpus does not match historical run")
    texts = dict(rows)
    jobs = {}
    for result in before:
        given = set(result.get("generator_input") or [])
        for claim in result.get("claims_pre") or []:
            if claim.get("figure"):
                continue
            for cid in claim["citations"]:
                if cid in given:
                    if cid not in texts:
                        raise SystemExit(f"missing historical chunk {cid}")
                    key = cache_key(claim["text"], cid, texts[cid], model, judge_version)
                    jobs[key] = (claim["text"], texts[cid])
    with sqlite3.connect(CACHE) as db:
        db.execute(
            "CREATE TABLE IF NOT EXISTS decisions (key TEXT PRIMARY KEY, value TEXT NOT NULL)"
        )
        cached = {
            key: json.loads(value) for key, value in db.execute("SELECT key, value FROM decisions")
        }
        pending = [(key, pair) for key, pair in jobs.items() if key not in cached]
        print(
            f"support pairs: {len(jobs)}, cached: {len(jobs) - len(pending)}, "
            f"pending: {len(pending)}",
            flush=True,
        )
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = {
                pool.submit(check_support, claim, text, model): key
                for key, (claim, text) in pending
            }
            for count, future in enumerate(as_completed(futures), 1):
                key = futures[future]
                decision = future.result()
                db.execute("INSERT INTO decisions VALUES (?, ?)", (key, json.dumps(decision)))
                db.commit()
                cached[key] = decision
                print(
                    f"[{count}/{len(pending)}] {'error' if decision['error'] else 'ok'}", flush=True
                )
    after = []
    for result in before:
        claims = result.get("claims_pre") or []
        if not claims:
            after.append(result)
            continue
        given = set(result.get("generator_input") or [])
        pre = []
        for claim in claims:
            decisions = {}
            if not claim.get("figure"):
                for cid in claim["citations"]:
                    if cid in given:
                        key = cache_key(claim["text"], cid, texts[cid], model, judge_version)
                        decisions[cid] = cached[key]
                    else:
                        decisions[cid] = {
                            "supported": False,
                            "error": "citation not available",
                            "model_requested": model,
                            "model_served": None,
                            "backend": "opencode_cli",
                        }
            pre.append(replay_claim(claim, decisions))
        gate_verdict, post = verdict(pre, None)
        item, reason = item_verdict(bool(result["answer"].get("abstained")), gate_verdict, pre)
        updated = {
            **result,
            "claims_pre": pre,
            "claims_post": post,
            "gate_verdict": gate_verdict,
            "verdict": item,
        }
        updated.pop("abstain_reason", None)
        if reason:
            updated["abstain_reason"] = reason
        after.append(updated)
    meta = {
        **saved,
        "source_run": RUN,
        "derived": "support-only replay; stored figure checks",
        "verification": {
            "prose_check": "llm_judge",
            "prose_judge_model": model,
            "judge_sha256": judge_version,
        },
    }
    report = build_report(items, after, meta, saved["k"], None)
    natural = [
        r["item_id"] for r in before if items[r["item_id"]]["question_type"] == "natural_phrasing"
    ]
    old = {r["item_id"]: r for r in before}
    new = {r["item_id"]: r for r in after}
    summary = {
        "before": verdict_summary(items, before),
        "after": verdict_summary(items, after),
        "natural_phrasing": {
            "items": len(natural),
            "abstained_before": sum(old[i]["verdict"] == "ABSTAIN" for i in natural),
            "abstained_after": sum(new[i]["verdict"] == "ABSTAIN" for i in natural),
        },
        "support_calls": len(jobs),
        "errors": sum(bool(cached[k]["error"]) for k in jobs),
    }
    if any(digest(ROOT / p) != h for p, h in pins.items()):
        raise SystemExit("historical inputs changed during replay")
    doc = {
        "kind": "derived support-only replay",
        "source_sha256": pins,
        "summary": summary,
        "report": report,
        "items": [
            {
                "item_id": r["item_id"],
                "verdict": r["verdict"],
                "abstain_reason": r.get("abstain_reason"),
                "claims_pre": r.get("claims_pre"),
                "claims_post": r.get("claims_post"),
            }
            for r in after
        ],
    }
    with OUTPUT.open("x", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
