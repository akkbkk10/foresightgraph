# Provider Gates

## Purpose

This document defines provider gates and provider status values for Phase 1: Methodology Foundation. Providers are candidates, not architecture identity.

Provider decisions include model providers, data providers, databases, retrieval systems, agent frameworks, UI frameworks, external services, and tooling integrations.

## Provider Gate Rule

No provider SDK, runtime integration, premium data source, live ingestion pipeline, autonomous agent runtime, GraphRAG system, Vector DB, or deployment workflow may be introduced without documented gates and explicit approval.

## Required Gates

| Gate | Minimum requirement |
|---|---|
| Fit Gate | A concrete ForesightGraph use case is documented. |
| Evidence Gate | Provider or manufacturer claims have Source, locator, and review status. |
| Security Gate | File, network, shell, secret, token, credential, and data boundary risks are reviewed. |
| Evaluation Gate | Provider is benchmarked or compared against a baseline when relevant. |
| License Gate | License, data rights, and usage limits are documented. |
| Cost/Latency Gate | Cost, latency, rate limits, and operational risk are acceptable for the use case. |
| Maintainability Gate | Integration surface is small and adapter-based. |
| Lock-in Gate | Data, prompts, benchmarks, and outputs remain portable. |
| Adoption Gate | Repeated project value exists beyond demo impression. |

## Provider Status Values

```text
candidate
manufacturer_claim
not_reproduced
needs_benchmark
rejected_for_mvp
accepted_for_pilot
accepted_with_constraints
project_decision
```

## Status Usage

| provider_status | Meaning |
|---|---|
| `candidate` | Under consideration only. No integration decision. |
| `manufacturer_claim` | Based on provider documentation or marketing claim. Not independently confirmed. |
| `not_reproduced` | Claim or capability was checked and not reproduced. |
| `needs_benchmark` | Plausible but requires evaluation before decision. |
| `rejected_for_mvp` | Not appropriate for the MVP or current phase. |
| `accepted_for_pilot` | Approved for a limited experiment, not default architecture. |
| `accepted_with_constraints` | Approved only under documented limits. |
| `project_decision` | Accepted as a reviewed project decision. |

## Documentation Requirements

Provider notes must include:

- Provider name and provider type.
- Use case.
- Gate status and open risks.
- Evidence references for claims.
- Security and data boundary notes.
- License and cost notes when relevant.
- Review decision and reviewer notes.

## Forbidden Without Separate Approval

- Provider SDK installation.
- Runtime integration.
- External service activation.
- Live news ingestion or scraping.
- Premium data integration.
- Autonomous agent runtime.
- GraphRAG or Vector DB implementation.
- Secrets, tokens, credentials, or private data in the repository.

## Investment Boundary

Provider tools must not be used to produce investment advice, Buy/Sell/Hold outputs, price targets as recommendations, broker integration, or automated trading logic.
