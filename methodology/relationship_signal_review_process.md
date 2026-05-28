# Relationship Signal Review Process

## Purpose

This document defines the manual review process for relationship signals and the criteria for status transitions. It ensures consistent evaluation of signal quality, evidence strength, and proper documentation before signals advance through different confidence levels.

## Review Principle

Relationship signals are research indicators, not investment advice or legal conclusions. The review process maintains clear distinctions between signal types:

- Partnership signal is not acquisition proof
- Acquisition signal is not a legal conclusion
- Stronger status requires stronger evidence
- Old signals decay unless revalidated
- Signals must be traced back to reliable sources with proper quality assessment

## Review Inputs

The following factors are evaluated during signal review:

- **Source quality**: Is the source reputable and authoritative?
- **Evidence summary**: Is the evidence clearly described and relevant?
- **Materiality**: Is the signal significant enough to warrant attention?
- **Confidence**: Does the confidence level match the evidence strength?
- **Recency**: Is the signal timely and relevant?
- **Regulatory/company confirmation**: Are there official confirmations or filings?
- **Repeat signal count**: Are there multiple independent sources supporting the signal?

## Status Transition Rules

- **unverified** → **watch**: Signal meets basic documentation requirements
- **watch** → **confirmed_partnership**: Evidence shows joint development or shared resources
- **watch** → **acquisition_watch**: Clear indication of acquisition interest without confirmation
- **acquisition_watch** → **acquisition_process**: Official filing or announcement indicates active process
- **acquisition_process** → **confirmed_transaction**: Final transaction details confirmed
- **any active status** → **stale**: Signal not revalidated within review period
- **any active status** → **superseded**: New evidence contradicts or replaces existing signal

## Minimal Review Checklist

During manual review, verify:

- Are company names clear and properly identified?
- Is source_type allowed and appropriate for the signal?
- Is url_or_locator present and accessible?
- Are published_at and observed_at present and reasonable?
- Is orientation justified by the evidence?
- Is confidence level appropriate for the evidence strength?
- Is review_due_at set for next review cycle?
- Is the conclusion appropriately scoped (not overclaiming)?

## Confidence Guidance

- **low**: Speculative or indirect evidence, single source, no confirmation
- **medium**: Clear evidence from reputable source, multiple indicators, some confirmation
- **high**: Official filing, regulatory document, or direct company confirmation

## Out of Scope

This review process does not include:
- Buy/Sell/Hold recommendations
- Price targets or financial projections
- Automated legal conclusions or compliance determinations
- Live scraping or real-time alerts
- Automated trading signals