# Golden Set Candidate Decision Log v0.1

## Purpose
This Markdown-first, human-reviewable decision log supports future Golden Set candidate accept/reject/defer decisions.
It does not add new Golden Set records.
Use this log to record candidate-level decisions before any separately approved Golden Set expansion PR.

## Decision Metadata
Record decision metadata before finalizing a review:
- decision_id:
- candidate_id:
- batch_id:
- reviewer:
- decision:
- review status:
- reviewer notes:
- review date:
- related small PRs:

## Candidate Reference
Reference the candidate under review without turning it into an approved Golden Set record.
Candidate decisions must stay distinct from approved Golden Set records.
Record the candidate scope, source coverage, and whether the review remains narrow enough for small PRs.

## Evidence Review Summary
Summarize the evidence review for the candidate.
A reviewer must complete source and locator review before accept_candidate.
If source support is incomplete or locator details are missing, accept_candidate is not allowed.
The summary must preserve evidence traceability and stay suitable for pytest validation.

## Conservative Wording Review
Summarize the conservative wording review before accept_candidate.
Benchmark overclaims are forbidden unless separately reproduced by the project.
The `nvidia_ai_004` conservative guardrail must be preserved when wording touches deployment, scalability, operational implications, or capability framing.

## Uncertainty and Contradiction Summary
Record uncertainty when evidence is incomplete, limited, or unresolved.
Record contradiction when sources conflict, scope is ambiguous, or wording risks overstating evidence.
Reviewer notes must explain how uncertainty and contradiction are handled conservatively when relevant.

## Decision Options
Allowed decisions:
- accept_candidate
- reject_candidate
- defer_candidate
- needs_more_evidence
Accept_candidate requires completed source and locator review, completed conservative wording review, and a documented uncertainty and contradiction summary.

## Rejection Reasons
Use this section when decision = reject_candidate.
Document why the candidate fails evidence quality, source, locator, scope, wording, or review-boundary requirements.

## Deferral Reasons
Use this section when decision = defer_candidate or decision = needs_more_evidence.
Document what is missing, what remains unclear, and what must be reviewed before the candidate can advance.

## Required Follow-up
List the next limited actions for the candidate review.
Follow-up must preserve small PRs, human review, and pytest validation before any future Golden Set record change.
This template PR forbids JSONL changes.

## Forbidden Decisions
This template PR does not authorize JSONL changes.
Investment/trading outputs are forbidden.
Buy/Sell/Hold outputs are forbidden.
Price targets are forbidden.
Broker integration is forbidden.
Investment advice is forbidden.
Runtime provider integration is forbidden.
Provider SDK changes are forbidden.
This template must not add factual claims, approved records, or benchmark claims unless separately reproduced by the project.

## Done Criteria
The decision log is documented in Markdown.
The decision log remains human-reviewable.
The decision log states that it does not add new Golden Set records.
The decision log captures decision_id, candidate_id, batch_id, reviewer, decision, review status, reviewer notes, source, locator, conservative wording, uncertainty, contradiction, and the `nvidia_ai_004` guardrail.
The decision log keeps candidate decisions separate from approved Golden Set records, preserves small PRs, requires pytest validation, and keeps JSONL changes out of scope for this PR.
