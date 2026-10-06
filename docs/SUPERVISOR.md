# Supervisor rules: FilingQA

The project's own rules for the agent-bridge supervisor (`supervisor_rules` in
`bridge.toml`). They are the project parts of the old `tools/bridge.py` supervisor
prompts (`SYSTEM` lines 131–141, `AUTONOMOUS` lines 180–197), kept verbatim where they
still apply. agent-bridge supplies the generic rules: the principles, phase order,
autonomous decisions, OWNER-BLOCKED handling and the output format.

## The project

The builder is building FilingQA, a citation-grounded QA system over SEC filings.

Use Read, Grep and Glob on docs/PRD.md, docs/OPEN.md, docs/TRADEOFFS.md,
docs/WORKLOG.md and the source when the builder references something you need.
Don't read the whole PRD. When it's cheap, verify the builder's claims against
the repo: if it says a file changed or a finding was logged, look.

The phase plan is PRD section 14.

## Work that belongs to the owner

Some work belongs to the developer personally and must NEVER be done by the
builder: hand-written eval items (unanswerable, adversarial,
natural-phrasing), the human review pass, and the hand labels for the judge's
Cohen's kappa. Have the builder build the schema and tooling for these, log
each as "OWNER-BLOCKED" in docs/OPEN.md, and move on to the next unblocked
task. Never accept placeholder or model-written items in their place.

In docs/OPEN.md these are F-103 (hand-written items), F-104 (human review),
F-105 (judge validation labels) and F-125 (the NLI gate labels, the same kind of
owner labelling). The golden-set freeze (F-106) waits on them.

## Project completion

Only when every PRD section 14 phase has its exit criterion met, or is blocked
solely on OWNER-BLOCKED items, and you have checked this in the repo yourself
(tests pass, docs/OPEN.md and docs/WORKLOG.md agree).
