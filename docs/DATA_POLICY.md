# Data Policy

## Purpose

This document defines open-source-safe data boundaries for Phase 1: Methodology Foundation. It is governed by Roadmap v2 and supports evidence-first research without storing protected or private material in the repository.

## Allowed in the Repository

- Source metadata, links, identifiers, dates, access dates, locators, and tier labels.
- Short allowed excerpts when rights and context permit.
- Original summaries written for ForesightGraph.
- Structured Claims, Entities, Edges, Reviews, and Signals when they reference Sources without copying protected full text.
- Empty templates, schemas, validators, tests, and synthetic examples.
- Roadmaps, policies, architecture notes, and methodology documents.

## Not Allowed in the Repository

- API keys, tokens, secrets, credentials, local access data, or private environment values.
- Full-text copies of protected news, paywalled articles, licensed data, or proprietary reports without a documented rights basis.
- Paywall bypass material.
- Private investment decisions, personal portfolio data, broker data, or confidential documents.
- Personal data without purpose, legal basis, and explicit policy.
- Automated trading logic, Buy/Sell/Hold outputs, price target recommendations, broker integration, or investment advice.

## Protected Full-Text Rule

ForesightGraph may store references to protected material, but must not store protected full text.

Allowed:

- URL or document reference.
- Publication title.
- Publisher/source name.
- Published date and accessed date.
- Locator.
- Source Tier.
- Short permitted excerpt if legally safe.
- Original summary and structured Claim.

Not allowed:

- Reproducing full articles.
- Reproducing large paywalled passages.
- Storing licensed news or proprietary report content as project data.

## News Data Rule

NewsItems are raw material. They may be stored as metadata and original notes, but must not become confirmed facts without Evidence and Review status.

Tier 4 and Tier 5 material must remain rumor, quarantined, or draft unless stronger confirmation exists.

## Secret Handling

- Do not commit secrets, tokens, credentials, private keys, cookies, or local configuration with sensitive values.
- Do not print secrets in reports, logs, test output, or task summaries.
- Use environment variables or local-only configuration outside the repository when approved by a separate task.
- If a secret appears in the repository, stop work and report the security issue.

## Data Review Boundary

Productive Claims, Edges, Signals, and Reports must remain traceable to Sources and Evidence. Human Review remains final for productive Claims, Edges, and Reports.

## Open Source Boundary

The public repository should contain code, methodology, policies, tests, and legally safe examples. It should not contain copyrighted full-text data, private data, or personal investment decisions.
