# Golden Set Expansion Protocol v0.1

## Purpose
This protocol prepares future Golden Set expansion in this repository.
It defines a conservative methodology and review boundary for future expansion work.
It does not add new Golden Set records.

## Current Baseline
The current baseline in the repository is `evals/golden_sets/real_nvidia_ai_micro_v0.1.jsonl`.
That baseline is treated as a small repository baseline for structural and methodology checks, not as a benchmark-quality dataset.
Existing validation already includes pytest CI, real NVIDIA micro golden set structural checks, and conservative `nvidia_ai_004` consistency checks.

## Expansion Principles
Future expansion must happen in small PRs.
Each expansion PR must stay limited to a clearly stated goal, a clearly bounded review scope, and explicit validation steps.
Each expansion PR must include tests.
Future expansion must preserve contradiction handling, uncertainty handling, and evidence traceability.
This protocol supports future expansion work without changing the current baseline records.

## Candidate Item Requirements
Every future item must define a clear item type.
Every future item must include source and evidence traceability.
Every future item must include conservative wording, review status, and explicit reviewer notes.
Every future item must distinguish whether it is a question item, claim item, or another separately approved item class.
Every future item must stay reviewable in a small PR.

## Source and Locator Requirements
Every future item must identify at least one source and at least one locator that allows a reviewer to find the cited material again.
The source record, locator, and evidence linkage must be clear enough for review and regression testing.
If a source or locator is incomplete, the item must not be added.
Traceability must remain specific enough to support contradiction review and uncertainty review.

## Conservative Wording Requirements
Provider or vendor statements must remain classified as claims unless reproduced by the project.
Conservative wording must avoid converting traceable claims into verified facts.
If evidence is mixed, incomplete, or contradicted, the wording must preserve the uncertainty directly in the item and review notes.
The conservative treatment of `nvidia_ai_004` must be preserved as a repository guardrail.
No future wording may turn provider or vendor claims into benchmark claims, operational proof, or investment/trading outputs.

## Required Review Fields
Each future item must include item_id, item_type, source_ids, evidence_ids, required_citations, review status, and reviewer notes.
Each future item must also record uncertainty notes and contradiction notes when relevant.
Review status must remain explicit so reviewers can distinguish draft material from separately approved states.

## Validation Requirements
Each expansion PR must include tests that verify the new methodology requirements and the relevant record-level guardrails.
Validation must check required headings, required review fields, traceability markers, and conservative wording markers.
Validation must also check that forbidden overclaim language is absent.
Any methodology update that changes the treatment of `nvidia_ai_004` requires explicit reviewer attention and matching tests.

## Forbidden Additions
This protocol does not permit new Golden Set records in this PR.
Investment/trading outputs are forbidden.
Runtime provider integration, provider SDKs, autonomous agents on real project files, GraphRAG, Vector DB work, and benchmark claims are out of scope unless separately approved.
This protocol does not authorize new factual claims about NVIDIA, providers, companies, markets, products, benchmarks, or partnerships.

## Suggested Next Batches
Suggested future batches should stay small and reviewable.
A future batch may add one tightly bounded group of candidate items with matching tests and methodology notes.
A future batch may refine contradiction handling and uncertainty handling for candidate items before any broader expansion.
A future batch may extend review templates or validation rules without changing the current baseline records.

## Done Criteria
This protocol file exists in the repository.
The protocol states that it prepares future Golden Set expansion.
The protocol states that it does not add new Golden Set records.
The protocol preserves conservative wording, source and locator requirements, review status requirements, and the `nvidia_ai_004` guardrail.
A pytest guardrail exists for this protocol.
