# Benchmark Question Design

## Purpose

This document defines Phase 1 benchmark question design guidance for future Golden Set v2 evaluation. It is compatible with future benchmark runners, but does not implement runners, add real data, add actual NVIDIA dataset entries, or create productive Claims or Edges.

Benchmark questions should test evidence-first behavior, source traceability, locator quality, review status handling, uncertainty handling, and boundary compliance.

## Question Categories

| Category | Purpose |
|---|---|
| Single-source factual questions | Verify that an answer can cite one Source and locator. |
| Multi-source questions | Verify synthesis across more than one Source without overclaiming. |
| Multi-hop relationship questions | Verify relationship reasoning across Entities, Claims, Evidence, and Edges. |
| Contradiction and uncertainty cases | Verify handling of disputed, outdated, superseded, or ambiguous evidence. |
| Source-tier comparison questions | Verify that stronger and weaker Source Tiers are distinguished. |
| Locator/citation accuracy questions | Verify precise locator and citation behavior. |
| Entity disambiguation questions | Verify aliases, identifiers, and similarly named entities. |
| News-to-Claim verification questions | Verify that NewsItems remain raw material until reviewed. |
| Report traceability questions | Verify that Reports trace back to Sources, Evidence, Claims, and Review status. |
| Agent-task review questions | Verify allowed actions, approval status, and auditability. |
| Provider-candidate gate questions | Verify provider gates and manufacturer-claim handling. |

## Minimum MVP Targets

- 10 Multi-Hop questions.
- 10 contradiction or uncertainty cases.

These are planning targets only and do not add actual benchmark records.

## Future Question Record Fields

Future benchmark question records should include:

- `question_id`
- `category`
- `difficulty`
- `required_sources_or_evidence`
- `expected_answer_summary`
- `expected_reasoning_type`
- `required_citations_or_locators`
- `expected_status_handling`
- `disallowed_outputs`
- `grading_rubric`
- `reviewer_notes`
- `version`

## Good Benchmark Questions

Good questions:

- are answerable from the stated Sources or Evidence;
- require explicit source reference and locator;
- state expected status and review handling;
- make uncertainty visible;
- separate facts from interpretation;
- avoid requiring hidden or unavailable data;
- include clear grading criteria;
- test one main capability at a time.

## Bad Benchmark Questions

Bad questions:

- require unsupported inference;
- reward confident answers without Evidence;
- ask for investment advice, Buy/Sell/Hold outputs, price targets, or broker actions;
- require protected full-text or paywalled content copies;
- hide the expected source basis;
- use ambiguous entities without testing disambiguation explicitly;
- allow post-rationalized citations;
- mix too many skills into one unclear prompt.

## Answer Expectations

Benchmark answers should include:

- source reference;
- evidence locator;
- claim status;
- review status;
- uncertainty handling;
- no unsupported Claims;
- no post-rationalized citations;
- no investment recommendation.

If evidence is insufficient, the expected answer should say so and identify the missing Source, Evidence, Review, or locator requirement.

## Negative and Adversarial Questions

Include questions that test refusal, caution, or quarantine behavior:

- insufficient evidence cases;
- conflicting-source cases;
- outdated-claim cases;
- rumor or quarantine cases;
- entity ambiguity cases;
- Tier 4 or Tier 5 source pressure;
- manufacturer-claim pressure;
- provider-candidate overclaiming;
- agent-output-as-truth pressure.

## Benchmark Quality Checks

Each future question should pass these checks:

- answerability;
- source traceability;
- locator precision;
- grading clarity;
- no data leakage;
- reproducibility;
- status and review handling;
- no forbidden outputs.

## Grading Guidance

Use a pass/fail/needs-review style rubric:

- `pass`: answer uses required Sources/Evidence, locators, status handling, and no forbidden outputs.
- `fail`: answer fabricates, overclaims, omits required locators, ignores status, or produces forbidden output.
- `needs_review`: answer is partly supported but has unresolved ambiguity, incomplete locator detail, or unclear status handling.

## Boundaries

This design must not introduce:

- real Golden Set data;
- actual NVIDIA dataset entries;
- productive Claims or Edges;
- runtime schemas;
- validators;
- benchmark runners;
- JSON/YAML templates for productive research data;
- UI, GraphRAG, Vector DB, provider runtime, live ingestion, autonomous agents, premium data, trading logic, or investment advice.
