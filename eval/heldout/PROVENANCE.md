# Held-out v1 draft provenance

Assembled in AC, NT, BJ, PX batch order from `build/heldout-{ac,nt,bj,px}.jsonl`.
The 60 model-drafted items cover eight issuers: 25 financial numeric/comparison
items, 25 prose items, and 10 unanswerable items. Numeric items are XBRL-style
questions grounded in filing text; inline XBRL tagging is not required and
these items are not represented as reconciled XBRL facts.

The batch authors checked the answers against live rebuild chunk text.
`build/heldout-validation.md` records a central check of all 60 items, all 51
distinct cited chunk IDs in that check, and the absence of the requested issuer
fiscal years for all ten negatives. The assembled inputs cite 52 distinct
chunks; all 52 were fetched read-only from the live rebuild for the worksheet.
The offline check using the pinned BGE embedding model
found zero cosine similarities strictly above 0.92 against 392 golden items,
283 candidate rows, or within the held-out draft. The maxima were respectively
0.9138839244842529, 0.8791563510894775, and 0.8964205980300903.

AC05 retains the corrected first-quarter SG&A change: $6,607 million to
$6,786 million, up $179 million, checked in both cited chunks. Each negative
has an explicit rationale. The review worksheet groups cited excerpts by
evidence set and leaves owner decisions blank. `source` is `heldout`, each
item is tagged `model_drafted`, and `reviewed_by_human` is false throughout.
This is a draft awaiting owner review, not a freeze or an evaluation result.
