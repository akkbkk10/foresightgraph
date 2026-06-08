# Golden Set Candidate Review Template v0.1

## Purpose
This Markdown-first, human-reviewable template supports future Golden Set candidate review.
It does not add new Golden Set records.
Use this template to review candidate items before any separately approved expansion PR.

## Candidate Metadata
Record candidate metadata before review:
- candidate_id:
- item_type:
- proposed source_ids:
- proposed evidence_ids:
- review status:
- reviewer notes:
- reviewer name:
- review date:

## Source and Locator Review
For each candidate, record the source and the locator needed for later verification.
Review whether the source is identifiable, the locator is specific, and the citation path is reproducible.
If the source or locator is weak, incomplete, or missing, the candidate is not ready.

## Claim and Wording Review
Classify each candidate statement as one of: fact, claim, interpretation, or vendor/provider claim.
Require conservative wording for every candidate.
Vendor/provider claim language must remain claim language unless separately reproduced by the project.
Benchmark overclaims are forbidden unless separately reproduced by the project.
Preserve the `nvidia_ai_004` conservative guardrail when wording touches deployability, scalability, or operational implications.

## Evidence Traceability
Confirm that each candidate has clear links between source, locator, evidence, and proposed output.
Traceability must be specific enough for later regression checks and reviewer audit.
If evidence linkage is unclear, contradictory, or incomplete, the candidate must not be approved.

## Uncertainty and Contradiction Review
Add uncertainty notes when evidence is incomplete, limited, or unresolved.
Add contradiction notes when sources conflict, scope is unclear, or wording could overstate the evidence.
When relevant, reviewer notes must explain how uncertainty and contradiction are handled conservatively.

## Conservative Output Boundary
Keep outputs bounded to review, traceability, and conservative wording.
Do not convert traceable material into stronger factual or operational conclusions without separately reproduced project evidence.
The template is Markdown-first and human-reviewable so reviewers can inspect wording directly before any future record change.

## Forbidden Outputs
This template does not authorize Golden Set record creation.
Investment/trading outputs are forbidden.
Buy/Sell/Hold outputs are forbidden.
Price targets are forbidden.
Broker integration is forbidden.
Investment advice is forbidden.
Runtime provider integration is forbidden.
Provider SDK changes are forbidden.

## Reviewer Decision
Reviewer decision:
- APPROVE_FOR_FUTURE_SMALL_PR
- NEEDS_CITATION_FIX
- NEEDS_CONSERVATIVE_WORDING_FIX
- NEEDS_UNCERTAINTY_NOTE
- NEEDS_CONTRADICTION_NOTE
- REJECT

Reviewers should approve only when source, locator, item_type, review status, reviewer notes, and conservative wording are all present and adequate.

## Done Criteria
The review is documented in Markdown.
The template remains human-reviewable.
The template states that it does not add new Golden Set records.
The review captures source, locator, item_type, review status, reviewer notes, conservative wording, uncertainty, contradiction, and the `nvidia_ai_004` guardrail.
Forbidden outputs remain out of scope for this review workflow.
