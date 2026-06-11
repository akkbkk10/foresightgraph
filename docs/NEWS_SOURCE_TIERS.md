# News Source Tiers

## Purpose

This document defines Source Tier rules for Phase 1: Methodology Foundation. It implements the Roadmap v2 Verified News principle: news is raw material, not automatically confirmed fact.

## Tier Rules

| Tier | Source type | Use | Claim weight | Review rule | Open-source rule |
|---|---|---|---|---|---|
| Tier 1 | Primary Sources: filings, annual reports, investor relations, official technical documents, regulatory documents | Preferred factual basis | High | Review still required, but quarantine is usually lower | Metadata, links, locators, short allowed excerpts, own Claims |
| Tier 2 | News agencies and high-quality financial or business media | Event and context validation | Medium to high | Source and Tier review required; critical Claims need stronger or second-source support | No full-text copies; metadata, link, short allowed excerpt, own summary |
| Tier 3 | Industry and technology media | Early signals and technical context | Medium | Productive Claims require cross-checking | No full-text copies; mark as secondary source |
| Tier 4 | Blogs, podcasts, YouTube, social media, expert commentary | Ideas, leads, opinions | Low | Not fact without Tier 1 or Tier 2 confirmation or equivalent stronger Evidence | Link, metadata, own note only |
| Tier 5 | Rumors, unconfirmed leaks, anonymous claims, weakly sourced posts | Watchlist and hypothesis only | Very low | Always `rumor` or `quarantined` unless upgraded by stronger Sources | Do not publish as confirmed knowledge |

## News-to-Claim Flow

```text
NewsItem -> Source Tier -> Relevance Check -> Evidence -> Claim Draft -> Review -> Confirmed/Rejected/Disputed -> Signal/Report
```

## NewsItem Rules

- A NewsItem is raw material.
- A NewsItem must not create a productive Claim, Edge, Signal, or Report conclusion by itself.
- A NewsItem must have Source Tier, Source metadata, publication date when available, locator, and quarantine or review status.
- Tier 4 and Tier 5 NewsItems must not become productive facts without stronger confirmation.

## Tier Upgrade and Downgrade

- A low-tier item may be upgraded only by adding stronger Evidence from a higher-tier or directly relevant Source.
- A high-tier item may be downgraded if it is corrected, contradicted, outdated, inaccessible, or too vague to support the Claim.
- Tier is source-quality metadata. It is not a truth label.

## Critical Claim Rule

Critical Claims include Claims that affect productive Edges, Signals, Reports, risk conclusions, provider decisions, or investment-adjacent interpretation.

Critical Claims require:

- Evidence with a clear locator.
- Review status.
- Source Tier recorded.
- Conservative wording.
- Stronger confirmation when based on Tier 3, Tier 4, or Tier 5 material.

## Forbidden News Handling

- Do not store copyrighted full-text news or paywalled article copies.
- Do not scrape or ingest live news in Phase 1.
- Do not treat rumors as facts.
- Do not produce Buy/Sell/Hold outputs, price targets, broker actions, automated trading logic, or investment advice.
