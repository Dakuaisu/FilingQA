---
title: FilingQA API
sdk: docker
app_port: 7860
---

# FilingQA on Hugging Face Spaces

**Offline preparation only. Docker build and smoke, hosted deployment, and live
queries are unverified.** This Space serves the API; Vercel serves the web UI.

## Package from the repository root

Create a separate Docker SDK Space. In its repository root, place this file
as `README.md`, `deploy/hf/Dockerfile` as `Dockerfile`, and
`deploy/hf/Dockerfile.dockerignore` as `Dockerfile.dockerignore`. Copy
`pyproject.toml`, `api/`, `eval/`, `scripts/`, and `infra/` from the FilingQA
repository root, preserving their paths, and copy `deploy/hf/entrypoint.sh`
to that same relative path. Do not upload only the `deploy/hf` directory:
the image's `COPY` instructions require the root context. Use tracked source
files only; never upload local `.env` files, credentials, or corpus dumps.
The entrypoint downloads the hosted rebuild archive named by the committed
manifest, checks its size and SHA-256, and restores it into local Postgres.

## Owner setup

1. Use CPU hardware for the Space. Configure a provider-side spending limit
   before enabling generation, and monitor usage. For a public demo, restrict
   access or add rate limiting before exposing a billable key.
2. Add `ANTHROPIC_API_KEY` in the Space settings as a **secret**, not a
   variable, build argument, or file. Leave it unset for the keyless smoke.
3. In Vercel, set the project root to `web` and set the production `API_BASE`
   to the Space origin, for example `https://OWNER-SPACE.hf.space`, without an
   API suffix. Redeploy after changing it. Do not set the provider key in Vercel.

The demo uses CPU retrieval and reranking, Haiku 5.5 for both generation
tiers, and local NLI for prose. The published full-run measurements used a
different verifier; this deployment does not reproduce them. CPU timing also
can change rerank fallbacks. Do not report this configuration as benchmarked.

## Smoke checklist — pending owner restart

After the owner restarts Docker, build from the FilingQA repository root
using `deploy/hf/Dockerfile` and context `.`. Start the image without a key,
binding port 7860 locally. Then repeat the infrastructure checks on the Space.

- Confirm logs show snapshot size and digest verification, restore and freeze
  verification, and startup on port 7860. Check that a clean Space restart
  restores successfully again.
- Check `GET /api/v1/health`, `/api/v1/corpus/summary`, and `/api/v1/metrics`.
  Then send a valid `POST /api/v1/query` without a secret: expect HTTP 503
  stating `ANTHROPIC_API_KEY` is not configured, before loading query context.
- Only after configuring the spending limit and secret, run one owner-approved
  answerable query. Check citations open through `/api/v1/chunks/{chunk_id}`,
  then test one abstention and confirm CPU latency is acceptable.
- After Vercel is pointed at the Space, verify Ask, citation rendering,
  Corpus, and Metrics through the public frontend. Record the URLs and actual
  smoke outcomes before marking F-143 resolved.
