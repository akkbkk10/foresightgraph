# NVIDIA/AI Mini Golden Set Controlled Answer Generation Protocol v0.1

## Purpose

This protocol establishes a conservative controlled answer-generation framework for the 5-item NVIDIA/AI mini golden set. It defines the boundaries, rules, and evaluation criteria for generating answers that strictly use existing reviewed evidence and claim references, without conducting external research or making independent technical assessments.

## Input Dataset

The protocol uses the NVIDIA/AI mini golden set containing 5 items:
- 2 factual questions (nvidia_ai_001, nvidia_ai_002)
- 2 claim verification items (nvidia_ai_003, nvidia_ai_004) 
- 1 multi-source question (nvidia_ai_005)

All items are based on reviewed vendor claim candidates and remain in draft status. Each item contains:
- item_id: Unique identifier for the record
- item_type: Type of item (question, claim, assertion, etc.)
- source_ids: IDs of source documents or references
- evidence_ids: IDs of supporting evidence or citations
- question_or_claim: The actual question or claim being evaluated
- expected_answer_or_label: The expected answer or classification
- required_citations: Citations required for the answer
- review_status: Review status (draft, reviewed, approved, etc.)
- reviewer_notes: Notes from the review process

## Test Boundary

This protocol defines strict boundaries for answer generation:
- Only use information explicitly stated in reviewed sources and evidence
- Do not conduct external browsing or new source research
- Do not perform independent technical verification or benchmarking
- Do not treat vendor claims as independently verified project facts
- Do not include benchmark results, provider conclusions, commercial traction, investment content, or trading conclusions
- Do not make claims about model quality, performance metrics, or technical verification

## Allowed Inputs

The following inputs are permitted:
- The 5-item NVIDIA/AI mini golden set JSONL file
- All reviewed source documents and evidence referenced in the golden set
- The existing reviewed vendor claim candidates
- Required citation references for each item
- The item's question_or_claim field for context
- The expected_answer_or_label field for reference

## Forbidden Actions

The following actions are strictly prohibited:
- External browsing or web research
- Creation of new sources or evidence
- Independent technical verification or benchmarking
- Treatment of vendor claims as independently verified facts
- Introduction of benchmark results, provider decisions, or commercial assessments
- Addition of investment thesis, trading conclusions, or price targets
- Any content that goes beyond the scope of the reviewed evidence
- Making claims about model quality, performance metrics, or technical verification
- Including information not present in the reviewed sources

## Answer-Generation Rules

1. **Evidence-First Approach**: All answers must be traceable to cited evidence and reviewed sources
2. **Conservative Language**: Use only the exact wording and claims present in reviewed vendor sources
3. **No Overclaiming**: Answers may not exceed what is explicitly stated in the reviewed evidence
4. **Status Preservation**: Maintain the draft/manual-review-only status of all items
5. **Citation Requirements**: All answers must include required citations from the golden set
6. **No External Content**: No external facts, benchmarks, or opinions may be introduced
7. **Vendor Claim Classification**: All vendor claims must remain classified as manufacturer_claim, not_reproduced, reviewed_vendor_claim_only
8. **Traceability Focus**: Answers must clearly demonstrate how they connect to specific evidence

## Citation Requirements

- All answers must include required citations from the golden set
- Citations must be properly formatted and linked to evidence
- Each citation must be traceable to the specific evidence referenced
- No additional citations beyond those required in the golden set are allowed
- Citation format must be consistent with existing documentation standards

## Evaluation Rubric

Answers are evaluated using the following conservative statuses:
- **PASS_EVIDENCE_BOUND**: Answer is fully traceable to reviewed evidence and citations
- **NEEDS_CITATION_FIX**: Answer has correct content but missing or incomplete citations
- **FAIL_UNSUPPORTED_CLAIM**: Answer cannot be supported by the cited evidence
- **FAIL_OVERCLAIM**: Answer exceeds what is stated in the reviewed evidence
- **NOT_EVALUATED**: Item not evaluated due to process issues or incomplete information

## Per-Item Result Structure

Each item's answer must include:
- item_id: The unique identifier from the golden set
- answer: The generated response following the evidence-first approach
- citations: All required citations from the golden set
- evaluation_status: One of the conservative evaluation statuses
- reviewer_notes: Observations about the answer generation process

## Pass/Fail Criteria

**PASS**: Answer is fully traceable to reviewed evidence, includes all required citations, and does not overclaim
**FAIL**: Answer fails any of the following:
- Lacks required citations
- Contains unsupported claims
- Overclaims beyond stated evidence
- Introduces external content
- Treats vendor claims as independently verified facts

## Safety and Overclaim Checks

1. **Evidence Verification**: Every claim in the answer must be directly supported by cited evidence
2. **Overclaim Detection**: Answers must not expand beyond what is explicitly stated in vendor sources
3. **Status Compliance**: All answers must maintain the draft/manual-review-only classification
4. **Content Boundary**: No external facts, benchmarks, or opinions may be introduced
5. **Vendor Claim Integrity**: Vendor claims must remain classified as manufacturer_claim, not_reproduced, reviewed_vendor_claim_only

## What This Protocol Can Prove

This protocol can demonstrate:
- Traceability of answers to reviewed vendor claims and evidence
- Consistency in answer generation using only existing documentation
- Ability to maintain conservative evaluation boundaries
- Proper citation and source linking practices
- Adherence to the draft/manual-review-only status of all items

## What This Protocol Cannot Prove

This protocol cannot demonstrate:
- Technical truth or accuracy of vendor claims
- Independent technical verification or benchmark results
- Model quality or performance metrics
- Commercial traction or market impact
- Provider decisions or recommendations
- Investment thesis or trading conclusions
- Automated extraction quality or reliability
- Any claims beyond what is explicitly stated in reviewed vendor sources

## Recommended Next Small Step

After creating this controlled answer-generation protocol, the next step is to prepare a dry-run test using the existing golden set items. This will validate that the protocol can be applied consistently to generate answers that remain within the evidence boundaries while maintaining the conservative evaluation approach.