# Golden Set Candidate Batch Intake Log v0.1

## Purpose
This Markdown-first, human-reviewable intake log supports future Golden Set candidate batches.
It does not add new Golden Set records.
Use this log to record intake and review decisions before any separately approved Golden Set expansion PR.

## Batch Metadata
Record batch metadata before review:
- batch_id:
- candidate_count:
- source_count:
- reviewer:
- review status:
- reviewer notes:
- review date:
- related small PRs:

## Candidate Source Summary
Summarize the proposed source set for the batch.
Each batch review must check source quality, source scope, and whether each source has a usable locator.
If a source or locator is missing, incomplete, or unclear, the batch is not ready.

## Candidate Item Summary
Summarize the candidate items under review without converting them into approved Golden Set records.
Candidate intake must stay distinct from approved Golden Set records.
Record item_type coverage, candidate scope, and whether the batch remains small enough for small PRs.

## Review Boundary
This log records intake and decision support only.
It does not authorize JSONL changes in this template PR.
It does not authorize record creation, record edits, or factual expansion by itself.
Each future batch must remain limited, reviewable, and suitable for pytest validation in small PRs.

## Required Evidence Checks
Check that each candidate batch includes clear source references, usable locator details, and evidence traceability.
Check that the reviewer can map each candidate back to the cited source material.
If evidence links are incomplete, the batch must not advance.

## Required Conservative Wording Checks
Check that candidate wording remains conservative.
Benchmark overclaims are forbidden unless separately reproduced by the project.
Vendor/provider claim wording must remain claim wording unless separately reproduced by the project.
The `nvidia_ai_004` conservative guardrail must be preserved when wording touches deployment, scalability, or operational implications.

## Uncertainty and Contradiction Checks
Record uncertainty when evidence is incomplete, limited, or unresolved.
Record contradiction when sources conflict, scope is ambiguous, or wording risks overstating evidence.
Reviewer notes must explain how uncertainty and contradiction are handled conservatively when relevant.

## Forbidden Changes
JSONL changes are forbidden in this template PR.
Investment/trading outputs are forbidden.
Buy/Sell/Hold outputs are forbidden.
Price targets are forbidden.
Broker integration is forbidden.
Investment advice is forbidden.
Runtime provider integration is forbidden.
Provider SDK changes are forbidden.

## Reviewer Decision Log
Reviewer decision options:
- READY_FOR_FUTURE_SMALL_PR
- NEEDS_SOURCE_FIX
- NEEDS_LOCATOR_FIX
- NEEDS_CONSERVATIVE_WORDING_FIX
- NEEDS_UNCERTAINTY_NOTE
- NEEDS_CONTRADICTION_NOTE
- REJECT

## Follow-up Actions
List the next limited actions for the batch.
Follow-up actions should preserve small PRs, pytest validation, and human review before any future Golden Set record change.

## Done Criteria
The intake log is documented in Markdown.
The intake log remains human-reviewable.
The intake log states that it does not add new Golden Set records.
The intake log captures batch_id, candidate_count, source_count, review status, reviewer notes, source, locator, conservative wording, uncertainty, contradiction, and the `nvidia_ai_004` guardrail.
The intake log keeps candidate intake separate from approved Golden Set records and keeps JSONL changes out of scope for this PR.
