# ProviderCandidate Governance

## Purpose

This document defines how ProviderCandidate records should be planned and reviewed in Phase 1. It supports `PROVIDER_GATES.md`, `DATA_POLICY.md`, and `SCHEMA_LITE.md`.

Provider candidates are evaluation objects. They are not runtime integrations and do not approve SDK installation, external service activation, premium data integration, or vendor lock-in.

## ProviderCandidate Record

Purpose: document a potential provider, tool, model, database, data source, framework, or service before any adoption decision.

Recommended fields:

- `id`
- `provider_name`
- `provider_type`
- `use_case`
- `gate_status`
- `provider_status`
- `evidence`
- `license_note`
- `security_notes`
- `cost_latency_notes`
- `lock_in_notes`
- `review_status`
- `created_at`
- `updated_at`

## Required Provider Gates

| Gate | Review question |
|---|---|
| Fit | Is there a concrete ForesightGraph use case? |
| Evidence | Are provider or manufacturer claims backed by Source, locator, and review status? |
| Security | Are file, network, shell, secret, token, credential, and data risks understood? |
| Evaluation | Is there a baseline or benchmark plan before adoption? |
| License | Are license, data rights, and usage limits documented? |
| Cost/Latency | Are cost, latency, quotas, and operational limits acceptable? |
| Maintainability | Is the integration surface small and adapter-based? |
| Lock-in | Are data, prompts, evaluations, and outputs portable? |
| Adoption | Is there repeated project value beyond a demo impression? |

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

## Manufacturer Claims vs Project Decisions

- `manufacturer_claim` means the capability is claimed by the provider or vendor and is not independently confirmed.
- `needs_benchmark` means the candidate may be useful but requires evaluation before adoption.
- `accepted_for_pilot` allows a limited, separately approved experiment. It is not default architecture.
- `accepted_with_constraints` requires documented limits and review notes.
- `project_decision` requires reviewed gates and explicit approval.

## Phase 1 Boundaries

Phase 1 may document ProviderCandidates and gates, but must not introduce:

- provider SDK installation;
- runtime integration;
- external service activation;
- live news ingestion or scraping;
- autonomous agents;
- premium data integration;
- GraphRAG;
- Vector DB;
- vendor lock-in;
- secrets, tokens, credentials, or private data.

## Review Requirements

ProviderCandidate review must include:

- use case;
- gate status;
- evidence references and locators for provider claims;
- security and data-boundary notes;
- license and cost notes when relevant;
- review status;
- decision rationale.

ProviderCandidate records must not produce investment advice, Buy/Sell/Hold outputs, price targets as recommendations, broker integration, or automated trading logic.
