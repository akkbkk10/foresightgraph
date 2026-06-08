# First Real Golden Set Candidate Batch Review v0.1

## Purpose
This is the first very small real Golden Set candidate batch for future review.
This is a candidate batch, not an approved Golden Set expansion.
It does not modify the approved baseline JSONL.
All records require human review before promotion.

## Batch Metadata
- batch_id: first_real_candidate_batch_v0.1
- candidate_count: 2
- reviewer: pending human review
- review status: candidate_only
- related small PRs: methodology/add-first-golden-set-candidate-batch

## Candidate Records Added
- candidate_nvidia_ai_001 derived from repository baseline source_id `real_nvidia_ai_001` and evidence_id `evidence_nvidia_blackwell_001`
- candidate_nvidia_ai_002 derived from repository baseline source_id `real_nvidia_ai_003` and evidence_id `evidence_nvidia_nim_001`

## Source and Locator Review
Each candidate record includes source_ids, evidence_ids, required_citations, a non-empty source field, and a non-empty locator field.
The source and locator values are derived from repository baseline identifiers already present in `evals/golden_sets/real_nvidia_ai_micro_v0.1.jsonl`.
No invented URLs, dates, source titles, or external locators were added.

## Conservative Wording Review
The candidate wording remains traceability-focused and candidate-only.
No benchmark claim is made.
The candidate batch does not claim production readiness.
The `nvidia_ai_004` conservative treatment remains protected.

## Uncertainty and Contradiction Review
Every candidate record includes non-empty uncertainty notes and contradiction notes.
No repository-level contradiction was identified for these two candidate records within the limited batch scope.
The records remain bounded to future human review before any promotion.

## Decision Boundary
This batch does not promote records to approved Golden Set status.
This batch does not modify `evals/golden_sets/real_nvidia_ai_micro_v0.1.jsonl`.
This batch only creates candidate records in a separate candidate JSONL file.

## Forbidden Outputs Check
No benchmark claim is made.
No investment/trading output is added.
No runtime provider integration is added.
No provider SDK change is added.

## Reviewer Notes
This batch stays intentionally tiny and reviewable.
Both candidate records preserve repository traceability markers and remain in `needs_review` status.

## Done Criteria
The candidate batch file exists separately from the approved baseline JSONL.
The review note states that this batch is candidate-only and requires human review.
The batch preserves conservative wording boundaries and keeps forbidden outputs out of scope.
