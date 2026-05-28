# Golden Sets

Golden sets are reviewed reference datasets used for evaluating ForesightGraph's reasoning capabilities. They are not live data or automated truth sources, but rather carefully curated datasets that serve as evaluation indicators.

## Purpose

Golden sets provide stable, reviewed datasets that can be traced back to specific data states. They ensure reproducible and consistent evaluation by serving as standard benchmarks for measuring ForesightGraph's performance.

## Record Format

Each golden set record contains the following fields:

- **item_id**: Unique identifier for the record
- **item_type**: Type of item (question, claim, assertion, etc.)
- **source_ids**: IDs of source documents or references
- **evidence_ids**: IDs of supporting evidence or citations
- **question_or_claim**: The actual question or claim being evaluated
- **expected_answer_or_label**: The expected answer or classification
- **required_citations**: Citations required for the answer
- **review_status**: Review status (draft, reviewed, approved, etc.)
- **reviewer_notes**: Notes from the review process

## Review Rules

- All records must undergo human review before approval
- Review status must be clearly documented
- Reviewer notes should explain evaluation decisions
- Only approved records should be used for official benchmark results

## Quality Checks

- Records must be internally consistent
- Answers must be clearly supported by provided evidence
- Citations must be accurate and complete
- Questions must be well-formed and unambiguous
- All required fields must be populated

## Out-of-Scope Items

The following items are explicitly out of scope for golden sets:

- Real-time market data or live information
- Unverified claims or speculative statements
- Personal opinions or subjective judgments
- Information that could cause legal or regulatory issues
- Content that violates privacy or confidentiality requirements

## Important Notes

Metrics and golden sets are evaluation indicators, not absolute truth. They provide a standardized way to measure performance but should not be treated as definitive or final answers. All evaluation results must include human review documentation and should not be claimed without proper review and approval.