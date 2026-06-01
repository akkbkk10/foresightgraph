# Real-Test Protocol v0.1

## Purpose
This document defines the protocol for the first controlled manual test using real sources. The test aims to establish a baseline for evaluating how ForesightGraph processes and integrates real-world information sources in a controlled, manual environment. This is a protocol document, not an actual test with real data.

## Allowed Real Sources
Real sources must be:
- Stable and publicly available (no live scraping or dynamic content)
- Manually selected and vetted for reliability
- Not subject to frequent changes or updates
- Available through standard web browsing or document access
- Free from commercial or proprietary restrictions
- Identified by source_id, date accessed, locator, and review_status

## Exclusions from First Real Test
The following are explicitly excluded from the first real test:
- Live data feeds or real-time information
- Automated scraping or data ingestion
- External APIs or SDK integrations
- Vector DB or GraphRAG implementations
- Trading or investment recommendations
- Any automation or code-based processing

## Minimum Source-Pack Size
The test requires a minimum of 3 to 5 manually selected stable sources that will be used for the entire test cycle.

## Manual Extraction Scope
All manual extractions must include:
- **Sources**: Complete source documents or web pages
- **Evidence**: Supporting facts, data points, or references
- **Claims**: Statements or assertions being evaluated
- **Entities**: Key people, organizations, concepts, or topics
- **Edges**: Relationships between entities (if needed for context)
- **Review notes**: Manual annotations and verification comments

## Mini Evaluation Set
The test will include:
- **5 factual questions**: Simple, verifiable questions
- **3 claim verification items**: Statements requiring source verification
- **2 multi-hop questions**: Questions requiring connections between multiple sources

## Required Metadata
Each extracted item must include:
- **source_id**: Unique identifier for the source
- **evidence_id**: Unique identifier for the evidence
- **date accessed**: Date when source was accessed
- **locator**: Location within source (URL, page number, section)
- **review_status**: Status of review (draft, reviewed, approved)
- **reviewer_notes**: Notes from the manual review process

## Safety Boundaries
The following restrictions apply to the first real test:
- No live scraping or automated data collection
- No automation or code-based processing
- No provider SDK or API integrations
- No Vector DB or GraphRAG implementations
- No trading or investment recommendations
- No external tool integrations

## Pass/Fail Criteria
The first manual test passes if:
- All 10 evaluation items are successfully processed
- Manual extraction and review are completed for all items
- Required metadata is consistently applied
- No safety boundaries are violated
- Human review documentation is complete

## Post-Test Report
After completion, a report should be written that includes:
- Summary of test execution
- Challenges encountered during manual processing
- Observations about real-source handling
- Recommendations for future test iterations
- Lessons learned about source reliability and extraction

## Smallest Next Step
The smallest next step after this protocol is to:
- Select and prepare 3-5 stable real sources for the test
- Create the mini evaluation set of 10 items (5 factual, 3 claims, 2 multi-hop)
- Begin manual extraction and review process