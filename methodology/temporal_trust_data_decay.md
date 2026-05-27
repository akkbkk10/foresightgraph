# Temporal Trust and Data Decay Policy

## Purpose

ForesightGraph should be an intelligent evidence system, not a static data cemetery. This policy defines how evidence, claims, and sources lose or keep value over time, ensuring that data relevance depends on context, source type, validity, and review status rather than age alone.

## Core Principle

Age alone is not enough to determine data value. Context determines decay - the same piece of information may remain highly relevant for years in some contexts while becoming obsolete quickly in others. Freshness must be evaluated relative to the data type, domain, and intended use.

## Freshness Classes

- **static**: Information that doesn't change over time (standards, laws, historical facts, mathematical truths)
- **slow**: Information that changes infrequently (technical architecture, product specifications, company policies)
- **medium**: Information that changes periodically (market data, news, regulatory updates)
- **fast**: Information that changes frequently (company statements, social media, short-term forecasts)
- **real_time**: Information that changes continuously (live signals, streaming data, current prices)

## Suggested Metadata Fields

- `observed_at`: When the evidence was first observed or collected
- `published_at`: When the source was originally published
- `valid_from`: When the evidence becomes valid
- `valid_until`: When the evidence expires
- `last_verified_at`: When the evidence was last verified
- `review_due_at`: When the evidence needs re-review
- `freshness_class`: The freshness class of the data
- `decay_policy`: The decay policy applied to this data
- `trust_score`: Overall trustworthiness score (0.0-1.0)
- `staleness_score`: Measure of how stale the data is (0.0-1.0)
- `status`: Current status of the evidence

## Suggested Statuses

- **active**: Evidence is current and valid
- **stale**: Evidence has exceeded its freshness threshold
- **superseded**: Evidence has been replaced by newer information
- **disputed**: Evidence is under review or contested
- **archived**: Evidence is preserved but not actively used

## Example Decay Behavior by Data Type

- **Historical fact**: Static - remains relevant indefinitely, but may need context for interpretation
- **Technical architecture**: Slow - changes only with major updates, but may become outdated
- **Product feature**: Medium - changes with product releases, but core features may remain stable
- **Regulation/law/norm**: Static - remains valid until changed, but may need interpretation
- **Company statement**: Fast - may become outdated quickly, especially in fast-moving markets
- **Market/news data**: Fast - becomes stale within hours to days depending on market volatility
- **Real-time price/signal**: Real-time - value diminishes immediately after observation

## MVP Scoring Idea

```
current_value = base_trust * freshness_factor * source_quality * review_factor
```

Where:
- `base_trust`: Inherent trustworthiness of the source (0.0-1.0)
- `freshness_factor`: Adjusts for how current the data is (0.0-1.0)
- `source_quality`: Quality of the source (0.0-1.0)
- `review_factor`: Impact of human review (0.0-1.0)

## Human Review Rule

All evidence must undergo human review at least once before being considered for active use. The review process establishes initial trust scores and sets review schedules based on the freshness class and data type.

## What is Out of Scope for Now

- No automatic trading signals
- No live data feeds
- No external APIs
- No full scoring implementation yet

## Next Implementation Candidates

- Add metadata to records later
- Add freshness_score later
- Add review_due queue later