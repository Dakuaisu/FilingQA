# Results register

Every number this project reports has a row here: id, what was measured, the
value, its kind (`development` or `real`, as the PRD defines them), the run id
or artifact it was read from, and the commit that added that artifact. No
`real` row exists: no `anthropic_api` run over a frozen, reviewed dataset has
been made (F-59 key, F-104 human review, F-106 golden-set freeze), so every row
below is `development`, including the model-free retrieval runs (DEC-002). Every
number reported from now on gets a row here. Thresholds are not restated; they
live in `eval/thresholds.yaml` only.

Values are copied from the committed run files, never recomputed: a number as
the file stores it; a string the file stores (for example a `pending` reason)
verbatim in backticks; `null` where the field is null; `absent` where the report
has no such field. Gated metrics are those in `eval/thresholds.yaml`, read from
the fields `eval/compare.py` reads. A `generation` section that carries only a
`status` gives that status for each of its metrics, as `eval/compare.py` does.

## Model-free retrieval runs (published by README, `eval/dashboard.yaml`, `/metrics`)

### 7fa009acac95 (README and dashboard current run)

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-001 | hybrid Sufficiency@10, xbrl_auto (`report.columns.hybrid.xbrl_auto.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | 0.375 | development | `eval/runs/7fa009acac95.retrieval.json` | `20f790c` |
| R-002 | hybrid Sufficiency@10, llm_seeded (`report.columns.hybrid.llm_seeded.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated; inflated by lexical overlap, F-110) | 0.927710843373494 | development | `eval/runs/7fa009acac95.retrieval.json` | `20f790c` |
| R-003 | hybrid Sufficiency@10, handwritten (`report.columns.hybrid.handwritten.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/7fa009acac95.retrieval.json` | `20f790c` |
| R-004 | hybrid Sufficiency@10, aggregate (`report.columns.hybrid.aggregate.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | 0.5371024734982333 | development | `eval/runs/7fa009acac95.retrieval.json` | `20f790c` |

### 5b3c3ac13e5e

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-005 | hybrid Sufficiency@10, xbrl_auto (`report.columns.hybrid.xbrl_auto.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | 0.375 | development | `eval/runs/5b3c3ac13e5e.retrieval.json` | `f9bf140` |
| R-006 | hybrid Sufficiency@10, llm_seeded (`report.columns.hybrid.llm_seeded.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated; inflated by lexical overlap, F-110) | 0.927710843373494 | development | `eval/runs/5b3c3ac13e5e.retrieval.json` | `f9bf140` |
| R-007 | hybrid Sufficiency@10, handwritten (`report.columns.hybrid.handwritten.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/5b3c3ac13e5e.retrieval.json` | `f9bf140` |
| R-008 | hybrid Sufficiency@10, aggregate (`report.columns.hybrid.aggregate.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | 0.5371024734982333 | development | `eval/runs/5b3c3ac13e5e.retrieval.json` | `f9bf140` |

### 188304ccaf94

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-009 | hybrid Sufficiency@10, xbrl_auto (`report.columns.hybrid.xbrl_auto.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | 0.215 | development | `eval/runs/188304ccaf94.retrieval.json` | `f7c4c98` |
| R-010 | hybrid Sufficiency@10, llm_seeded (`report.columns.hybrid.llm_seeded.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated; inflated by lexical overlap, F-110) | 0.6867469879518072 | development | `eval/runs/188304ccaf94.retrieval.json` | `f7c4c98` |
| R-011 | hybrid Sufficiency@10, handwritten (`report.columns.hybrid.handwritten.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/188304ccaf94.retrieval.json` | `f7c4c98` |
| R-012 | hybrid Sufficiency@10, aggregate (`report.columns.hybrid.aggregate.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | 0.35335689045936397 | development | `eval/runs/188304ccaf94.retrieval.json` | `f7c4c98` |

### 01019ff395ec

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-013 | hybrid Sufficiency@10, xbrl_auto (`report.columns.hybrid.xbrl_auto.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | 0.365 | development | `eval/runs/01019ff395ec.retrieval.json` | `9ad0d74` |
| R-014 | hybrid Sufficiency@10, llm_seeded (`report.columns.hybrid.llm_seeded.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated; inflated by lexical overlap, F-110) | 0.891566265060241 | development | `eval/runs/01019ff395ec.retrieval.json` | `9ad0d74` |
| R-015 | hybrid Sufficiency@10, handwritten (`report.columns.hybrid.handwritten.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/01019ff395ec.retrieval.json` | `9ad0d74` |
| R-016 | hybrid Sufficiency@10, aggregate (`report.columns.hybrid.aggregate.sufficiency@10`; Config 3; model-free, unreviewed candidates, not gated) | 0.519434628975265 | development | `eval/runs/01019ff395ec.retrieval.json` | `9ad0d74` |

## Eval runs (all `claude_cli` development runs; gated metrics as each report states them)

### 19693d4aa874

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-017 | sufficiency_at_10, xbrl_auto (`columns.xbrl_auto.sufficiency@10`) | 0.285 | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-018 | sufficiency_at_10, llm_seeded (`columns.llm_seeded.sufficiency@10`) | 0.6746987951807228 | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-019 | sufficiency_at_10, handwritten (`columns.handwritten.sufficiency@10`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-020 | sufficiency_at_10, aggregate (`columns.aggregate.sufficiency@10`) | 0.3992932862190813 | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-021 | faithfulness_pre, xbrl_auto (`columns.xbrl_auto.generation.faithfulness_pre`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-022 | faithfulness_pre, llm_seeded (`columns.llm_seeded.generation.faithfulness_pre`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-023 | faithfulness_pre, handwritten (`columns.handwritten.generation.faithfulness_pre`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-024 | faithfulness_pre, aggregate (`columns.aggregate.generation.faithfulness_pre`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-025 | claim_retention, xbrl_auto (`columns.xbrl_auto.generation.claim_retention`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-026 | claim_retention, llm_seeded (`columns.llm_seeded.generation.claim_retention`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-027 | claim_retention, handwritten (`columns.handwritten.generation.claim_retention`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-028 | claim_retention, aggregate (`columns.aggregate.generation.claim_retention`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-029 | citation_coverage, xbrl_auto (`columns.xbrl_auto.generation.citation_coverage`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-030 | citation_coverage, llm_seeded (`columns.llm_seeded.generation.citation_coverage`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-031 | citation_coverage, handwritten (`columns.handwritten.generation.citation_coverage`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-032 | citation_coverage, aggregate (`columns.aggregate.generation.citation_coverage`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-033 | xbrl_contradiction, xbrl_auto (`columns.xbrl_auto.generation.xbrl_contradiction_rate`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-034 | xbrl_contradiction, llm_seeded (`columns.llm_seeded.generation.xbrl_contradiction_rate`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-035 | xbrl_contradiction, handwritten (`columns.handwritten.generation.xbrl_contradiction_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-036 | xbrl_contradiction, aggregate (`columns.aggregate.generation.xbrl_contradiction_rate`) | absent: the report has no `generation` section | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-037 | false_answer_rate, xbrl_auto (`columns.xbrl_auto.abstention.false_answer_rate`) | null | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-038 | false_answer_rate, llm_seeded (`columns.llm_seeded.abstention.false_answer_rate`) | null | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-039 | false_answer_rate, handwritten (`columns.handwritten.abstention.false_answer_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-040 | false_answer_rate, aggregate (`columns.aggregate.abstention.false_answer_rate`) | null | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-041 | over_abstention_rate, xbrl_auto (`columns.xbrl_auto.abstention.over_abstention_rate`) | 0.0 | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-042 | over_abstention_rate, llm_seeded (`columns.llm_seeded.abstention.over_abstention_rate`) | 0.0 | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-043 | over_abstention_rate, handwritten (`columns.handwritten.abstention.over_abstention_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-044 | over_abstention_rate, aggregate (`columns.aggregate.abstention.over_abstention_rate`) | 0.0 | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-045 | cost_per_query, xbrl_auto (`columns.xbrl_auto.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-046 | cost_per_query, llm_seeded (`columns.llm_seeded.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-047 | cost_per_query, handwritten (`columns.handwritten.cost_per_query`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-048 | cost_per_query, aggregate (`columns.aggregate.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-049 | answer_correctness, xbrl_auto (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-050 | answer_correctness, llm_seeded (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-051 | answer_correctness, handwritten (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-052 | answer_correctness, aggregate (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |
| R-053 | natural_phrasing_gap, aggregate (not a report field) | absent: no report carries it; needs hand-written natural-phrasing items (F-103) | development | `eval/runs/19693d4aa874.json` | `e3dee34` |

### f2e616e0a7d7

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-054 | sufficiency_at_10, xbrl_auto (`columns.xbrl_auto.sufficiency@10`) | 0.285 | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-055 | sufficiency_at_10, llm_seeded (`columns.llm_seeded.sufficiency@10`) | 0.6746987951807228 | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-056 | sufficiency_at_10, handwritten (`columns.handwritten.sufficiency@10`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-057 | sufficiency_at_10, aggregate (`columns.aggregate.sufficiency@10`) | 0.3992932862190813 | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-058 | faithfulness_pre, xbrl_auto (`columns.xbrl_auto.generation.faithfulness_pre`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-059 | faithfulness_pre, llm_seeded (`columns.llm_seeded.generation.faithfulness_pre`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-060 | faithfulness_pre, handwritten (`columns.handwritten.generation.faithfulness_pre`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-061 | faithfulness_pre, aggregate (`columns.aggregate.generation.faithfulness_pre`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-062 | claim_retention, xbrl_auto (`columns.xbrl_auto.generation.claim_retention`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-063 | claim_retention, llm_seeded (`columns.llm_seeded.generation.claim_retention`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-064 | claim_retention, handwritten (`columns.handwritten.generation.claim_retention`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-065 | claim_retention, aggregate (`columns.aggregate.generation.claim_retention`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-066 | citation_coverage, xbrl_auto (`columns.xbrl_auto.generation.citation_coverage`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-067 | citation_coverage, llm_seeded (`columns.llm_seeded.generation.citation_coverage`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-068 | citation_coverage, handwritten (`columns.handwritten.generation.citation_coverage`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-069 | citation_coverage, aggregate (`columns.aggregate.generation.citation_coverage`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-070 | xbrl_contradiction, xbrl_auto (`columns.xbrl_auto.generation.xbrl_contradiction_rate`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-071 | xbrl_contradiction, llm_seeded (`columns.llm_seeded.generation.xbrl_contradiction_rate`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-072 | xbrl_contradiction, handwritten (`columns.handwritten.generation.xbrl_contradiction_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-073 | xbrl_contradiction, aggregate (`columns.aggregate.generation.xbrl_contradiction_rate`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-074 | false_answer_rate, xbrl_auto (`columns.xbrl_auto.abstention.false_answer_rate`) | null | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-075 | false_answer_rate, llm_seeded (`columns.llm_seeded.abstention.false_answer_rate`) | null | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-076 | false_answer_rate, handwritten (`columns.handwritten.abstention.false_answer_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-077 | false_answer_rate, aggregate (`columns.aggregate.abstention.false_answer_rate`) | null | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-078 | over_abstention_rate, xbrl_auto (`columns.xbrl_auto.abstention.over_abstention_rate`) | 0.0 | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-079 | over_abstention_rate, llm_seeded (`columns.llm_seeded.abstention.over_abstention_rate`) | 0.0 | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-080 | over_abstention_rate, handwritten (`columns.handwritten.abstention.over_abstention_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-081 | over_abstention_rate, aggregate (`columns.aggregate.abstention.over_abstention_rate`) | 0.0 | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-082 | cost_per_query, xbrl_auto (`columns.xbrl_auto.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-083 | cost_per_query, llm_seeded (`columns.llm_seeded.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-084 | cost_per_query, handwritten (`columns.handwritten.cost_per_query`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-085 | cost_per_query, aggregate (`columns.aggregate.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-086 | answer_correctness, xbrl_auto (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-087 | answer_correctness, llm_seeded (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-088 | answer_correctness, handwritten (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-089 | answer_correctness, aggregate (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |
| R-090 | natural_phrasing_gap, aggregate (not a report field) | absent: no report carries it; needs hand-written natural-phrasing items (F-103) | development | `eval/runs/f2e616e0a7d7.json` | `81c332f` |

### 63cf35c328e2

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-091 | sufficiency_at_10, xbrl_auto (`columns.xbrl_auto.sufficiency@10`) | 0.365 | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-092 | sufficiency_at_10, llm_seeded (`columns.llm_seeded.sufficiency@10`) | 0.891566265060241 | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-093 | sufficiency_at_10, handwritten (`columns.handwritten.sufficiency@10`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-094 | sufficiency_at_10, aggregate (`columns.aggregate.sufficiency@10`) | 0.519434628975265 | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-095 | faithfulness_pre, xbrl_auto (`columns.xbrl_auto.generation.faithfulness_pre`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-096 | faithfulness_pre, llm_seeded (`columns.llm_seeded.generation.faithfulness_pre`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-097 | faithfulness_pre, handwritten (`columns.handwritten.generation.faithfulness_pre`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-098 | faithfulness_pre, aggregate (`columns.aggregate.generation.faithfulness_pre`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-099 | claim_retention, xbrl_auto (`columns.xbrl_auto.generation.claim_retention`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-100 | claim_retention, llm_seeded (`columns.llm_seeded.generation.claim_retention`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-101 | claim_retention, handwritten (`columns.handwritten.generation.claim_retention`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-102 | claim_retention, aggregate (`columns.aggregate.generation.claim_retention`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-103 | citation_coverage, xbrl_auto (`columns.xbrl_auto.generation.citation_coverage`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-104 | citation_coverage, llm_seeded (`columns.llm_seeded.generation.citation_coverage`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-105 | citation_coverage, handwritten (`columns.handwritten.generation.citation_coverage`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-106 | citation_coverage, aggregate (`columns.aggregate.generation.citation_coverage`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-107 | xbrl_contradiction, xbrl_auto (`columns.xbrl_auto.generation.xbrl_contradiction_rate`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-108 | xbrl_contradiction, llm_seeded (`columns.llm_seeded.generation.xbrl_contradiction_rate`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-109 | xbrl_contradiction, handwritten (`columns.handwritten.generation.xbrl_contradiction_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-110 | xbrl_contradiction, aggregate (`columns.aggregate.generation.xbrl_contradiction_rate`) | `n/a: no claims` (from `generation.status`) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-111 | false_answer_rate, xbrl_auto (`columns.xbrl_auto.abstention.false_answer_rate`) | null | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-112 | false_answer_rate, llm_seeded (`columns.llm_seeded.abstention.false_answer_rate`) | null | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-113 | false_answer_rate, handwritten (`columns.handwritten.abstention.false_answer_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-114 | false_answer_rate, aggregate (`columns.aggregate.abstention.false_answer_rate`) | null | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-115 | over_abstention_rate, xbrl_auto (`columns.xbrl_auto.abstention.over_abstention_rate`) | 0.0 | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-116 | over_abstention_rate, llm_seeded (`columns.llm_seeded.abstention.over_abstention_rate`) | 0.0 | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-117 | over_abstention_rate, handwritten (`columns.handwritten.abstention.over_abstention_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-118 | over_abstention_rate, aggregate (`columns.aggregate.abstention.over_abstention_rate`) | 0.0 | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-119 | cost_per_query, xbrl_auto (`columns.xbrl_auto.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-120 | cost_per_query, llm_seeded (`columns.llm_seeded.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-121 | cost_per_query, handwritten (`columns.handwritten.cost_per_query`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-122 | cost_per_query, aggregate (`columns.aggregate.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-123 | answer_correctness, xbrl_auto (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-124 | answer_correctness, llm_seeded (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-125 | answer_correctness, handwritten (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-126 | answer_correctness, aggregate (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |
| R-127 | natural_phrasing_gap, aggregate (not a report field) | absent: no report carries it; needs hand-written natural-phrasing items (F-103) | development | `eval/runs/63cf35c328e2.json` | `f42b2fe` |

### a4e39a65c2c8

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-128 | sufficiency_at_10, xbrl_auto (`columns.xbrl_auto.sufficiency@10`) | 0.705 | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-129 | sufficiency_at_10, llm_seeded (`columns.llm_seeded.sufficiency@10`) | 1.0 | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-130 | sufficiency_at_10, handwritten (`columns.handwritten.sufficiency@10`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-131 | sufficiency_at_10, aggregate (`columns.aggregate.sufficiency@10`) | 0.7915194346289752 | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-132 | faithfulness_pre, xbrl_auto (`columns.xbrl_auto.generation.faithfulness_pre`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-133 | faithfulness_pre, llm_seeded (`columns.llm_seeded.generation.faithfulness_pre`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-134 | faithfulness_pre, handwritten (`columns.handwritten.generation.faithfulness_pre`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-135 | faithfulness_pre, aggregate (`columns.aggregate.generation.faithfulness_pre`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-136 | claim_retention, xbrl_auto (`columns.xbrl_auto.generation.claim_retention`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-137 | claim_retention, llm_seeded (`columns.llm_seeded.generation.claim_retention`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-138 | claim_retention, handwritten (`columns.handwritten.generation.claim_retention`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-139 | claim_retention, aggregate (`columns.aggregate.generation.claim_retention`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-140 | citation_coverage, xbrl_auto (`columns.xbrl_auto.generation.citation_coverage`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-141 | citation_coverage, llm_seeded (`columns.llm_seeded.generation.citation_coverage`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-142 | citation_coverage, handwritten (`columns.handwritten.generation.citation_coverage`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-143 | citation_coverage, aggregate (`columns.aggregate.generation.citation_coverage`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-144 | xbrl_contradiction, xbrl_auto (`columns.xbrl_auto.generation.xbrl_contradiction_rate`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-145 | xbrl_contradiction, llm_seeded (`columns.llm_seeded.generation.xbrl_contradiction_rate`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-146 | xbrl_contradiction, handwritten (`columns.handwritten.generation.xbrl_contradiction_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-147 | xbrl_contradiction, aggregate (`columns.aggregate.generation.xbrl_contradiction_rate`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-148 | false_answer_rate, xbrl_auto (`columns.xbrl_auto.abstention.false_answer_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-149 | false_answer_rate, llm_seeded (`columns.llm_seeded.abstention.false_answer_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-150 | false_answer_rate, handwritten (`columns.handwritten.abstention.false_answer_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-151 | false_answer_rate, aggregate (`columns.aggregate.abstention.false_answer_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-152 | over_abstention_rate, xbrl_auto (`columns.xbrl_auto.abstention.over_abstention_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-153 | over_abstention_rate, llm_seeded (`columns.llm_seeded.abstention.over_abstention_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-154 | over_abstention_rate, handwritten (`columns.handwritten.abstention.over_abstention_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-155 | over_abstention_rate, aggregate (`columns.aggregate.abstention.over_abstention_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-156 | cost_per_query, xbrl_auto (`columns.xbrl_auto.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-157 | cost_per_query, llm_seeded (`columns.llm_seeded.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-158 | cost_per_query, handwritten (`columns.handwritten.cost_per_query`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-159 | cost_per_query, aggregate (`columns.aggregate.cost_per_query`) | absent: the field is not in this report | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-160 | answer_correctness, xbrl_auto (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-161 | answer_correctness, llm_seeded (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-162 | answer_correctness, handwritten (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-163 | answer_correctness, aggregate (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |
| R-164 | natural_phrasing_gap, aggregate (not a report field) | absent: no report carries it; needs hand-written natural-phrasing items (F-103) | development | `eval/runs/a4e39a65c2c8.json` | `895bf6d` |

### 7a079fe7abfe

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-165 | sufficiency_at_10, xbrl_auto (`columns.xbrl_auto.sufficiency@10`) | 0.71 | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-166 | sufficiency_at_10, llm_seeded (`columns.llm_seeded.sufficiency@10`) | 1.0 | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-167 | sufficiency_at_10, handwritten (`columns.handwritten.sufficiency@10`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-168 | sufficiency_at_10, aggregate (`columns.aggregate.sufficiency@10`) | 0.7950530035335689 | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-169 | faithfulness_pre, xbrl_auto (`columns.xbrl_auto.generation.faithfulness_pre`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-170 | faithfulness_pre, llm_seeded (`columns.llm_seeded.generation.faithfulness_pre`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-171 | faithfulness_pre, handwritten (`columns.handwritten.generation.faithfulness_pre`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-172 | faithfulness_pre, aggregate (`columns.aggregate.generation.faithfulness_pre`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-173 | claim_retention, xbrl_auto (`columns.xbrl_auto.generation.claim_retention`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-174 | claim_retention, llm_seeded (`columns.llm_seeded.generation.claim_retention`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-175 | claim_retention, handwritten (`columns.handwritten.generation.claim_retention`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-176 | claim_retention, aggregate (`columns.aggregate.generation.claim_retention`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-177 | citation_coverage, xbrl_auto (`columns.xbrl_auto.generation.citation_coverage`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-178 | citation_coverage, llm_seeded (`columns.llm_seeded.generation.citation_coverage`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-179 | citation_coverage, handwritten (`columns.handwritten.generation.citation_coverage`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-180 | citation_coverage, aggregate (`columns.aggregate.generation.citation_coverage`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-181 | xbrl_contradiction, xbrl_auto (`columns.xbrl_auto.generation.xbrl_contradiction_rate`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-182 | xbrl_contradiction, llm_seeded (`columns.llm_seeded.generation.xbrl_contradiction_rate`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-183 | xbrl_contradiction, handwritten (`columns.handwritten.generation.xbrl_contradiction_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-184 | xbrl_contradiction, aggregate (`columns.aggregate.generation.xbrl_contradiction_rate`) | `pending NLI threshold (F-125)` (from `generation.status`) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-185 | false_answer_rate, xbrl_auto (`columns.xbrl_auto.abstention.false_answer_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-186 | false_answer_rate, llm_seeded (`columns.llm_seeded.abstention.false_answer_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-187 | false_answer_rate, handwritten (`columns.handwritten.abstention.false_answer_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-188 | false_answer_rate, aggregate (`columns.aggregate.abstention.false_answer_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-189 | over_abstention_rate, xbrl_auto (`columns.xbrl_auto.abstention.over_abstention_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-190 | over_abstention_rate, llm_seeded (`columns.llm_seeded.abstention.over_abstention_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-191 | over_abstention_rate, handwritten (`columns.handwritten.abstention.over_abstention_rate`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-192 | over_abstention_rate, aggregate (`columns.aggregate.abstention.over_abstention_rate`) | `pending NLI threshold (F-125)` | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-193 | cost_per_query, xbrl_auto (`columns.xbrl_auto.cost_per_query`) | `cost n/a (dev backend)` | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-194 | cost_per_query, llm_seeded (`columns.llm_seeded.cost_per_query`) | `cost n/a (dev backend)` | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-195 | cost_per_query, handwritten (`columns.handwritten.cost_per_query`) | null: the report's `handwritten` column is null (no hand-written items, F-103) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-196 | cost_per_query, aggregate (`columns.aggregate.cost_per_query`) | `cost n/a (dev backend)` | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-197 | answer_correctness, xbrl_auto (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-198 | answer_correctness, llm_seeded (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-199 | answer_correctness, handwritten (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-200 | answer_correctness, aggregate (not a report field) | absent: no report carries it; the judge waits on validation labels (F-105) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |
| R-201 | natural_phrasing_gap, aggregate (not a report field) | absent: no report carries it; needs hand-written natural-phrasing items (F-103) | development | `eval/runs/7a079fe7abfe.json` | `2cee0cd` |

## Retrieval ablation — 373f11f1949c

Sufficiency@10 values below are stored `sufficient` / `scored` counts, not
computed rates. `0/0 (N/A)` means no items were scored. Depth is the retrieval
pool depth, not the evaluation cutoff of 10.

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-202 | Sufficiency@10, all, aggregate, dense, depth 20 (`results_at_10["all"]["aggregate"]["dense"]["20"].sufficient` / `results_at_10["all"]["aggregate"]["dense"]["20"].scored`) | 132/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-203 | Sufficiency@10, all, aggregate, dense, depth 50 (`results_at_10["all"]["aggregate"]["dense"]["50"].sufficient` / `results_at_10["all"]["aggregate"]["dense"]["50"].scored`) | 132/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-204 | Sufficiency@10, all, aggregate, dense, depth 100 (`results_at_10["all"]["aggregate"]["dense"]["100"].sufficient` / `results_at_10["all"]["aggregate"]["dense"]["100"].scored`) | 132/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-205 | Sufficiency@10, all, aggregate, sparse, depth 20 (`results_at_10["all"]["aggregate"]["sparse"]["20"].sufficient` / `results_at_10["all"]["aggregate"]["sparse"]["20"].scored`) | 123/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-206 | Sufficiency@10, all, aggregate, sparse, depth 50 (`results_at_10["all"]["aggregate"]["sparse"]["50"].sufficient` / `results_at_10["all"]["aggregate"]["sparse"]["50"].scored`) | 123/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-207 | Sufficiency@10, all, aggregate, sparse, depth 100 (`results_at_10["all"]["aggregate"]["sparse"]["100"].sufficient` / `results_at_10["all"]["aggregate"]["sparse"]["100"].scored`) | 123/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-208 | Sufficiency@10, all, aggregate, hybrid_1_1, depth 20 (`results_at_10["all"]["aggregate"]["hybrid_1_1"]["20"].sufficient` / `results_at_10["all"]["aggregate"]["hybrid_1_1"]["20"].scored`) | 156/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-209 | Sufficiency@10, all, aggregate, hybrid_1_1, depth 50 (`results_at_10["all"]["aggregate"]["hybrid_1_1"]["50"].sufficient` / `results_at_10["all"]["aggregate"]["hybrid_1_1"]["50"].scored`) | 166/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-210 | Sufficiency@10, all, aggregate, hybrid_1_1, depth 100 (`results_at_10["all"]["aggregate"]["hybrid_1_1"]["100"].sufficient` / `results_at_10["all"]["aggregate"]["hybrid_1_1"]["100"].scored`) | 173/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-211 | Sufficiency@10, all, aggregate, hybrid_1.5_1, depth 20 (`results_at_10["all"]["aggregate"]["hybrid_1.5_1"]["20"].sufficient` / `results_at_10["all"]["aggregate"]["hybrid_1.5_1"]["20"].scored`) | 147/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-212 | Sufficiency@10, all, aggregate, hybrid_1.5_1, depth 50 (`results_at_10["all"]["aggregate"]["hybrid_1.5_1"]["50"].sufficient` / `results_at_10["all"]["aggregate"]["hybrid_1.5_1"]["50"].scored`) | 170/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-213 | Sufficiency@10, all, aggregate, hybrid_1.5_1, depth 100 (`results_at_10["all"]["aggregate"]["hybrid_1.5_1"]["100"].sufficient` / `results_at_10["all"]["aggregate"]["hybrid_1.5_1"]["100"].scored`) | 173/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-214 | Sufficiency@10, all, aggregate, hybrid_1_1.5, depth 20 (`results_at_10["all"]["aggregate"]["hybrid_1_1.5"]["20"].sufficient` / `results_at_10["all"]["aggregate"]["hybrid_1_1.5"]["20"].scored`) | 128/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-215 | Sufficiency@10, all, aggregate, hybrid_1_1.5, depth 50 (`results_at_10["all"]["aggregate"]["hybrid_1_1.5"]["50"].sufficient` / `results_at_10["all"]["aggregate"]["hybrid_1_1.5"]["50"].scored`) | 146/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-216 | Sufficiency@10, all, aggregate, hybrid_1_1.5, depth 100 (`results_at_10["all"]["aggregate"]["hybrid_1_1.5"]["100"].sufficient` / `results_at_10["all"]["aggregate"]["hybrid_1_1.5"]["100"].scored`) | 164/332 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-217 | Sufficiency@10, all, xbrl_auto, dense, depth 20 (`results_at_10["all"]["xbrl_auto"]["dense"]["20"].sufficient` / `results_at_10["all"]["xbrl_auto"]["dense"]["20"].scored`) | 62/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-218 | Sufficiency@10, all, xbrl_auto, dense, depth 50 (`results_at_10["all"]["xbrl_auto"]["dense"]["50"].sufficient` / `results_at_10["all"]["xbrl_auto"]["dense"]["50"].scored`) | 62/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-219 | Sufficiency@10, all, xbrl_auto, dense, depth 100 (`results_at_10["all"]["xbrl_auto"]["dense"]["100"].sufficient` / `results_at_10["all"]["xbrl_auto"]["dense"]["100"].scored`) | 62/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-220 | Sufficiency@10, all, xbrl_auto, sparse, depth 20 (`results_at_10["all"]["xbrl_auto"]["sparse"]["20"].sufficient` / `results_at_10["all"]["xbrl_auto"]["sparse"]["20"].scored`) | 35/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-221 | Sufficiency@10, all, xbrl_auto, sparse, depth 50 (`results_at_10["all"]["xbrl_auto"]["sparse"]["50"].sufficient` / `results_at_10["all"]["xbrl_auto"]["sparse"]["50"].scored`) | 35/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-222 | Sufficiency@10, all, xbrl_auto, sparse, depth 100 (`results_at_10["all"]["xbrl_auto"]["sparse"]["100"].sufficient` / `results_at_10["all"]["xbrl_auto"]["sparse"]["100"].scored`) | 35/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-223 | Sufficiency@10, all, xbrl_auto, hybrid_1_1, depth 20 (`results_at_10["all"]["xbrl_auto"]["hybrid_1_1"]["20"].sufficient` / `results_at_10["all"]["xbrl_auto"]["hybrid_1_1"]["20"].scored`) | 66/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-224 | Sufficiency@10, all, xbrl_auto, hybrid_1_1, depth 50 (`results_at_10["all"]["xbrl_auto"]["hybrid_1_1"]["50"].sufficient` / `results_at_10["all"]["xbrl_auto"]["hybrid_1_1"]["50"].scored`) | 75/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-225 | Sufficiency@10, all, xbrl_auto, hybrid_1_1, depth 100 (`results_at_10["all"]["xbrl_auto"]["hybrid_1_1"]["100"].sufficient` / `results_at_10["all"]["xbrl_auto"]["hybrid_1_1"]["100"].scored`) | 80/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-226 | Sufficiency@10, all, xbrl_auto, hybrid_1.5_1, depth 20 (`results_at_10["all"]["xbrl_auto"]["hybrid_1.5_1"]["20"].sufficient` / `results_at_10["all"]["xbrl_auto"]["hybrid_1.5_1"]["20"].scored`) | 69/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-227 | Sufficiency@10, all, xbrl_auto, hybrid_1.5_1, depth 50 (`results_at_10["all"]["xbrl_auto"]["hybrid_1.5_1"]["50"].sufficient` / `results_at_10["all"]["xbrl_auto"]["hybrid_1.5_1"]["50"].scored`) | 82/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-228 | Sufficiency@10, all, xbrl_auto, hybrid_1.5_1, depth 100 (`results_at_10["all"]["xbrl_auto"]["hybrid_1.5_1"]["100"].sufficient` / `results_at_10["all"]["xbrl_auto"]["hybrid_1.5_1"]["100"].scored`) | 82/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-229 | Sufficiency@10, all, xbrl_auto, hybrid_1_1.5, depth 20 (`results_at_10["all"]["xbrl_auto"]["hybrid_1_1.5"]["20"].sufficient` / `results_at_10["all"]["xbrl_auto"]["hybrid_1_1.5"]["20"].scored`) | 40/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-230 | Sufficiency@10, all, xbrl_auto, hybrid_1_1.5, depth 50 (`results_at_10["all"]["xbrl_auto"]["hybrid_1_1.5"]["50"].sufficient` / `results_at_10["all"]["xbrl_auto"]["hybrid_1_1.5"]["50"].scored`) | 58/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-231 | Sufficiency@10, all, xbrl_auto, hybrid_1_1.5, depth 100 (`results_at_10["all"]["xbrl_auto"]["hybrid_1_1.5"]["100"].sufficient` / `results_at_10["all"]["xbrl_auto"]["hybrid_1_1.5"]["100"].scored`) | 71/200 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-232 | Sufficiency@10, all, llm_seeded, dense, depth 20 (`results_at_10["all"]["llm_seeded"]["dense"]["20"].sufficient` / `results_at_10["all"]["llm_seeded"]["dense"]["20"].scored`) | 50/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-233 | Sufficiency@10, all, llm_seeded, dense, depth 50 (`results_at_10["all"]["llm_seeded"]["dense"]["50"].sufficient` / `results_at_10["all"]["llm_seeded"]["dense"]["50"].scored`) | 50/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-234 | Sufficiency@10, all, llm_seeded, dense, depth 100 (`results_at_10["all"]["llm_seeded"]["dense"]["100"].sufficient` / `results_at_10["all"]["llm_seeded"]["dense"]["100"].scored`) | 50/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-235 | Sufficiency@10, all, llm_seeded, sparse, depth 20 (`results_at_10["all"]["llm_seeded"]["sparse"]["20"].sufficient` / `results_at_10["all"]["llm_seeded"]["sparse"]["20"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-236 | Sufficiency@10, all, llm_seeded, sparse, depth 50 (`results_at_10["all"]["llm_seeded"]["sparse"]["50"].sufficient` / `results_at_10["all"]["llm_seeded"]["sparse"]["50"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-237 | Sufficiency@10, all, llm_seeded, sparse, depth 100 (`results_at_10["all"]["llm_seeded"]["sparse"]["100"].sufficient` / `results_at_10["all"]["llm_seeded"]["sparse"]["100"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-238 | Sufficiency@10, all, llm_seeded, hybrid_1_1, depth 20 (`results_at_10["all"]["llm_seeded"]["hybrid_1_1"]["20"].sufficient` / `results_at_10["all"]["llm_seeded"]["hybrid_1_1"]["20"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-239 | Sufficiency@10, all, llm_seeded, hybrid_1_1, depth 50 (`results_at_10["all"]["llm_seeded"]["hybrid_1_1"]["50"].sufficient` / `results_at_10["all"]["llm_seeded"]["hybrid_1_1"]["50"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-240 | Sufficiency@10, all, llm_seeded, hybrid_1_1, depth 100 (`results_at_10["all"]["llm_seeded"]["hybrid_1_1"]["100"].sufficient` / `results_at_10["all"]["llm_seeded"]["hybrid_1_1"]["100"].scored`) | 66/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-241 | Sufficiency@10, all, llm_seeded, hybrid_1.5_1, depth 20 (`results_at_10["all"]["llm_seeded"]["hybrid_1.5_1"]["20"].sufficient` / `results_at_10["all"]["llm_seeded"]["hybrid_1.5_1"]["20"].scored`) | 57/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-242 | Sufficiency@10, all, llm_seeded, hybrid_1.5_1, depth 50 (`results_at_10["all"]["llm_seeded"]["hybrid_1.5_1"]["50"].sufficient` / `results_at_10["all"]["llm_seeded"]["hybrid_1.5_1"]["50"].scored`) | 63/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-243 | Sufficiency@10, all, llm_seeded, hybrid_1.5_1, depth 100 (`results_at_10["all"]["llm_seeded"]["hybrid_1.5_1"]["100"].sufficient` / `results_at_10["all"]["llm_seeded"]["hybrid_1.5_1"]["100"].scored`) | 63/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-244 | Sufficiency@10, all, llm_seeded, hybrid_1_1.5, depth 20 (`results_at_10["all"]["llm_seeded"]["hybrid_1_1.5"]["20"].sufficient` / `results_at_10["all"]["llm_seeded"]["hybrid_1_1.5"]["20"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-245 | Sufficiency@10, all, llm_seeded, hybrid_1_1.5, depth 50 (`results_at_10["all"]["llm_seeded"]["hybrid_1_1.5"]["50"].sufficient` / `results_at_10["all"]["llm_seeded"]["hybrid_1_1.5"]["50"].scored`) | 64/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-246 | Sufficiency@10, all, llm_seeded, hybrid_1_1.5, depth 100 (`results_at_10["all"]["llm_seeded"]["hybrid_1_1.5"]["100"].sufficient` / `results_at_10["all"]["llm_seeded"]["hybrid_1_1.5"]["100"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-247 | Sufficiency@10, all, handwritten, dense, depth 20 (`results_at_10["all"]["handwritten"]["dense"]["20"].sufficient` / `results_at_10["all"]["handwritten"]["dense"]["20"].scored`) | 20/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-248 | Sufficiency@10, all, handwritten, dense, depth 50 (`results_at_10["all"]["handwritten"]["dense"]["50"].sufficient` / `results_at_10["all"]["handwritten"]["dense"]["50"].scored`) | 20/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-249 | Sufficiency@10, all, handwritten, dense, depth 100 (`results_at_10["all"]["handwritten"]["dense"]["100"].sufficient` / `results_at_10["all"]["handwritten"]["dense"]["100"].scored`) | 20/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-250 | Sufficiency@10, all, handwritten, sparse, depth 20 (`results_at_10["all"]["handwritten"]["sparse"]["20"].sufficient` / `results_at_10["all"]["handwritten"]["sparse"]["20"].scored`) | 23/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-251 | Sufficiency@10, all, handwritten, sparse, depth 50 (`results_at_10["all"]["handwritten"]["sparse"]["50"].sufficient` / `results_at_10["all"]["handwritten"]["sparse"]["50"].scored`) | 23/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-252 | Sufficiency@10, all, handwritten, sparse, depth 100 (`results_at_10["all"]["handwritten"]["sparse"]["100"].sufficient` / `results_at_10["all"]["handwritten"]["sparse"]["100"].scored`) | 23/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-253 | Sufficiency@10, all, handwritten, hybrid_1_1, depth 20 (`results_at_10["all"]["handwritten"]["hybrid_1_1"]["20"].sufficient` / `results_at_10["all"]["handwritten"]["hybrid_1_1"]["20"].scored`) | 25/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-254 | Sufficiency@10, all, handwritten, hybrid_1_1, depth 50 (`results_at_10["all"]["handwritten"]["hybrid_1_1"]["50"].sufficient` / `results_at_10["all"]["handwritten"]["hybrid_1_1"]["50"].scored`) | 26/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-255 | Sufficiency@10, all, handwritten, hybrid_1_1, depth 100 (`results_at_10["all"]["handwritten"]["hybrid_1_1"]["100"].sufficient` / `results_at_10["all"]["handwritten"]["hybrid_1_1"]["100"].scored`) | 27/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-256 | Sufficiency@10, all, handwritten, hybrid_1.5_1, depth 20 (`results_at_10["all"]["handwritten"]["hybrid_1.5_1"]["20"].sufficient` / `results_at_10["all"]["handwritten"]["hybrid_1.5_1"]["20"].scored`) | 21/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-257 | Sufficiency@10, all, handwritten, hybrid_1.5_1, depth 50 (`results_at_10["all"]["handwritten"]["hybrid_1.5_1"]["50"].sufficient` / `results_at_10["all"]["handwritten"]["hybrid_1.5_1"]["50"].scored`) | 25/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-258 | Sufficiency@10, all, handwritten, hybrid_1.5_1, depth 100 (`results_at_10["all"]["handwritten"]["hybrid_1.5_1"]["100"].sufficient` / `results_at_10["all"]["handwritten"]["hybrid_1.5_1"]["100"].scored`) | 28/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-259 | Sufficiency@10, all, handwritten, hybrid_1_1.5, depth 20 (`results_at_10["all"]["handwritten"]["hybrid_1_1.5"]["20"].sufficient` / `results_at_10["all"]["handwritten"]["hybrid_1_1.5"]["20"].scored`) | 23/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-260 | Sufficiency@10, all, handwritten, hybrid_1_1.5, depth 50 (`results_at_10["all"]["handwritten"]["hybrid_1_1.5"]["50"].sufficient` / `results_at_10["all"]["handwritten"]["hybrid_1_1.5"]["50"].scored`) | 24/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-261 | Sufficiency@10, all, handwritten, hybrid_1_1.5, depth 100 (`results_at_10["all"]["handwritten"]["hybrid_1_1.5"]["100"].sufficient` / `results_at_10["all"]["handwritten"]["hybrid_1_1.5"]["100"].scored`) | 28/60 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-262 | Sufficiency@10, reviewed, aggregate, dense, depth 20 (`results_at_10["reviewed"]["aggregate"]["dense"]["20"].sufficient` / `results_at_10["reviewed"]["aggregate"]["dense"]["20"].scored`) | 60/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-263 | Sufficiency@10, reviewed, aggregate, dense, depth 50 (`results_at_10["reviewed"]["aggregate"]["dense"]["50"].sufficient` / `results_at_10["reviewed"]["aggregate"]["dense"]["50"].scored`) | 60/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-264 | Sufficiency@10, reviewed, aggregate, dense, depth 100 (`results_at_10["reviewed"]["aggregate"]["dense"]["100"].sufficient` / `results_at_10["reviewed"]["aggregate"]["dense"]["100"].scored`) | 60/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-265 | Sufficiency@10, reviewed, aggregate, sparse, depth 20 (`results_at_10["reviewed"]["aggregate"]["sparse"]["20"].sufficient` / `results_at_10["reviewed"]["aggregate"]["sparse"]["20"].scored`) | 73/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-266 | Sufficiency@10, reviewed, aggregate, sparse, depth 50 (`results_at_10["reviewed"]["aggregate"]["sparse"]["50"].sufficient` / `results_at_10["reviewed"]["aggregate"]["sparse"]["50"].scored`) | 73/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-267 | Sufficiency@10, reviewed, aggregate, sparse, depth 100 (`results_at_10["reviewed"]["aggregate"]["sparse"]["100"].sufficient` / `results_at_10["reviewed"]["aggregate"]["sparse"]["100"].scored`) | 73/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-268 | Sufficiency@10, reviewed, aggregate, hybrid_1_1, depth 20 (`results_at_10["reviewed"]["aggregate"]["hybrid_1_1"]["20"].sufficient` / `results_at_10["reviewed"]["aggregate"]["hybrid_1_1"]["20"].scored`) | 79/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-269 | Sufficiency@10, reviewed, aggregate, hybrid_1_1, depth 50 (`results_at_10["reviewed"]["aggregate"]["hybrid_1_1"]["50"].sufficient` / `results_at_10["reviewed"]["aggregate"]["hybrid_1_1"]["50"].scored`) | 79/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-270 | Sufficiency@10, reviewed, aggregate, hybrid_1_1, depth 100 (`results_at_10["reviewed"]["aggregate"]["hybrid_1_1"]["100"].sufficient` / `results_at_10["reviewed"]["aggregate"]["hybrid_1_1"]["100"].scored`) | 81/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-271 | Sufficiency@10, reviewed, aggregate, hybrid_1.5_1, depth 20 (`results_at_10["reviewed"]["aggregate"]["hybrid_1.5_1"]["20"].sufficient` / `results_at_10["reviewed"]["aggregate"]["hybrid_1.5_1"]["20"].scored`) | 71/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-272 | Sufficiency@10, reviewed, aggregate, hybrid_1.5_1, depth 50 (`results_at_10["reviewed"]["aggregate"]["hybrid_1.5_1"]["50"].sufficient` / `results_at_10["reviewed"]["aggregate"]["hybrid_1.5_1"]["50"].scored`) | 81/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-273 | Sufficiency@10, reviewed, aggregate, hybrid_1.5_1, depth 100 (`results_at_10["reviewed"]["aggregate"]["hybrid_1.5_1"]["100"].sufficient` / `results_at_10["reviewed"]["aggregate"]["hybrid_1.5_1"]["100"].scored`) | 80/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-274 | Sufficiency@10, reviewed, aggregate, hybrid_1_1.5, depth 20 (`results_at_10["reviewed"]["aggregate"]["hybrid_1_1.5"]["20"].sufficient` / `results_at_10["reviewed"]["aggregate"]["hybrid_1_1.5"]["20"].scored`) | 75/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-275 | Sufficiency@10, reviewed, aggregate, hybrid_1_1.5, depth 50 (`results_at_10["reviewed"]["aggregate"]["hybrid_1_1.5"]["50"].sufficient` / `results_at_10["reviewed"]["aggregate"]["hybrid_1_1.5"]["50"].scored`) | 76/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-276 | Sufficiency@10, reviewed, aggregate, hybrid_1_1.5, depth 100 (`results_at_10["reviewed"]["aggregate"]["hybrid_1_1.5"]["100"].sufficient` / `results_at_10["reviewed"]["aggregate"]["hybrid_1_1.5"]["100"].scored`) | 81/125 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-277 | Sufficiency@10, reviewed, xbrl_auto, dense, depth 20 (`results_at_10["reviewed"]["xbrl_auto"]["dense"]["20"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["dense"]["20"].scored`) | 10/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-278 | Sufficiency@10, reviewed, xbrl_auto, dense, depth 50 (`results_at_10["reviewed"]["xbrl_auto"]["dense"]["50"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["dense"]["50"].scored`) | 10/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-279 | Sufficiency@10, reviewed, xbrl_auto, dense, depth 100 (`results_at_10["reviewed"]["xbrl_auto"]["dense"]["100"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["dense"]["100"].scored`) | 10/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-280 | Sufficiency@10, reviewed, xbrl_auto, sparse, depth 20 (`results_at_10["reviewed"]["xbrl_auto"]["sparse"]["20"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["sparse"]["20"].scored`) | 8/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-281 | Sufficiency@10, reviewed, xbrl_auto, sparse, depth 50 (`results_at_10["reviewed"]["xbrl_auto"]["sparse"]["50"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["sparse"]["50"].scored`) | 8/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-282 | Sufficiency@10, reviewed, xbrl_auto, sparse, depth 100 (`results_at_10["reviewed"]["xbrl_auto"]["sparse"]["100"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["sparse"]["100"].scored`) | 8/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-283 | Sufficiency@10, reviewed, xbrl_auto, hybrid_1_1, depth 20 (`results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1"]["20"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1"]["20"].scored`) | 14/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-284 | Sufficiency@10, reviewed, xbrl_auto, hybrid_1_1, depth 50 (`results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1"]["50"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1"]["50"].scored`) | 14/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-285 | Sufficiency@10, reviewed, xbrl_auto, hybrid_1_1, depth 100 (`results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1"]["100"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1"]["100"].scored`) | 15/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-286 | Sufficiency@10, reviewed, xbrl_auto, hybrid_1.5_1, depth 20 (`results_at_10["reviewed"]["xbrl_auto"]["hybrid_1.5_1"]["20"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["hybrid_1.5_1"]["20"].scored`) | 14/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-287 | Sufficiency@10, reviewed, xbrl_auto, hybrid_1.5_1, depth 50 (`results_at_10["reviewed"]["xbrl_auto"]["hybrid_1.5_1"]["50"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["hybrid_1.5_1"]["50"].scored`) | 18/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-288 | Sufficiency@10, reviewed, xbrl_auto, hybrid_1.5_1, depth 100 (`results_at_10["reviewed"]["xbrl_auto"]["hybrid_1.5_1"]["100"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["hybrid_1.5_1"]["100"].scored`) | 17/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-289 | Sufficiency@10, reviewed, xbrl_auto, hybrid_1_1.5, depth 20 (`results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1.5"]["20"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1.5"]["20"].scored`) | 10/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-290 | Sufficiency@10, reviewed, xbrl_auto, hybrid_1_1.5, depth 50 (`results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1.5"]["50"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1.5"]["50"].scored`) | 12/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-291 | Sufficiency@10, reviewed, xbrl_auto, hybrid_1_1.5, depth 100 (`results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1.5"]["100"].sufficient` / `results_at_10["reviewed"]["xbrl_auto"]["hybrid_1_1.5"]["100"].scored`) | 16/53 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-292 | Sufficiency@10, reviewed, llm_seeded, dense, depth 20 (`results_at_10["reviewed"]["llm_seeded"]["dense"]["20"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["dense"]["20"].scored`) | 50/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-293 | Sufficiency@10, reviewed, llm_seeded, dense, depth 50 (`results_at_10["reviewed"]["llm_seeded"]["dense"]["50"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["dense"]["50"].scored`) | 50/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-294 | Sufficiency@10, reviewed, llm_seeded, dense, depth 100 (`results_at_10["reviewed"]["llm_seeded"]["dense"]["100"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["dense"]["100"].scored`) | 50/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-295 | Sufficiency@10, reviewed, llm_seeded, sparse, depth 20 (`results_at_10["reviewed"]["llm_seeded"]["sparse"]["20"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["sparse"]["20"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-296 | Sufficiency@10, reviewed, llm_seeded, sparse, depth 50 (`results_at_10["reviewed"]["llm_seeded"]["sparse"]["50"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["sparse"]["50"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-297 | Sufficiency@10, reviewed, llm_seeded, sparse, depth 100 (`results_at_10["reviewed"]["llm_seeded"]["sparse"]["100"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["sparse"]["100"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-298 | Sufficiency@10, reviewed, llm_seeded, hybrid_1_1, depth 20 (`results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1"]["20"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1"]["20"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-299 | Sufficiency@10, reviewed, llm_seeded, hybrid_1_1, depth 50 (`results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1"]["50"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1"]["50"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-300 | Sufficiency@10, reviewed, llm_seeded, hybrid_1_1, depth 100 (`results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1"]["100"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1"]["100"].scored`) | 66/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-301 | Sufficiency@10, reviewed, llm_seeded, hybrid_1.5_1, depth 20 (`results_at_10["reviewed"]["llm_seeded"]["hybrid_1.5_1"]["20"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["hybrid_1.5_1"]["20"].scored`) | 57/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-302 | Sufficiency@10, reviewed, llm_seeded, hybrid_1.5_1, depth 50 (`results_at_10["reviewed"]["llm_seeded"]["hybrid_1.5_1"]["50"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["hybrid_1.5_1"]["50"].scored`) | 63/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-303 | Sufficiency@10, reviewed, llm_seeded, hybrid_1.5_1, depth 100 (`results_at_10["reviewed"]["llm_seeded"]["hybrid_1.5_1"]["100"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["hybrid_1.5_1"]["100"].scored`) | 63/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-304 | Sufficiency@10, reviewed, llm_seeded, hybrid_1_1.5, depth 20 (`results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1.5"]["20"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1.5"]["20"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-305 | Sufficiency@10, reviewed, llm_seeded, hybrid_1_1.5, depth 50 (`results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1.5"]["50"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1.5"]["50"].scored`) | 64/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-306 | Sufficiency@10, reviewed, llm_seeded, hybrid_1_1.5, depth 100 (`results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1.5"]["100"].sufficient` / `results_at_10["reviewed"]["llm_seeded"]["hybrid_1_1.5"]["100"].scored`) | 65/72 | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-307 | Sufficiency@10, reviewed, handwritten, dense, depth 20 (`results_at_10["reviewed"]["handwritten"]["dense"]["20"].sufficient` / `results_at_10["reviewed"]["handwritten"]["dense"]["20"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-308 | Sufficiency@10, reviewed, handwritten, dense, depth 50 (`results_at_10["reviewed"]["handwritten"]["dense"]["50"].sufficient` / `results_at_10["reviewed"]["handwritten"]["dense"]["50"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-309 | Sufficiency@10, reviewed, handwritten, dense, depth 100 (`results_at_10["reviewed"]["handwritten"]["dense"]["100"].sufficient` / `results_at_10["reviewed"]["handwritten"]["dense"]["100"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-310 | Sufficiency@10, reviewed, handwritten, sparse, depth 20 (`results_at_10["reviewed"]["handwritten"]["sparse"]["20"].sufficient` / `results_at_10["reviewed"]["handwritten"]["sparse"]["20"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-311 | Sufficiency@10, reviewed, handwritten, sparse, depth 50 (`results_at_10["reviewed"]["handwritten"]["sparse"]["50"].sufficient` / `results_at_10["reviewed"]["handwritten"]["sparse"]["50"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-312 | Sufficiency@10, reviewed, handwritten, sparse, depth 100 (`results_at_10["reviewed"]["handwritten"]["sparse"]["100"].sufficient` / `results_at_10["reviewed"]["handwritten"]["sparse"]["100"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-313 | Sufficiency@10, reviewed, handwritten, hybrid_1_1, depth 20 (`results_at_10["reviewed"]["handwritten"]["hybrid_1_1"]["20"].sufficient` / `results_at_10["reviewed"]["handwritten"]["hybrid_1_1"]["20"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-314 | Sufficiency@10, reviewed, handwritten, hybrid_1_1, depth 50 (`results_at_10["reviewed"]["handwritten"]["hybrid_1_1"]["50"].sufficient` / `results_at_10["reviewed"]["handwritten"]["hybrid_1_1"]["50"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-315 | Sufficiency@10, reviewed, handwritten, hybrid_1_1, depth 100 (`results_at_10["reviewed"]["handwritten"]["hybrid_1_1"]["100"].sufficient` / `results_at_10["reviewed"]["handwritten"]["hybrid_1_1"]["100"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-316 | Sufficiency@10, reviewed, handwritten, hybrid_1.5_1, depth 20 (`results_at_10["reviewed"]["handwritten"]["hybrid_1.5_1"]["20"].sufficient` / `results_at_10["reviewed"]["handwritten"]["hybrid_1.5_1"]["20"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-317 | Sufficiency@10, reviewed, handwritten, hybrid_1.5_1, depth 50 (`results_at_10["reviewed"]["handwritten"]["hybrid_1.5_1"]["50"].sufficient` / `results_at_10["reviewed"]["handwritten"]["hybrid_1.5_1"]["50"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-318 | Sufficiency@10, reviewed, handwritten, hybrid_1.5_1, depth 100 (`results_at_10["reviewed"]["handwritten"]["hybrid_1.5_1"]["100"].sufficient` / `results_at_10["reviewed"]["handwritten"]["hybrid_1.5_1"]["100"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-319 | Sufficiency@10, reviewed, handwritten, hybrid_1_1.5, depth 20 (`results_at_10["reviewed"]["handwritten"]["hybrid_1_1.5"]["20"].sufficient` / `results_at_10["reviewed"]["handwritten"]["hybrid_1_1.5"]["20"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-320 | Sufficiency@10, reviewed, handwritten, hybrid_1_1.5, depth 50 (`results_at_10["reviewed"]["handwritten"]["hybrid_1_1.5"]["50"].sufficient` / `results_at_10["reviewed"]["handwritten"]["hybrid_1_1.5"]["50"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |
| R-321 | Sufficiency@10, reviewed, handwritten, hybrid_1_1.5, depth 100 (`results_at_10["reviewed"]["handwritten"]["hybrid_1_1.5"]["100"].sufficient` / `results_at_10["reviewed"]["handwritten"]["hybrid_1_1.5"]["100"].scored`) | 0/0 (N/A) | development | `eval/runs/retrieval-ablation-373f11f1949c.json` | `8481fb4` |

## Golden v1 development run 35b3efbbfd5d

The run resumed after 48f2b01; 200 rerank fallbacks make it hardware-dependent. Null is not zero. Verdict counts are counted from each derived artifact’s item records.

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-322 | as-run xbrl_auto columns.xbrl_auto.sufficiency@10 | 0.71 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-323 | as-run xbrl_auto columns.xbrl_auto.cost_per_query | `cost n/a (dev backend)` | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-324 | as-run xbrl_auto columns.xbrl_auto.rerank_fell_back | 148 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-325 | as-run xbrl_auto columns.xbrl_auto.numeric.numeric_accuracy | 0.7 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-326 | as-run xbrl_auto columns.xbrl_auto.generation.answer_rate | 0.815 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-327 | as-run xbrl_auto columns.xbrl_auto.generation.faithfulness_pre | 0.9385964912280702 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-328 | as-run xbrl_auto columns.xbrl_auto.generation.claim_retention | 0.9385964912280702 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-329 | as-run xbrl_auto columns.xbrl_auto.generation.citation_coverage | 1.0 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-330 | as-run xbrl_auto columns.xbrl_auto.generation.xbrl_contradiction_rate | 0.01327433628318584 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-331 | as-run xbrl_auto columns.xbrl_auto.abstention.false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-332 | as-run xbrl_auto columns.xbrl_auto.abstention.over_abstention_rate | 0.24 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-333 | as-run xbrl_auto columns.xbrl_auto.abstention.abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-334 | as-run llm_seeded columns.llm_seeded.sufficiency@10 | 0.9583333333333334 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-335 | as-run llm_seeded columns.llm_seeded.cost_per_query | `cost n/a (dev backend)` | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-336 | as-run llm_seeded columns.llm_seeded.rerank_fell_back | 13 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-337 | as-run llm_seeded columns.llm_seeded.numeric.numeric_accuracy | 0.7894736842105263 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-338 | as-run llm_seeded columns.llm_seeded.generation.answer_rate | 0.9166666666666666 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-339 | as-run llm_seeded columns.llm_seeded.generation.faithfulness_pre | 0.8266666666666667 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-340 | as-run llm_seeded columns.llm_seeded.generation.claim_retention | 0.8266666666666667 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-341 | as-run llm_seeded columns.llm_seeded.generation.citation_coverage | 1.0 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-342 | as-run llm_seeded columns.llm_seeded.generation.xbrl_contradiction_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-343 | as-run llm_seeded columns.llm_seeded.abstention.false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-344 | as-run llm_seeded columns.llm_seeded.abstention.over_abstention_rate | 0.16666666666666666 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-345 | as-run llm_seeded columns.llm_seeded.abstention.abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-346 | as-run handwritten columns.handwritten.sufficiency@10 | 0.6833333333333333 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-347 | as-run handwritten columns.handwritten.cost_per_query | `cost n/a (dev backend)` | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-348 | as-run handwritten columns.handwritten.rerank_fell_back | 39 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-349 | as-run handwritten columns.handwritten.numeric.numeric_accuracy | 0.8 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-350 | as-run handwritten columns.handwritten.generation.answer_rate | 0.36666666666666664 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-351 | as-run handwritten columns.handwritten.generation.faithfulness_pre | 0.7230769230769231 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-352 | as-run handwritten columns.handwritten.generation.claim_retention | 0.7230769230769231 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-353 | as-run handwritten columns.handwritten.generation.citation_coverage | 1.0 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-354 | as-run handwritten columns.handwritten.generation.xbrl_contradiction_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-355 | as-run handwritten columns.handwritten.abstention.false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-356 | as-run handwritten columns.handwritten.abstention.over_abstention_rate | 0.4166666666666667 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-357 | as-run handwritten columns.handwritten.abstention.abstention_f1 | 0.8275862068965517 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-358 | as-run aggregate columns.aggregate.sufficiency@10 | 0.7590361445783133 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-359 | as-run aggregate columns.aggregate.cost_per_query | `cost n/a (dev backend)` | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-360 | as-run aggregate columns.aggregate.rerank_fell_back | 200 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-361 | as-run aggregate columns.aggregate.numeric.numeric_accuracy | 0.7209302325581395 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-362 | as-run aggregate columns.aggregate.generation.answer_rate | 0.6964285714285714 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-363 | as-run aggregate columns.aggregate.generation.faithfulness_pre | 0.8503937007874016 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-364 | as-run aggregate columns.aggregate.generation.claim_retention | 0.8503937007874016 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-365 | as-run aggregate columns.aggregate.generation.citation_coverage | 1.0 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-366 | as-run aggregate columns.aggregate.generation.xbrl_contradiction_rate | 0.008403361344537815 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-367 | as-run aggregate columns.aggregate.abstention.false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-368 | as-run aggregate columns.aggregate.abstention.over_abstention_rate | 0.2560240963855422 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-369 | as-run aggregate columns.aggregate.abstention.abstention_f1 | 0.5853658536585366 | development | `eval/runs/35b3efbbfd5d.json` | `2b4f9bb` |
| R-370 | judge aggregate eligible | 247 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-371 | judge aggregate judged | 247 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-372 | judge aggregate mean_score | 4.704453441295547 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-373 | judge aggregate normalized_mean | 0.9408906882591093 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-374 | judge aggregate share_at_least_4 | 0.9230769230769231 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-375 | judge handwritten eligible | 35 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-376 | judge handwritten judged | 35 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-377 | judge handwritten mean_score | 4.8 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-378 | judge handwritten normalized_mean | 0.96 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-379 | judge handwritten share_at_least_4 | 0.9428571428571428 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-380 | judge llm_seeded eligible | 60 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-381 | judge llm_seeded judged | 60 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-382 | judge llm_seeded mean_score | 4.683333333333334 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-383 | judge llm_seeded normalized_mean | 0.9366666666666666 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-384 | judge llm_seeded share_at_least_4 | 0.9166666666666666 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-385 | judge xbrl_auto eligible | 152 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-386 | judge xbrl_auto judged | 152 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-387 | judge xbrl_auto mean_score | 4.690789473684211 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-388 | judge xbrl_auto normalized_mean | 0.9381578947368421 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-389 | judge xbrl_auto share_at_least_4 | 0.9210526315789473 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-390 | judge adversarial eligible | 8 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-391 | judge adversarial judged | 8 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-392 | judge adversarial mean_score | 4.625 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-393 | judge adversarial normalized_mean | 0.925 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-394 | judge adversarial share_at_least_4 | 0.875 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-395 | judge comparison eligible | 41 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-396 | judge comparison judged | 41 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-397 | judge comparison mean_score | 4.878048780487805 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-398 | judge comparison normalized_mean | 0.975609756097561 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-399 | judge comparison share_at_least_4 | 0.975609756097561 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-400 | judge natural_phrasing eligible | 11 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-401 | judge natural_phrasing judged | 11 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-402 | judge natural_phrasing mean_score | 4.7272727272727275 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-403 | judge natural_phrasing normalized_mean | 0.9454545454545454 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-404 | judge natural_phrasing share_at_least_4 | 0.9090909090909091 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-405 | judge synthesis eligible | 27 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-406 | judge synthesis judged | 27 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-407 | judge synthesis mean_score | 4.777777777777778 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-408 | judge synthesis normalized_mean | 0.9555555555555556 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-409 | judge synthesis share_at_least_4 | 0.9629629629629629 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-410 | judge table eligible | 33 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-411 | judge table judged | 33 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-412 | judge table mean_score | 4.606060606060606 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-413 | judge table normalized_mean | 0.9212121212121213 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-414 | judge table share_at_least_4 | 0.8787878787878788 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-415 | judge unanswerable eligible | 0 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-416 | judge unanswerable judged | 0 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-417 | judge unanswerable mean_score | null | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-418 | judge unanswerable normalized_mean | null | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-419 | judge unanswerable share_at_least_4 | null | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-420 | judge xbrl_numeric eligible | 127 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-421 | judge xbrl_numeric judged | 127 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-422 | judge xbrl_numeric mean_score | 4.661417322834645 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-423 | judge xbrl_numeric normalized_mean | 0.9322834645669291 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-424 | judge xbrl_numeric share_at_least_4 | 0.9133858267716536 | development | `eval/runs/35b3efbbfd5d.judged.json` | `2b906a8` |
| R-425 | rescore-0.0010178742231801152.json xbrl_auto faithfulness_pre | 0.9385964912280702 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-426 | rescore-0.0010178742231801152.json xbrl_auto claim_retention | 0.9385964912280702 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-427 | rescore-0.0010178742231801152.json xbrl_auto verdict counts PASS/PARTIAL/ABSTAIN | `151/1/48` | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-428 | rescore-0.0010178742231801152.json xbrl_auto false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-429 | rescore-0.0010178742231801152.json xbrl_auto over_abstention_rate | 0.24 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-430 | rescore-0.0010178742231801152.json xbrl_auto abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-431 | rescore-0.0010178742231801152.json llm_seeded faithfulness_pre | 0.8266666666666667 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-432 | rescore-0.0010178742231801152.json llm_seeded claim_retention | 0.8266666666666667 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-433 | rescore-0.0010178742231801152.json llm_seeded verdict counts PASS/PARTIAL/ABSTAIN | `49/11/12` | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-434 | rescore-0.0010178742231801152.json llm_seeded false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-435 | rescore-0.0010178742231801152.json llm_seeded over_abstention_rate | 0.16666666666666666 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-436 | rescore-0.0010178742231801152.json llm_seeded abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-437 | rescore-0.0010178742231801152.json handwritten faithfulness_pre | 0.7230769230769231 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-438 | rescore-0.0010178742231801152.json handwritten claim_retention | 0.7230769230769231 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-439 | rescore-0.0010178742231801152.json handwritten verdict counts PASS/PARTIAL/ABSTAIN | `23/12/85` | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-440 | rescore-0.0010178742231801152.json handwritten false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-441 | rescore-0.0010178742231801152.json handwritten over_abstention_rate | 0.4166666666666667 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-442 | rescore-0.0010178742231801152.json handwritten abstention_f1 | 0.8275862068965517 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-443 | rescore-0.0010178742231801152.json aggregate faithfulness_pre | 0.8503937007874016 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-444 | rescore-0.0010178742231801152.json aggregate claim_retention | 0.8503937007874016 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-445 | rescore-0.0010178742231801152.json aggregate verdict counts PASS/PARTIAL/ABSTAIN | `223/24/145` | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-446 | rescore-0.0010178742231801152.json aggregate false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-447 | rescore-0.0010178742231801152.json aggregate over_abstention_rate | 0.2560240963855422 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-448 | rescore-0.0010178742231801152.json aggregate abstention_f1 | 0.5853658536585366 | development | `eval/runs/35b3efbbfd5d.rescore-0.0010178742231801152.json` | `52318c7` |
| R-449 | rescore-0.5.json xbrl_auto faithfulness_pre | 0.9298245614035088 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-450 | rescore-0.5.json xbrl_auto claim_retention | 0.9298245614035088 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-451 | rescore-0.5.json xbrl_auto verdict counts PASS/PARTIAL/ABSTAIN | `149/2/49` | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-452 | rescore-0.5.json xbrl_auto false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-453 | rescore-0.5.json xbrl_auto over_abstention_rate | 0.245 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-454 | rescore-0.5.json xbrl_auto abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-455 | rescore-0.5.json llm_seeded faithfulness_pre | 0.52 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-456 | rescore-0.5.json llm_seeded claim_retention | 0.52 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-457 | rescore-0.5.json llm_seeded verdict counts PASS/PARTIAL/ABSTAIN | `36/6/30` | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-458 | rescore-0.5.json llm_seeded false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-459 | rescore-0.5.json llm_seeded over_abstention_rate | 0.4166666666666667 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-460 | rescore-0.5.json llm_seeded abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-461 | rescore-0.5.json handwritten faithfulness_pre | 0.4846153846153846 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-462 | rescore-0.5.json handwritten claim_retention | 0.4846153846153846 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-463 | rescore-0.5.json handwritten verdict counts PASS/PARTIAL/ABSTAIN | `17/8/95` | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-464 | rescore-0.5.json handwritten false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-465 | rescore-0.5.json handwritten over_abstention_rate | 0.5833333333333334 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-466 | rescore-0.5.json handwritten abstention_f1 | 0.7741935483870968 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-467 | rescore-0.5.json aggregate faithfulness_pre | 0.6948818897637795 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-468 | rescore-0.5.json aggregate claim_retention | 0.6948818897637795 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-469 | rescore-0.5.json aggregate verdict counts PASS/PARTIAL/ABSTAIN | `202/16/174` | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-470 | rescore-0.5.json aggregate false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-471 | rescore-0.5.json aggregate over_abstention_rate | 0.3433734939759036 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-472 | rescore-0.5.json aggregate abstention_f1 | 0.5128205128205129 | development | `eval/runs/35b3efbbfd5d.rescore-0.5.json` | `52318c7` |
| R-473 | rescore-0.7.json xbrl_auto faithfulness_pre | 0.9298245614035088 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-474 | rescore-0.7.json xbrl_auto claim_retention | 0.9298245614035088 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-475 | rescore-0.7.json xbrl_auto verdict counts PASS/PARTIAL/ABSTAIN | `149/2/49` | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-476 | rescore-0.7.json xbrl_auto false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-477 | rescore-0.7.json xbrl_auto over_abstention_rate | 0.245 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-478 | rescore-0.7.json xbrl_auto abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-479 | rescore-0.7.json llm_seeded faithfulness_pre | 0.4866666666666667 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-480 | rescore-0.7.json llm_seeded claim_retention | 0.4866666666666667 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-481 | rescore-0.7.json llm_seeded verdict counts PASS/PARTIAL/ABSTAIN | `35/5/32` | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-482 | rescore-0.7.json llm_seeded false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-483 | rescore-0.7.json llm_seeded over_abstention_rate | 0.4444444444444444 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-484 | rescore-0.7.json llm_seeded abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-485 | rescore-0.7.json handwritten faithfulness_pre | 0.4846153846153846 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-486 | rescore-0.7.json handwritten claim_retention | 0.4846153846153846 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-487 | rescore-0.7.json handwritten verdict counts PASS/PARTIAL/ABSTAIN | `17/8/95` | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-488 | rescore-0.7.json handwritten false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-489 | rescore-0.7.json handwritten over_abstention_rate | 0.5833333333333334 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-490 | rescore-0.7.json handwritten abstention_f1 | 0.7741935483870968 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-491 | rescore-0.7.json aggregate faithfulness_pre | 0.6850393700787402 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-492 | rescore-0.7.json aggregate claim_retention | 0.6850393700787402 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-493 | rescore-0.7.json aggregate verdict counts PASS/PARTIAL/ABSTAIN | `201/15/176` | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-494 | rescore-0.7.json aggregate false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-495 | rescore-0.7.json aggregate over_abstention_rate | 0.3493975903614458 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-496 | rescore-0.7.json aggregate abstention_f1 | 0.5084745762711864 | development | `eval/runs/35b3efbbfd5d.rescore-0.7.json` | `52318c7` |
| R-497 | rescore-0.85.json xbrl_auto faithfulness_pre | 0.9298245614035088 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-498 | rescore-0.85.json xbrl_auto claim_retention | 0.9298245614035088 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-499 | rescore-0.85.json xbrl_auto verdict counts PASS/PARTIAL/ABSTAIN | `149/2/49` | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-500 | rescore-0.85.json xbrl_auto false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-501 | rescore-0.85.json xbrl_auto over_abstention_rate | 0.245 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-502 | rescore-0.85.json xbrl_auto abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-503 | rescore-0.85.json llm_seeded faithfulness_pre | 0.4866666666666667 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-504 | rescore-0.85.json llm_seeded claim_retention | 0.4866666666666667 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-505 | rescore-0.85.json llm_seeded verdict counts PASS/PARTIAL/ABSTAIN | `35/5/32` | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-506 | rescore-0.85.json llm_seeded false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-507 | rescore-0.85.json llm_seeded over_abstention_rate | 0.4444444444444444 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-508 | rescore-0.85.json llm_seeded abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-509 | rescore-0.85.json handwritten faithfulness_pre | 0.46923076923076923 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-510 | rescore-0.85.json handwritten claim_retention | 0.46923076923076923 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-511 | rescore-0.85.json handwritten verdict counts PASS/PARTIAL/ABSTAIN | `17/8/95` | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-512 | rescore-0.85.json handwritten false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-513 | rescore-0.85.json handwritten over_abstention_rate | 0.5833333333333334 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-514 | rescore-0.85.json handwritten abstention_f1 | 0.7741935483870968 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-515 | rescore-0.85.json aggregate faithfulness_pre | 0.6811023622047244 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-516 | rescore-0.85.json aggregate claim_retention | 0.6811023622047244 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-517 | rescore-0.85.json aggregate verdict counts PASS/PARTIAL/ABSTAIN | `201/15/176` | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-518 | rescore-0.85.json aggregate false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-519 | rescore-0.85.json aggregate over_abstention_rate | 0.3493975903614458 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-520 | rescore-0.85.json aggregate abstention_f1 | 0.5084745762711864 | development | `eval/runs/35b3efbbfd5d.rescore-0.85.json` | `52318c7` |
| R-521 | reverify-xbrl_off.json xbrl_auto faithfulness_pre | 0.9517543859649122 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-522 | reverify-xbrl_off.json xbrl_auto claim_retention | 0.9517543859649122 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-523 | reverify-xbrl_off.json xbrl_auto verdict counts PASS/PARTIAL/ABSTAIN | `154/1/45` | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-524 | reverify-xbrl_off.json xbrl_auto false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-525 | reverify-xbrl_off.json xbrl_auto over_abstention_rate | 0.225 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-526 | reverify-xbrl_off.json xbrl_auto abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-527 | reverify-xbrl_off.json llm_seeded faithfulness_pre | 0.8266666666666667 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-528 | reverify-xbrl_off.json llm_seeded claim_retention | 0.8266666666666667 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-529 | reverify-xbrl_off.json llm_seeded verdict counts PASS/PARTIAL/ABSTAIN | `49/11/12` | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-530 | reverify-xbrl_off.json llm_seeded false_answer_rate | null | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-531 | reverify-xbrl_off.json llm_seeded over_abstention_rate | 0.16666666666666666 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-532 | reverify-xbrl_off.json llm_seeded abstention_f1 | null | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-533 | reverify-xbrl_off.json handwritten faithfulness_pre | 0.7230769230769231 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-534 | reverify-xbrl_off.json handwritten claim_retention | 0.7230769230769231 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-535 | reverify-xbrl_off.json handwritten verdict counts PASS/PARTIAL/ABSTAIN | `23/12/85` | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-536 | reverify-xbrl_off.json handwritten false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-537 | reverify-xbrl_off.json handwritten over_abstention_rate | 0.4166666666666667 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-538 | reverify-xbrl_off.json handwritten abstention_f1 | 0.8275862068965517 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-539 | reverify-xbrl_off.json aggregate faithfulness_pre | 0.8562992125984252 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-540 | reverify-xbrl_off.json aggregate claim_retention | 0.8562992125984252 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-541 | reverify-xbrl_off.json aggregate verdict counts PASS/PARTIAL/ABSTAIN | `226/24/142` | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-542 | reverify-xbrl_off.json aggregate false_answer_rate | 0.0 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-543 | reverify-xbrl_off.json aggregate over_abstention_rate | 0.2469879518072289 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |
| R-544 | reverify-xbrl_off.json aggregate abstention_f1 | 0.5940594059405941 | development | `eval/runs/35b3efbbfd5d.reverify-xbrl_off.json` | `52318c7` |

## 2026-11-26 — OWNER DECISION: single-chunk prose support fallback

The owner directed `verification.prose_check: llm_judge` as the served default,
retaining `nli` as a configurable historical comparator. Each cited passage is
judged independently; citation validity and entity match remain mandatory, and
figure verification remains unchanged. This is a development decision, not a
new gated baseline or a change to the NLI threshold or gold data.

The fresh single-passage check of the 40 labelled pairs in
`eval/nli/support_judge_v1.json` produced TP 33, TN 6, FP 1, FN 0, zero errors,
accuracy 0.975 and Cohen's κ 0.9083. All 40 are seeded prose, with only seven
negative labels, so this is a narrow validation. A pre-existing untracked blind
review file names the same model and matches all 40 recorded labels; the
independence of the labels from that prior model review cannot be established
from these artifacts alone. The new calls received only the claim and one
passage, not the labels.

The derived development replay
`eval/runs/35b3efbbfd5d.reverify-support_judge_v1.json` used the corpus whose
text hash matched the source run, made 165 support calls with zero errors and
preserved all 381 stored figure checks. No generation, retrieval or reranking
was repeated. Original run and dataset hashes are recorded in the derived file.
The per-source pre-verification faithfulness and claim retention were:

| Source | NLI as run | Support judge replay |
|---|---:|---:|
| aggregate | 0.8504 | 0.9311 |
| xbrl_auto | 0.9386 | 0.9342 |
| llm_seeded | 0.8267 | 0.9533 |
| handwritten | 0.7231 | 0.9000 |

Among 30 natural-phrasing items, abstentions changed from 19 to 11. This is an
observed verdict change, not a correctness improvement: support/faithfulness is
not answer correctness, and the newly retained answers have not been separately
scored for correctness. The handwritten slice is model-drafted (F-103), and the
development run cannot pass the CI gate.

## Golden v1 final development run 13fc0fa4eb72

Development only; 142 timeout fallbacks make the run hardware-dependent. `null` is not zero.

| id | what was measured | value | kind | run id or artifact | commit |
|---|---|---|---|---|---|
| R-545 | xbrl_auto columns.xbrl_auto.sufficiency@10 | 0.71 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-546 | xbrl_auto columns.xbrl_auto.cost_per_query | `cost n/a (dev backend)` | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-547 | xbrl_auto columns.xbrl_auto.rerank_fell_back | 67 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-548 | xbrl_auto columns.xbrl_auto.numeric.numeric_accuracy | 0.66 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-549 | xbrl_auto columns.xbrl_auto.generation.answer_rate | 0.81 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-550 | xbrl_auto columns.xbrl_auto.generation.faithfulness_pre | 0.8991596638655462 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-551 | xbrl_auto columns.xbrl_auto.generation.claim_retention | 0.8991596638655462 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-552 | xbrl_auto columns.xbrl_auto.generation.citation_coverage | 1.0 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-553 | xbrl_auto columns.xbrl_auto.generation.xbrl_contradiction_rate | 0.01293103448275862 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-554 | xbrl_auto columns.xbrl_auto.abstention.false_answer_rate | null | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-555 | xbrl_auto columns.xbrl_auto.abstention.over_abstention_rate | 0.26 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-556 | xbrl_auto columns.xbrl_auto.abstention.abstention_f1 | null | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-557 | llm_seeded columns.llm_seeded.sufficiency@10 | 0.9583333333333334 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-558 | llm_seeded columns.llm_seeded.cost_per_query | `cost n/a (dev backend)` | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-559 | llm_seeded columns.llm_seeded.rerank_fell_back | 47 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-560 | llm_seeded columns.llm_seeded.numeric.numeric_accuracy | 0.8421052631578947 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-561 | llm_seeded columns.llm_seeded.generation.answer_rate | 0.9583333333333334 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-562 | llm_seeded columns.llm_seeded.generation.faithfulness_pre | 0.9370629370629371 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-563 | llm_seeded columns.llm_seeded.generation.claim_retention | 0.9370629370629371 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-564 | llm_seeded columns.llm_seeded.generation.citation_coverage | 1.0 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-565 | llm_seeded columns.llm_seeded.generation.xbrl_contradiction_rate | 0.0 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-566 | llm_seeded columns.llm_seeded.abstention.false_answer_rate | null | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-567 | llm_seeded columns.llm_seeded.abstention.over_abstention_rate | 0.08333333333333333 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-568 | llm_seeded columns.llm_seeded.abstention.abstention_f1 | null | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-569 | handwritten columns.handwritten.sufficiency@10 | 0.7166666666666667 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-570 | handwritten columns.handwritten.cost_per_query | `cost n/a (dev backend)` | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-571 | handwritten columns.handwritten.rerank_fell_back | 28 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-572 | handwritten columns.handwritten.numeric.numeric_accuracy | 0.8 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-573 | handwritten columns.handwritten.generation.answer_rate | 0.35833333333333334 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-574 | handwritten columns.handwritten.generation.faithfulness_pre | 0.9032258064516129 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-575 | handwritten columns.handwritten.generation.claim_retention | 0.9032258064516129 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-576 | handwritten columns.handwritten.generation.citation_coverage | 1.0 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-577 | handwritten columns.handwritten.generation.xbrl_contradiction_rate | 0.0 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-578 | handwritten columns.handwritten.abstention.false_answer_rate | 0.0 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-579 | handwritten columns.handwritten.abstention.over_abstention_rate | 0.3 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-580 | handwritten columns.handwritten.abstention.abstention_f1 | 0.8695652173913044 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-581 | aggregate columns.aggregate.sufficiency@10 | 0.7650602409638554 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-582 | aggregate columns.aggregate.cost_per_query | `cost n/a (dev backend)` | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-583 | aggregate columns.aggregate.rerank_fell_back | 142 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-584 | aggregate columns.aggregate.numeric.numeric_accuracy | 0.6976744186046512 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-585 | aggregate columns.aggregate.generation.answer_rate | 0.6989795918367347 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-586 | aggregate columns.aggregate.generation.faithfulness_pre | 0.9108910891089109 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-587 | aggregate columns.aggregate.generation.claim_retention | 0.9108910891089109 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-588 | aggregate columns.aggregate.generation.citation_coverage | 1.0 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-589 | aggregate columns.aggregate.generation.xbrl_contradiction_rate | 0.008403361344537815 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-590 | aggregate columns.aggregate.abstention.false_answer_rate | 0.0 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-591 | aggregate columns.aggregate.abstention.over_abstention_rate | 0.2289156626506024 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-592 | aggregate columns.aggregate.abstention.abstention_f1 | 0.6122448979591837 | development | `eval/runs/13fc0fa4eb72.json` | `32b04c8` |
| R-593 | answer_correctness.aggregate.aggregate.eligible | 256 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-594 | answer_correctness.aggregate.aggregate.judged | 256 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-595 | answer_correctness.aggregate.aggregate.mean_score | 4.68359375 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-596 | answer_correctness.aggregate.aggregate.normalized_mean | 0.93671875 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-597 | answer_correctness.aggregate.aggregate.share_at_least_4 | 0.92578125 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-598 | answer_correctness.by_source.handwritten.eligible | 42 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-599 | answer_correctness.by_source.handwritten.judged | 42 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-600 | answer_correctness.by_source.handwritten.mean_score | 4.666666666666667 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-601 | answer_correctness.by_source.handwritten.normalized_mean | 0.9333333333333333 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-602 | answer_correctness.by_source.handwritten.share_at_least_4 | 0.9047619047619048 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-603 | answer_correctness.by_source.llm_seeded.eligible | 66 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-604 | answer_correctness.by_source.llm_seeded.judged | 66 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-605 | answer_correctness.by_source.llm_seeded.mean_score | 4.742424242424242 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-606 | answer_correctness.by_source.llm_seeded.normalized_mean | 0.9484848484848485 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-607 | answer_correctness.by_source.llm_seeded.share_at_least_4 | 0.9393939393939394 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-608 | answer_correctness.by_source.xbrl_auto.eligible | 148 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-609 | answer_correctness.by_source.xbrl_auto.judged | 148 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-610 | answer_correctness.by_source.xbrl_auto.mean_score | 4.662162162162162 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-611 | answer_correctness.by_source.xbrl_auto.normalized_mean | 0.9324324324324325 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-612 | answer_correctness.by_source.xbrl_auto.share_at_least_4 | 0.9256756756756757 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-613 | answer_correctness.by_type.adversarial.eligible | 6 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-614 | answer_correctness.by_type.adversarial.judged | 6 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-615 | answer_correctness.by_type.adversarial.mean_score | 4.833333333333333 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-616 | answer_correctness.by_type.adversarial.normalized_mean | 0.9666666666666667 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-617 | answer_correctness.by_type.adversarial.share_at_least_4 | 1.0 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-618 | answer_correctness.by_type.comparison.eligible | 43 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-619 | answer_correctness.by_type.comparison.judged | 43 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-620 | answer_correctness.by_type.comparison.mean_score | 4.813953488372093 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-621 | answer_correctness.by_type.comparison.normalized_mean | 0.9627906976744186 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-622 | answer_correctness.by_type.comparison.share_at_least_4 | 0.9534883720930233 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-623 | answer_correctness.by_type.natural_phrasing.eligible | 21 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-624 | answer_correctness.by_type.natural_phrasing.judged | 21 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-625 | answer_correctness.by_type.natural_phrasing.mean_score | 4.380952380952381 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-626 | answer_correctness.by_type.natural_phrasing.normalized_mean | 0.8761904761904762 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-627 | answer_correctness.by_type.natural_phrasing.share_at_least_4 | 0.8095238095238095 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-628 | answer_correctness.by_type.synthesis.eligible | 32 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-629 | answer_correctness.by_type.synthesis.judged | 32 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-630 | answer_correctness.by_type.synthesis.mean_score | 4.84375 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-631 | answer_correctness.by_type.synthesis.normalized_mean | 0.96875 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-632 | answer_correctness.by_type.synthesis.share_at_least_4 | 1.0 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-633 | answer_correctness.by_type.table.eligible | 34 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-634 | answer_correctness.by_type.table.judged | 34 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-635 | answer_correctness.by_type.table.mean_score | 4.647058823529412 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-636 | answer_correctness.by_type.table.normalized_mean | 0.9294117647058824 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-637 | answer_correctness.by_type.table.share_at_least_4 | 0.8823529411764706 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-638 | answer_correctness.by_type.unanswerable.eligible | 0 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-639 | answer_correctness.by_type.unanswerable.judged | 0 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-640 | answer_correctness.by_type.unanswerable.mean_score | null | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-641 | answer_correctness.by_type.unanswerable.normalized_mean | null | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-642 | answer_correctness.by_type.unanswerable.share_at_least_4 | null | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-643 | answer_correctness.by_type.xbrl_numeric.eligible | 120 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-644 | answer_correctness.by_type.xbrl_numeric.judged | 120 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-645 | answer_correctness.by_type.xbrl_numeric.mean_score | 4.65 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-646 | answer_correctness.by_type.xbrl_numeric.normalized_mean | 0.93 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
| R-647 | answer_correctness.by_type.xbrl_numeric.share_at_least_4 | 0.925 | development | `eval/runs/13fc0fa4eb72.judged.json` | `4ccf2ad` |
