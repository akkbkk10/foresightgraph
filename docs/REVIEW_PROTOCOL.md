# Review Protocol

## Purpose

This document defines review decisions and `review_status` usage for Phase 1: Methodology Foundation. Human Review remains final for productive Claims, Edges, and Reports.

## Review Principle

Agent outputs, extracted Claims, proposed Edges, NewsItems, Signals, and Reports are drafts until reviewed. Review records must preserve who reviewed, what decision was made, when it happened, and why.

## Review Status Values

Use these `review_status` values for review workflow documentation:

| review_status | Meaning | Productive use |
|---|---|---|
| `draft` | Created but not ready for review | No |
| `needs_review` | Ready for human or approved review process | No |
| `confirmed` | Accepted as sufficiently supported for its stated scope | Yes |
| `disputed` | Evidence conflicts or reviewer disagreement remains | No as confirmed fact |
| `rejected` | Not supported, invalid, or out of scope | No |
| `superseded` | Replaced by newer reviewed object | No as current fact |
| `outdated` | No longer current or stale | No as current fact |
| `rumor` | Unconfirmed and weakly sourced | No |
| `quarantined` | Isolated pending stronger verification | No |
| `not_reproduced` | Could not reproduce or verify | No |
| `manufacturer_claim` | Claimed by provider/manufacturer but not independently confirmed | Only with that label |
| `project_decision` | Accepted governance or architecture decision | Yes for project policy only |

## Review Decisions

| Decision | Use when | Required notes |
|---|---|---|
| Accept | Evidence supports the object within stated scope | Evidence IDs, locator quality, caveats |
| Reject | Evidence does not support the object or object is out of scope | Reason for rejection |
| Dispute | Sources conflict or interpretation is unresolved | Conflicting Evidence and next check |
| Quarantine | Source or data risk exists, especially Tier 4 or Tier 5 | Risk and required stronger confirmation |
| Supersede | A newer reviewed object replaces this one | Replacement object reference |
| Mark outdated | Claim or Edge is stale but historically relevant | Last checked date and refresh need |

## Minimum Review Checklist

Before a productive Claim, Edge, or Report is accepted:

- Source exists and has tier metadata.
- Evidence exists and includes locator.
- Claim or Edge is atomic and not overclaiming.
- Review status is assigned.
- Tier 4 or Tier 5 material has stronger confirmation before productive use.
- Any uncertainty, contradiction, or age risk is visible.
- No protected full-text, secrets, private data, or personal investment decision is included.
- No investment advice, Buy/Sell/Hold output, price target recommendation, broker integration, or trading logic is produced.

## Productive Claim Gate

A Claim may become productive only when:

1. It has at least one Evidence reference.
2. Evidence points to a registered Source and locator.
3. Source Tier is recorded.
4. `review_status` is `confirmed` or another explicitly accepted status for the intended use.
5. The Claim is not merely a rumor, unreviewed NewsItem, or unsupported agent output.

## Productive Edge Gate

An Edge may become productive only when:

1. Source and target Entities are clear.
2. Relationship type is specific.
3. Evidence references support the relationship.
4. Review status is recorded.
5. Weak-source material is not the only support unless the Edge remains draft, rumor, or quarantined.

## Reports

Reports must remain traceable to Sources, Evidence, Claims, and Review status. Reports must not present unreviewed objects as confirmed knowledge.
