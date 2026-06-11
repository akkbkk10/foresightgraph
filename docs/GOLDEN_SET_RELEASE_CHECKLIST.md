# Golden Set Release Checklist

## Purpose

This checklist defines the documentation-only release gate for future Golden Set v2 versions. It supports `GOLDEN_SET_V2_PLAN.md`, `GOLDEN_SET_ACCEPTANCE_CRITERIA.md`, `BENCHMARK_QUESTION_DESIGN.md`, and `MANUAL_REVIEW_WORKFLOW.md`.

This checklist does not add real Golden Set data, runtime schemas, validators, benchmark runners, or productive research templates.

## Release Metadata

Future Golden Set releases should record:

- `golden_set_version`;
- release date;
- changelog summary;
- reviewer or review decision placeholder;
- included object counts;
- superseded record references;
- known limitations;
- next review date.

## Minimum Count Targets

| Object type | MVP target |
|---|---:|
| Sources | 20 |
| Claims | 20 |
| Entities | 30 |
| Edges | 30 |
| NewsItems | 20 |
| Multi-Hop questions | 10 |
| Contradiction or uncertainty cases | 10 |
| Reports | 5 |
| AgentTasks | 5 |

## Pre-Release Checklist

- [ ] Object counts are recorded.
- [ ] Required metadata is present where relevant: source reference, date, locator, tier, status, review_status, reviewer or decision placeholder, and last_checked.
- [ ] Productive Claims have Evidence and Review status.
- [ ] Productive Edges have Evidence and Review status.
- [ ] NewsItems are treated as raw material until reviewed.
- [ ] Tier 4 and Tier 5 material is not promoted to productive fact without stronger confirmation.
- [ ] ProviderCandidate records are gate-based, not vendor-claim-based.
- [ ] AgentTask records include allowed actions, approval status, and auditability.
- [ ] Benchmark questions have expected answer summary, required locators, disallowed outputs, and grading rubric.
- [ ] Superseded records remain traceable and are not treated as current.

## Data Boundary Checklist

- [ ] No protected full-text news is stored.
- [ ] No paywalled full-text copies are stored.
- [ ] No secrets, tokens, credentials, private data, or personal portfolio data are stored.
- [ ] No private investment decisions are stored.
- [ ] No investment advice, Buy/Sell/Hold output, price target recommendation, broker integration, or trading logic is present.

## Review Outcomes

Every reviewed object should end in one of:

```text
accepted
needs_review
rejected
quarantined
superseded
```

`accepted` means accepted for the Golden Set release scope. It does not override object-level status, review_status, or source-tier limitations.

## Release Decision

A future Golden Set release is ready only when:

1. required metadata and review outcomes are complete;
2. object counts and known limitations are documented;
3. boundary checks pass;
4. benchmark question checks pass;
5. superseded or quarantined items are clearly marked;
6. reviewers can reproduce source and locator traceability.

If any checklist item fails, the release remains `needs_review` or `quarantined` until corrected.

## Out of Scope

This checklist does not approve:

- real data ingestion;
- runtime schemas;
- validators;
- benchmark runners;
- UI;
- GraphRAG;
- Vector DB;
- provider runtime integration;
- live ingestion or scraping;
- autonomous agents;
- premium data;
- trading logic or investment advice.
