# Schema-Lite Data Model

## Purpose

This document defines the Phase 1 schema-lite model for ForesightGraph. It is documentation only. It does not implement runtime schemas, validators, migrations, JSON/YAML templates, or database changes.

The model aligns with:

- `EVIDENCE_RULES.md`
- `NEWS_SOURCE_TIERS.md`
- `REVIEW_PROTOCOL.md`
- `PROVIDER_GATES.md`
- `DATA_POLICY.md`
- `../ForesightGraph_Intelligence_OS_Roadmap_v2.md`

## Shared Conventions

Where useful, objects should include:

- `id`
- `created_at`
- `updated_at`
- `status`
- `review_status`

Use Roadmap v2 status values where applicable:

```text
draft
needs_review
confirmed
disputed
rejected
superseded
outdated
rumor
quarantined
not_reproduced
manufacturer_claim
project_decision
```

Productive Claims and Edges require Evidence and Review status. NewsItems are raw material until reviewed and converted into Evidence-backed Claims.

## Source

Purpose: register a recoverable source before it supports Evidence, Claims, NewsItems, or Edges.

Required fields:

- `id`
- `title`
- `source_type`
- `url_or_file`
- `source_date`
- `accessed_at`
- `tier`
- `license_note`
- `status`

Allowed statuses: `draft`, `needs_review`, `confirmed`, `rejected`, `outdated`, `superseded`, `quarantined`.

Key relationships:

- Source has many Evidence records.
- Source may have many NewsItems.
- Source tier follows `NEWS_SOURCE_TIERS.md`.
- Source storage follows `DATA_POLICY.md`; protected full text is not stored.

## Evidence

Purpose: document a traceable source location, excerpt, or summary that supports a Claim or Edge.

Required fields:

- `id`
- `source_id`
- `locator`
- `excerpt_or_summary`
- `evidence_type`
- `confidence`
- `status`
- `review_status`

Allowed statuses: `draft`, `needs_review`, `confirmed`, `disputed`, `rejected`, `superseded`, `outdated`, `manufacturer_claim`.

Key relationships:

- Evidence belongs to one Source.
- Evidence may support many Claims.
- Evidence may support many Edges.
- Evidence must include a locator precise enough for review.

## NewsItem

Purpose: capture news as raw material for review, Evidence creation, and Claim drafting.

Required fields:

- `id`
- `source_id`
- `title`
- `published_at`
- `tier`
- `topic`
- `quarantine_status`
- `status`
- `review_status`

Allowed statuses: `draft`, `needs_review`, `rumor`, `quarantined`, `confirmed`, `rejected`, `outdated`, `superseded`.

Key relationships:

- NewsItem belongs to one Source.
- NewsItem may lead to Evidence.
- NewsItem may lead to draft Claims only after relevance and review checks.
- NewsItem does not create productive Claims, Edges, Signals, or Reports by itself.

## Claim

Purpose: represent an atomic, testable statement derived from Evidence.

Required fields:

- `id`
- `text`
- `claim_type`
- `evidence_ids`
- `status`
- `confidence`
- `last_checked`
- `review_status`

Allowed statuses: `draft`, `needs_review`, `confirmed`, `disputed`, `rejected`, `superseded`, `outdated`, `rumor`, `quarantined`, `not_reproduced`, `manufacturer_claim`.

Key relationships:

- Claim has one or more Evidence references before productive use.
- Claim may reference Entities.
- Claim may support Edges, Signals, or Reports after Review.
- Claim must not combine fact, interpretation, and recommendation in one object.

## Entity

Purpose: normalize companies, products, technologies, people, places, and concepts.

Required fields:

- `id`
- `name`
- `entity_type`
- `aliases`
- `identifiers`
- `status`
- `review_status`

Allowed statuses: `draft`, `needs_review`, `confirmed`, `disputed`, `rejected`, `superseded`, `outdated`.

Key relationships:

- Entity may appear in Claims.
- Entity may be the source or target of Edges.
- Entity aliases and identifiers support consistent naming.

## Edge

Purpose: model an evidence-bound relationship between two Entities.

Required fields:

- `id`
- `source_entity_id`
- `target_entity_id`
- `relationship_type`
- `evidence_ids`
- `status`
- `review_status`

Allowed statuses: `draft`, `needs_review`, `confirmed`, `disputed`, `rejected`, `superseded`, `outdated`, `rumor`, `quarantined`.

Key relationships:

- Edge connects two Entities.
- Edge requires one or more Evidence references before productive use.
- Edge requires Review status before it appears as a productive graph relationship.
- Tier 4 and Tier 5 material must not support a productive Edge without stronger confirmation.

## Review

Purpose: record a human or approved review-process decision for a reviewable object.

Required fields:

- `id`
- `object_type`
- `object_id`
- `reviewer`
- `decision`
- `reviewed_at`
- `notes`

Allowed decisions:

- `accept`
- `reject`
- `dispute`
- `quarantine`
- `supersede`
- `mark_outdated`

Key relationships:

- Review may apply to Source, Evidence, NewsItem, Claim, Entity, Edge, Signal, Report, ProviderCandidate, or AgentTask.
- Review decisions update or justify `review_status`.
- Human Review remains final for productive Claims, Edges, and Reports.

## AuditLogEntry

Purpose: preserve an audit trail for agent, human, repository, and review actions.

Required fields:

- `id`
- `actor`
- `action`
- `object_ref`
- `timestamp`
- `result`
- `notes`

Allowed statuses: `draft`, `confirmed`, `rejected`, `superseded`, `project_decision`.

Key relationships:

- AuditLogEntry may reference an AgentTask, Review, PR, Claim, Edge, Report, or provider decision.
- Audit entries must not expose secrets, tokens, credentials, private data, or protected full text.

## Boundary Rules

- This document is not a runtime schema.
- Do not add validators, migrations, JSON/YAML templates, database changes, or application code from this document alone.
- Do not store copyrighted full-text news, secrets, private data, or personal investment decisions.
- Do not produce investment advice, Buy/Sell/Hold outputs, price targets, broker integration, or trading logic.
