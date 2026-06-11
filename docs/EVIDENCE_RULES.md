# Evidence Rules

## Purpose

This document defines the minimum evidence rules for Phase 1: Methodology Foundation. It is governed by `../ForesightGraph_Intelligence_OS_Roadmap_v2.md`.

ForesightGraph is evidence-first: no productive Claim, Edge, Signal, or Report may be treated as reliable unless it is traceable to Sources, Evidence, locator metadata, and Review status.

## Core Rule

```text
Source -> Evidence -> Claim Draft -> Review -> Productive Claim or Rejection
Source -> Evidence -> Edge Draft -> Review -> Productive Edge or Rejection
```

NewsItems are raw material. They are not confirmed facts until the News-to-Claim process creates Evidence, a draft Claim, and a Review decision.

## Required Fields

| Object | Minimum evidence fields | Rule |
|---|---|---|
| Source | `id`, `title`, `source_type`, `url_or_file`, `source_date`, `accessed_at`, `tier`, `license_note` | A Source must be recoverable and classified before it supports Evidence. |
| Evidence | `id`, `source_id`, `locator`, `excerpt_or_summary`, `evidence_type`, `confidence` | Evidence must point to a Source and a precise location or locator. |
| Claim | `id`, `text`, `claim_type`, `evidence_ids`, `status`, `confidence`, `last_checked`, `review_status` | A productive Claim requires at least one Evidence reference and Review status. |
| Edge | `id`, `source_entity_id`, `target_entity_id`, `relationship_type`, `evidence_ids`, `status`, `review_status` | A productive Edge requires Evidence and Review status. |

## Status Values

Use Roadmap v2 status values where possible:

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

## Claim Rules

- Claims must be atomic, testable, and tied to one or more Evidence records.
- Claims must not combine fact, interpretation, and recommendation in one statement.
- A `confirmed` Claim must have Review status showing it was accepted under the Review Protocol.
- A `manufacturer_claim` is not independently verified unless stronger Evidence and Review support it.
- `rumor`, `quarantined`, `disputed`, and `not_reproduced` Claims must not be used as confirmed facts.
- `outdated` and `superseded` Claims must remain traceable, but must not be presented as current.

## Edge Rules

- Edges are relationships between Entities and must be evidence-bound.
- A productive Edge requires at least one Evidence reference and a Review decision.
- Weak or indirect Evidence may support an Edge draft, but not a confirmed productive Edge.
- Tier 4 and Tier 5 material must not support a productive Edge without stronger confirmation from higher-tier Sources.

## Evidence Strength

| Evidence condition | Allowed use |
|---|---|
| Direct primary Source with clear locator | May support `confirmed` after Review. |
| Reputable secondary Source with clear locator | May support `needs_review`; may support `confirmed` when Review accepts it or stronger support exists. |
| Manufacturer or provider claim | Use `manufacturer_claim` until independently checked or explicitly accepted as such. |
| Opinion, blog, social, podcast, or unverified report | Use only as draft, watchlist, `rumor`, or `quarantined` unless stronger confirmation exists. |

## Open-Source Boundary

- Store metadata, links, locators, short allowed excerpts, and original summaries.
- Do not store protected full-text news, paywalled article copies, or licensed data unless rights are documented.
- Do not store secrets, tokens, credentials, private data, or personal portfolio decisions.

## Investment Boundary

Evidence, Claims, Edges, Signals, and Reports must not produce investment advice, Buy/Sell/Hold outputs, price targets as recommendations, broker integration, or automated trading logic.
