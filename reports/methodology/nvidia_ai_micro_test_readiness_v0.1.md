# NVIDIA/AI Micro Test Readiness Checkpoint v0.1

## Scope
This checkpoint summarizes the completed 3-source NVIDIA/AI micro test, documenting the workflow validation and lessons learned from manually processing real vendor sources.

## Sources covered
- real_nvidia_ai_001 - NVIDIA Blackwell Architecture
- real_nvidia_ai_003 - NVIDIA NIM Microservices
- real_nvidia_ai_004 - NVIDIA NeMo

## Workflow validated
Source Pack -> Manual Locator -> Short Excerpt -> Evidence Draft -> Claim Candidate -> Human Review -> Micro-Test Report

## What was proven
- The manual evidence-first workflow can be repeated across 3 real vendor sources.
- Short manually provided excerpts can be connected to evidence placeholders.
- Conservative claim candidates can be created from excerpts.
- Vendor claims can remain clearly marked as manufacturer_claim, not_reproduced, and reviewed_vendor_claim_only.
- Human review can explicitly limit conclusions.

## What was not proven
- no independent technical truth verification
- no benchmark performance
- no commercial traction
- no provider decision
- no investment thesis
- no trading or Buy/Sell/Hold conclusion
- no automated extraction quality

## Lessons learned
- Source-bound claims must stay narrow.
- Vendor-source statements must not become project facts.
- Short excerpts and locators are enough for controlled first evidence drafts.
- Review labels are essential.
- Cline must not browse, infer missing facts, or expand scope during real-source work.

## Readiness assessment
Status: READY_FOR_NEXT_MANUAL_REAL_TEST_STEP

### Meaning
Ready for a small next manual step, not for automation.

### Allowed next steps
- create a mini real golden set from the existing 3-source micro test
- add one more manually reviewed source only if needed
- convert reviewed worksheet items into structured draft records only after separate review

### Not allowed yet
- live scraping
- automatic extraction
- provider SDK/runtime integration
- Vector DB
- GraphRAG
- RAGAS automation
- benchmark claims
- investment interpretation

## Recommended next small block
Create a mini real golden-set draft from the 3 reviewed NVIDIA/AI micro-test sources, using only already reviewed excerpts and claim candidates.