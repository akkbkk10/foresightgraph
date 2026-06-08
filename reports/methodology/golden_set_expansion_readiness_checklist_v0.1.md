# Golden Set Expansion Readiness Checklist v0.1

## Purpose
This Markdown-first, human-reviewable readiness checklist defines when future Golden Set expansion may start.
It does not add new Golden Set records.
This checklist documents readiness only and remains distinct from actual Golden Set expansion.

## Methodology Files Required
The protocol, review template, intake log, and decision log must exist before future Golden Set expansion may start.
These methodology files must remain available in the repository as reviewable Markdown artifacts.
Readiness must stay compatible with small PRs and human review.

## Test Guardrails Required
Matching pytest guardrails must exist for the protocol, review template, intake log, and decision log.
Future readiness work must remain suitable for pytest validation before any candidate record work begins.
No JSONL changes are allowed in this checklist PR.

## Candidate Intake Readiness
Candidate intake readiness requires an intake log that can capture source scope, candidate scope, review status, and reviewer notes.
Readiness for intake must stay distinct from actual Golden Set expansion.
The intake process must remain narrow enough for small PRs and human review.

## Candidate Review Readiness
Candidate review readiness requires a review template that supports evidence traceability, review boundaries, and conservative handling.
Review readiness must preserve Markdown-first, human-reviewable workflow boundaries.
Pytest validation must remain part of the review process.

## Candidate Decision Readiness
Candidate decision readiness requires a decision log for accept/reject/defer handling and reviewer notes.
Decision readiness must keep candidate decisions separate from approved Golden Set records.
Decision readiness must remain compatible with small PRs and human review.

## Source and Locator Readiness
Source and locator readiness is required before candidate expansion may start.
Reviewers must be able to trace each future candidate to a clear source and usable locator.
If source or locator support is incomplete, expansion is not ready.

## Conservative Wording Readiness
Conservative wording readiness is required before candidate expansion may start.
Benchmark overclaims are forbidden unless separately reproduced by the project.
The `nvidia_ai_004` conservative guardrail must be preserved when wording touches deployment, scalability, operational implications, or capability framing.

## Uncertainty and Contradiction Readiness
Uncertainty and contradiction readiness is required before candidate expansion may start.
Reviewers must be prepared to document uncertainty and contradiction conservatively.
Readiness must keep uncertainty and contradiction handling explicit in human review.

## Forbidden Start Conditions
Do not start expansion when methodology files or pytest guardrails are missing.
Do not start expansion when source or locator readiness is incomplete.
Do not start expansion when conservative wording readiness is incomplete.
Do not start expansion when uncertainty and contradiction readiness is incomplete.
Investment/trading outputs are forbidden.
Buy/Sell/Hold outputs are forbidden.
Price targets are forbidden.
Broker integration is forbidden.
Investment advice is forbidden.
Runtime provider integration is forbidden.
Provider SDK changes are forbidden.

## Start Criteria for First Candidate Batch
The first candidate batch may start only when the protocol, review template, intake log, decision log, matching pytest guardrails, source readiness, locator readiness, conservative wording readiness, uncertainty readiness, contradiction readiness, small PRs, pytest validation, and human review are all in place.
This readiness checklist does not authorize actual Golden Set record changes by itself.
Any future batch must remain separate from approved Golden Set records until a later reviewed PR explicitly performs that work.

## Done Criteria
The readiness checklist is documented in Markdown.
The readiness checklist remains human-reviewable.
The readiness checklist states that it does not add new Golden Set records.
The readiness checklist requires the protocol, review template, intake log, decision log, pytest guardrails, source, locator, conservative wording, uncertainty, contradiction, small PRs, pytest validation, human review, and the `nvidia_ai_004` guardrail before expansion may start.
The readiness checklist keeps readiness separate from actual Golden Set expansion and keeps JSONL changes out of scope for this PR.
