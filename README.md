# FilingQA

Ask a question about the 10-K and 10-Q filings of eight US companies and get an
answer broken into claims, each citing the filing chunk it came from, each
checked against that chunk and, for figures, against the filing's own XBRL data;
when the filings do not support an answer, it says so. The pipeline exists to be
measured: the evaluation harness, and the CI gate built on it, is the point.
Full specification in [`docs/PRD.md`](docs/PRD.md).

## Architecture

1. **Ingest** EDGAR filings and XBRL facts; inline-XBRL spans are captured before
   the HTML is flattened (`api/ingest/`, `api/parse/ixbrl.py`).
2. **Chunk** by document structure, tables whole, every chunk headed with its
   company, form, period and section (`api/chunk/`).
3. **Retrieve** with exact dense search plus BM25, fused by RRF
   (`api/query/retrieve.py`, `api/query/bm25.py`).
4. **Route**: a small model classifies intent and extracts companies and periods;
   periods are resolved to fiscal years in code, not by the model
   (`api/query/router.py`).
5. **Rerank** with a cross-encoder, a score floor and a timeout that falls back
   to the fused order (`api/query/rerank.py`).
6. **Generate** schema-enforced claims, each with citations and a figure object
   (`api/generate/claims.py`).
7. **Verify** numeric grounding against the cited chunk
   (`api/verify/grounding.py`), figures against the cited filing's XBRL fact
   (`api/verify/xbrl_check.py`), and prose with an LLM judging one cited chunk
   at a time (NLI remains configurable for comparison).
8. **Decide** PASS / PARTIAL / ABSTAIN from the checks (`api/verify/verdict.py`).
9. **Serve** the same function the eval runs (`api/pipeline.py`, `api/server.py`,
   `web/`).
10. **Measure** per source and gate it (`eval/runner.py`, `eval/compare.py`).

## What is hard here

What the build found, not what the PRD predicted:

