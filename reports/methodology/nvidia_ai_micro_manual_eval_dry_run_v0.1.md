# NVIDIA/AI Mini Golden Set Manual Evaluation Dry Run v0.1

## Scope
This dry run checks whether the 5 draft golden-set items are usable for a manual evidence-first evaluation. It does not test technical truth, benchmark performance, model quality, provider quality, commercial traction, or investment relevance.

## Input file
evals/golden_sets/real_nvidia_ai_micro_v0.1.jsonl

## Input records
List all 5 item IDs and item types:
- nvidia_ai_001: question, factual
- nvidia_ai_002: question, factual
- nvidia_ai_003: claim, claim verification
- nvidia_ai_004: claim, claim verification
- nvidia_ai_005: question, multi-source/multi-hop style

## Dry-run method
For each item, check only:
- required fields are present
- source IDs are approved
- evidence IDs are linked
- expected answer or expected label is present
- required citations are present
- item remains draft/manual-review only
- item preserves manufacturer_claim, not_reproduced, reviewed_vendor_claim_only
- no item requires external browsing or new source facts

## Per-item dry-run table
| item_id | item_type | traceability_status | answerability_status | safety_status | dry_run_result | notes |
|---------|-----------|-------------------|-------------------|-------------|--------------|-------|
| nvidia_ai_001 | question | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | Item is traceable to reviewed source and evidence, answerable from existing material |
| nvidia_ai_002 | question | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | Item is traceable to reviewed source and evidence, answerable from existing material |
| nvidia_ai_003 | claim | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | Item is traceable to reviewed sources and evidence, claim verification from existing material |
| nvidia_ai_004 | claim | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | Item is traceable to reviewed sources and evidence, claim verification from existing material |
| nvidia_ai_005 | question | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | PASS_TRACEABILITY_ONLY | Item is traceable to multiple reviewed sources and evidence, multi-source question answerable from existing material |

## Overall result
PASS_FOR_MANUAL_DRY_RUN_ONLY

## What this dry run proves
- The mini golden set can be manually inspected.
- Items are traceable to reviewed source, evidence, and claim references.
- The dataset can support a first conservative manual evaluation workflow.

## What this dry run does not prove
- no technical truth
- no independent verification
- no benchmark performance
- no model quality comparison
- no commercial traction
- no provider decision
- no investment thesis
- no trading conclusion
- no automated extraction quality

## Issues found
No blocking issues found.

## Recommended next small step
Create a manual evaluation result template for this golden set, or run a controlled answer-generation test only after a separate review.