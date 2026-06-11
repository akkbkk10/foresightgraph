# Provider Evaluation Notes

## Purpose

Provider Evaluation Notes document provider claims, evidence, gates, and review decisions before any adoption decision. They support `PROVIDER_GATES.md`, `PROVIDER_CANDIDATE_GOVERNANCE.md`, and `ARCHITECTURE_DECISION_RECORDS.md`.

Provider Evaluation Notes do not approve provider SDK installation, runtime integration, premium data integration, live ingestion, or vendor lock-in.

## Evaluation Status Concepts

| Concept | Meaning |
|---|---|
| `manufacturer_claim` | A provider or vendor claims a capability; it is not independently confirmed. |
| `not_reproduced` | A claim or capability was checked and could not be reproduced. |
| `benchmark_result` | A measured result from a documented benchmark or comparison. |
| `accepted_for_pilot` | Approved only for a limited, separately scoped pilot. |
| `rejected_for_mvp` | Not suitable for the current MVP or Phase 1 scope. |
| `project_decision` | A reviewed project decision, usually requiring gates and an ADR when architectural. |

## Minimum Provider Evaluation Fields

Provider Evaluation Notes should include:

- `provider_name`
- `provider_type`
- `use_case`
- `claim_source`
- `locator`
- `evidence_summary`
- `security_notes`
- `license_notes`
- `cost_latency_notes`
- `benchmark_requirement`
- `lock_in_risk`
- `maintainability_notes`
- `decision_status`
- `reviewer_notes`

## Required Gate Alignment

Provider notes should address the existing provider gates:

- Fit;
- Evidence;
- Security;
- Evaluation;
- License;
- Cost/Latency;
- Maintainability;
- Lock-in;
- Adoption.

If a gate is unknown, the decision status should remain `needs_review`, `needs_benchmark`, or `rejected_for_mvp` rather than becoming a project decision.

## Manufacturer Claims vs Project Decisions

Manufacturer claims are useful inputs, but they are not project decisions. A provider claim needs Source, locator, Evidence summary, and review notes before it can influence architecture.

Project decisions require:

- reviewed gates;
- benchmark evidence or a clear Roadmap gate where relevant;
- documented risks;
- explicit approval;
- ADR linkage when the decision changes architecture or runtime behavior.

## Phase 1 Boundaries

Phase 1 may document provider evaluation notes, but must not introduce:

- provider SDK installation;
- runtime integration;
- external service activation;
- live ingestion or scraping;
- premium data integration;
- autonomous agents;
- GraphRAG;
- Vector DB;
- secrets, tokens, credentials, or private data.

Provider notes must not produce investment advice, Buy/Sell/Hold outputs, price targets as recommendations, broker integration, or automated trading logic.
