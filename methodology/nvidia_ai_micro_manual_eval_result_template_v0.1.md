# NVIDIA/AI Mini Golden Set Manual Evaluation Result Template v0.1

## Purpose
This template provides a structured format for documenting manual evaluation results of the 5-item NVIDIA/AI mini golden set. The evaluation focuses on traceability and evidence verification rather than technical truth, benchmark performance, or commercial assessment.

## Input Dataset
The evaluation uses the NVIDIA/AI mini golden set containing 5 items:
- 2 factual questions (nvidia_ai_001, nvidia_ai_002)
- 2 claim verification items (nvidia_ai_003, nvidia_ai_004) 
- 1 multi-source question (nvidia_ai_005)

All items are based on reviewed vendor claim candidates and remain in draft status.

## Evaluator Rules
1. **Conservative Approach**: Only use information explicitly stated in reviewed sources and evidence
2. **Traceability Focus**: Verify that answers can be traced back to documented sources
3. **Evidence Requirements**: All answers must be supported by cited evidence
4. **Status Preservation**: Maintain the draft/manual-review-only status of all items
5. **No External Research**: Do not conduct external browsing or new source research
6. **No Technical Verification**: Do not perform independent technical verification or benchmarking

## Allowed Result Statuses
- **PASS_WITH_REVIEWED_EVIDENCE**: Answer is traceable to reviewed evidence and supported by citations
- **NEEDS_MANUAL_REVIEW**: Additional review needed due to ambiguity or incomplete evidence
- **FAIL_MISSING_EVIDENCE**: Answer cannot be traced to required evidence or citations
- **NOT_EVALUATED**: Item not evaluated due to incomplete information or process issues

## Per-Item Result Template Table

| item_id | evaluation_status | evidence_citations | reviewer_notes |
|---------|-------------------|-------------------|----------------|
| nvidia_ai_001 |  |  |  |
| nvidia_ai_002 |  |  |  |
| nvidia_ai_003 |  |  |  |
| nvidia_ai_004 |  |  |  |
| nvidia_ai_005 |  |  |  |

## Evidence/Citation Checklist
- [ ] All required citations are present and linked
- [ ] Evidence supports the claimed answer
- [ ] Source IDs are properly documented
- [ ] Evidence IDs are correctly referenced
- [ ] No external sources or new facts were used
- [ ] All items remain in draft status

## Reviewer Notes Section
Document any observations, clarifications, or concerns about the evaluation process or individual items:

---

## Overall Evaluation Summary Template
**Total Items**: 5
**Passed with Reviewed Evidence**: 
**Needs Manual Review**: 
**Failed Missing Evidence**: 
**Not Evaluated**: 

**Overall Status**: 
**Key Findings**: 

## What This Template Does Not Prove
This evaluation template is designed to document traceability and evidence verification only. It does not prove:
- Technical truth or accuracy of claims
- Independent technical verification or benchmark results
- Model quality or performance metrics
- Commercial traction or market impact
- Provider decisions or recommendations
- Investment thesis or trading conclusions
- Automated extraction quality or reliability

## Recommended Next Small Step
After completing manual evaluation, consider:
1. Documenting any discrepancies found
2. Preparing a summary report of evaluation findings
3. Planning for potential follow-up verification if needed
4. Reviewing the evaluation process for improvements