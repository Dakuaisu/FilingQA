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