- **Finding the right filing is not enough.** XBRL-templated questions often
  miss the evidence chunk because of ranking or retrieval budget (F-138).
  LLM-seeded questions reuse their source chunk's words, flattering keyword
  retrieval (F-110). The [retrieval ablation](docs/RESULTS.md#retrieval-ablation--373f11f1949c)
  separates the slices and reports the reviewed subset separately.
- **Natural phrasing exposed a verifier failure.** Of 30 answerable questions,
  19 ended in abstention. In [eight verifier abstentions](eval/runs/35b3efbbfd5d.natural_phrasing_diagnosis.json),
  seven already had a complete accepted evidence set in the generator input.
  Better retrieval alone would not address that pattern. In the [saved-answer re-verification](docs/RESULTS.md#2026-11-26--owner-decision-single-chunk-prose-support-fallback),
  natural-phrasing abstentions went from **19/30 to 11/30**. No retrieval,
  reranking, or generation was repeated, and the newly retained answers were
  not separately scored for correctness.
- **Reranking trades gains on one slice for losses on another.** In the
  [paired replay](eval/runs/paired-rerank-83be50a9dd79.json), BGE with the floor
  off beat no reranker on the model-drafted handwritten slice (39/60 vs 35/60)
  but lost on seeded questions (57/72 vs 67/72) and overall (208/332 vs 216/332).
  The replay did not test the served 0.30 floor; quality and latency still need
  a paired test on a quiet machine.
- **Fiscal-year conventions:** NVIDIA's year ending January 2026 is fiscal 2026,
  Target's is fiscal 2025; a model asked to pick the year picked wrong
  confidently, so periods are resolved from the filings' own dates (F-119).
- **Scale captions:** "in millions" does not cover per-share rows, and many
  tables state no scale at all (F-90).
- **Restatements versus rounding:** the facts feed drops XBRL precision, so a
  rounded figure and a real restatement look alike (F-47).

## Metrics

Gated metrics by source (PRD 11.2, thresholds in `eval/thresholds.yaml`). No
value appears here until a gated run exists; the figures in the status section
below are model-free retrieval measurements, not this table.

| Metric | xbrl_auto | llm_seeded | handwritten | aggregate |
|---|---|---|---|---|
| Sufficiency@10 | waiting on a gated run (F-59) | waiting on a gated run (F-59) | waiting on F-103 | waiting on a gated run (F-59) |
| Faithfulness (pre) | waiting on a gated run (F-59) | waiting on a gated run (F-59) | waiting on F-103 | waiting on a gated run (F-59) |
| Claim retention | waiting on a gated run (F-59) | waiting on a gated run (F-59) | waiting on F-103 | waiting on a gated run (F-59) |
| Citation coverage | waiting on a gated run (F-59) | waiting on a gated run (F-59) | waiting on F-103 | waiting on a gated run (F-59) |
| Answer correctness | waiting on a gated run (F-59) | waiting on a gated run (F-59) | waiting on F-103 | waiting on a gated run (F-59) |
| False-answer rate | waiting on a gated run (F-59) | waiting on a gated run (F-59) | waiting on F-103 | waiting on a gated run (F-59) |
| Over-abstention rate | waiting on a gated run (F-59) | waiting on a gated run (F-59) | waiting on F-103 | waiting on a gated run (F-59) |
| XBRL contradiction rate | waiting on a gated run (F-59) | waiting on a gated run (F-59) | waiting on F-103 | waiting on a gated run (F-59) |

## Reproduce

- `make eval`: every candidate item through the served pipeline, a per-source
  report and the run files in `eval/runs/`.
- `make eval-fast`: the committed 60-item subset, then the gate
  (`eval/compare.py`), which exits non-zero on any failed or pending metric.
- On the default `claude_cli` backend every run is a development run: never a
  baseline, never a result, never able to pass the gate. Gated runs use
  `anthropic_api`.

## Status

**Latest `golden_v1` development run: [13fc0fa4eb72](docs/RESULTS.md#golden-v1-final-development-run-13fc0fa4eb72).** It completed after the owner re-logged in; 142 rerank timeouts make it hardware-dependent and it cannot serve as a CI baseline. The earlier [35b3efbbfd5d](docs/RESULTS.md#golden-v1-development-run-35b3efbbfd5d) remains the before run.

Natural-phrasing abstentions fell from **19/30 to 9/30**, and aggregate over-abstention from **0.256 to 0.229** ([before](eval/runs/35b3efbbfd5d.json), [fresh run](eval/runs/13fc0fa4eb72.json)). These are different runs, not the saved-answer replay described above; the change is not a controlled causal estimate.

### Where the gate stands

- **No gated run exists.** The CI gate (`eval/compare.py` against
  `eval/thresholds.yaml`) does not pass with pending metrics. A gated run
  requires `anthropic_api`, `ANTHROPIC_API_KEY` in CI, and the hosted corpus
  snapshot (F-59, F-135).
- Candidate worksheet review is complete. The frozen `golden_v1` dataset has
  **392 items** (`eval/datasets/golden_v1_manifest.json`). The `handwritten`
  slice contains model-drafted items, so the freeze does not resolve the
  independent-authorship requirement (F-103).
- The separate `openai/gpt-6.2-sol` answer-correctness judge reached **Cohen's kappa of 0.818** against the
  owner labels (`eval/judge/verdicts_v1.jsonl`, `eval/judge/labels_v1.yaml`).
- The [single-chunk support judge](docs/RESULTS.md#2026-11-26--owner-decision-single-chunk-prose-support-fallback)
  is now the default because NLI's selected threshold was nearly open despite
  AUC 0.766 (`eval/nli/auc_v1.json`). The support judge reached **Cohen's kappa of
  0.908** on just 40 seeded-prose pairs, seven negative. A prior review naming
  the same model matches all recorded labels, so label independence is not
  established. This measures claim support, not answer correctness.
- BGE remains at a **0.30** score floor pending the quiet-machine test. The
  [floor sweep](eval/runs/4b5036b69ca0.f112.json) covered reviewed answerables
  but no handwritten answerables; recovery from floor-induced abstentions is
  not established (F-112). Timeout fallback uses hybrid ordering without the floor.

**Historical dashboard snapshot** (the dashboard configuration predates the
current status above): Config 3 retrieval run `7fa009acac95` reported aggregate
Sufficiency@10 0.537 (threshold 0.82), xbrl_auto 0.375 (0.90), and llm_seeded
0.928 (0.80). These are unreviewed candidate retrieval results, not gated scores.
The dashboard's historical pending list read:

- faithfulness, claim retention, citation coverage and the abstention rates (the NLI threshold needs 40 owner labels, F-125)
- answer correctness (judge labels, F-105)
- the natural-phrasing gap and every handwritten-slice threshold (hand-written items, F-103)
- cost per query (needs a priced run, F-134)

Those statements describe the older dashboard snapshot, not current blockers;
the newer review, judge validation and NLI results are recorded above.

**PASS is a faithfulness verdict, never a correctness claim.** The verifier
checks each claim against the evidence it cites (PRD 7.5); whether the answer
addresses the question is measured separately by numeric accuracy and the
validated judge. Reports print the two side by side (F-133).

### What waits on the owner

- `ANTHROPIC_API_KEY` for CI, the `anthropic_api` fast-eval baseline, the first priced run, and the deliberate-regression PR with its failing-check and PR-comment screenshot (F-59, F-134).
- Independently authored handwritten items and their provenance (unanswerable, adversarial, natural phrasing, comparison); the frozen model-drafted items do not meet this requirement (F-103).
- Hosting the corpus snapshot for CI (exact command in the finding) (F-135).
- Non-blocking owner review of the XBRL concept synonym map (F-127).
- Deploy: hosted snapshot, pgvector Postgres, Fly.io and Vercel accounts, `ANTHROPIC_API_KEY`, LangFuse keys, deployment, first live trace verification, and public URL (exact commands in the finding) (F-143).

**Historical dashboard owner-blocked snapshot** (not the current list above):

| Item | Finding |
|---|---|
| API key for CI runs, the fast-eval baseline, a priced run, the deliberate-regression PR and its screenshot | F-59, F-134 |
| Hand-written eval items (unanswerable, adversarial, natural phrasing, comparison) | F-103 |
| Human review of the candidates; the golden-set freeze; ablations run only on reviewed items | F-104, F-106 |
| Judge validation labels | F-105 |
| NLI gate labels (40 pairs, `eval/nli/label_sheet_v1.md`) | F-125 |
| Rerank score-floor calibration | F-112 |
| Hosting the corpus snapshot for CI (exact command in the finding) | F-135 |
| Review of the XBRL concept synonym map | F-127 |
| Deploy: Fly.io and Vercel accounts, LangFuse keys, the deploy itself and the public URL (exact commands in the finding) | F-143 |

Dense search is exact, so any run is reproducible from the corpus snapshot
(F-136). The reranker runs on whatever device is present; a run where it hit
its timeout is marked hardware-dependent, and a GPU CI runner is the owner's
cost decision (F-137). Everything decided so
far is in [`docs/TRADEOFFS.md`](docs/TRADEOFFS.md); every finding, open or
resolved, in [`docs/OPEN.md`](docs/OPEN.md); the build log in
[`docs/WORKLOG.md`](docs/WORKLOG.md).

## Known limitations

- Six 10-Ks are not in the index: JPMorgan Chase's three and Exxon Mobil's
  three. Their MD&A and financial statements sit in an appended annual-report
  section that the parser does not follow, so they were quarantined at the corpus
  freeze (F-66, F-70). Their 10-Qs are in the corpus; there are no 10-K
  questions for JPM or XOM. The Corpus screen lists the six filings.

## Deploy

What exists: Docker images for the API (`deploy/api.Dockerfile`, which refuses to
serve unless the database matches the corpus freeze) and the frontend
(`web/Dockerfile`), `deploy/compose.yaml` running both on Postgres restored from
the corpus snapshot, hosting manifests (`deploy/fly.toml` for the API,
`web/vercel.json` for the frontend), and LangFuse tracing that sends nothing
without keys. `make deploy-check` builds and runs both images locally against
the snapshot and checks `/health` and the Ask page. Every secret is an
environment variable.

What waits on the owner: hosting the snapshot, a Postgres, Fly.io and Vercel
accounts, `ANTHROPIC_API_KEY` and LangFuse keys, the deploy itself and the public
URL. The exact commands are in `docs/OPEN.md` F-143. There is no public URL yet.

## Local setup

Requires Postgres 18 with the `vector` extension available, and Python 3.11+.

```bash
python -m pip install -e ".[dev]"
cp .env.example .env      # set DATABASE_URL, and SEC_USER_AGENT to a real email
make migrate
```

`make migrate` applies everything in `infra/migrations/` in filename order and
records each file in `schema_migrations`, so re-running it is a no-op.

If you do not have a local Postgres, `make db-up` starts one in Docker
(`pgvector/pgvector:pg18`) matching the default DSN in `.env.example`.

## Development

```bash
make lint
make test
make eval        # full candidate set on the configured pipeline (verify_freeze first)
make eval-fast   # the committed 60-item subset, then the gate (eval/compare.py)
```

`make eval` on the default `claude_cli` backend produces development runs only;
they are never a baseline (`refuse_dev_baseline`) and never pass the gate.

## Documents

- [`docs/PRD.md`](docs/PRD.md) — the specification
- [`docs/TRADEOFFS.md`](docs/TRADEOFFS.md) — decisions taken, and deferred PRD
  defects logged against the phase where they have to be resolved
