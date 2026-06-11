# Golden Set Acceptance Criteria

## Purpose

This document defines planning-stage acceptance criteria for future Golden Set v2 records. It supports manual review first and later validators, but does not add real Golden Set data, runtime schemas, validators, or productive research templates.

Golden Set acceptance must align with `SCHEMA_LITE.md`, `GOLDEN_SET_V2_PLAN.md`, `EVIDENCE_RULES.md`, `NEWS_SOURCE_TIERS.md`, `REVIEW_PROTOCOL.md`, `AGENT_TASK_GOVERNANCE.md`, and `PROVIDER_CANDIDATE_GOVERNANCE.md`.

## Readiness States

Use these readiness states for acceptance review:

```text
draft
needs_review
accepted
rejected
quarantined
superseded
```

`accepted` means accepted for the Golden Set review scope. It does not override object-level `status` or `review_status`, and it does not turn weak or quarantined evidence into confirmed fact.

## Minimum Metadata

Golden Set records should include, where relevant:

- source reference;
- source date or accessed date;
- locator;
- tier;
- status;
- review_status;
- reviewer or review decision placeholder;
- last_checked;
- version reference.

## Object Acceptance Criteria

| Object type | Accept when | Reject or quarantine when |
|---|---|---|
| Source | Recoverable source reference, source date or accessed date, locator, tier, license note, and review status are present. | Source is inaccessible, lacks rights context, has no locator, or contains protected full text. |
| Evidence | Evidence points to a Source, has locator precision, short allowed excerpt or original summary, confidence, status, and review status. | Evidence cannot be traced, overquotes protected content, or does not support the linked object. |
| NewsItem | Source Tier, publication metadata when available, topic, quarantine or review status, and no full-text copy are present. | NewsItem is treated as confirmed fact before review or relies on Tier 4/5 material without stronger confirmation. |
| Claim | Claim is atomic, evidence-backed, has status, confidence, last_checked, and review_status. | Claim lacks Evidence, overclaims, combines fact and interpretation, or produces investment advice. |
| Entity | Entity has stable name, entity type, useful aliases or identifiers, status, and review status. | Entity is ambiguous, duplicated, or unsupported by reviewed context. |
| Edge | Edge links two clear Entities, has relationship type, Evidence references, status, and review status. | Edge lacks Evidence or Review status, or depends only on weak Tier 4/5 material. |
| Review | Review identifies object type, object id, decision, reviewer placeholder or reviewer, reviewed_at placeholder or date, and notes. | Review decision is missing, unexplained, or inconsistent with Evidence. |
| Report | Report references reviewed Sources, Evidence, Claims, uncertainty notes, and traceable status handling. | Report presents unreviewed Claims, Edges, NewsItems, or agent outputs as confirmed. |
| AgentTask | AgentTask has allowed actions, forbidden actions, approval status, output references, and auditability. | AgentTask lacks approval status, exceeds allowed actions, or finalizes productive research objects autonomously. |
| ProviderCandidate | ProviderCandidate is evaluated through gates and status values, not vendor claims alone. | ProviderCandidate depends on manufacturer claims as project decisions or implies runtime adoption without approval. |

## Pass / Fail / Needs-Review Checks

Use these check outcomes for future manual review and validator design:

- `pass`: required metadata is present, traceability is clear, and boundaries are respected.
- `fail`: required metadata is missing, traceability fails, or forbidden content appears.
- `needs_review`: evidence exists but source quality, status, locator, ambiguity, or interpretation requires human review.

Minimum checks:

- Source reference exists.
- Source date or accessed date exists.
- Locator exists and is specific enough.
- Source Tier is recorded.
- `status` is recorded.
- `review_status` is recorded.
- Reviewer or review decision placeholder exists.
- `last_checked` exists where recency matters.
- No protected full-text, secrets, private data, or paywalled full-text copies are stored.

## Productive Object Rules

- Productive Claims require Evidence and Review status.
- Productive Edges require Evidence and Review status.
- NewsItems remain raw material until reviewed and converted into Evidence-backed Claims.
- Tier 4 and Tier 5 sources must not become productive facts without stronger confirmation.
- ProviderCandidate acceptance is gate-based, not vendor-claim-based.
- AgentTask acceptance requires allowed actions, approval status, and auditability.

## Versioning Guidance

Future Golden Set releases should use:

- `golden_set_version`;
- changelog entry;
- record-level version or last updated date;
- superseded record references;
- reason for acceptance, rejection, quarantine, or supersession.

Superseded records should remain traceable but must not be treated as current accepted records.

## Boundaries

Golden Set acceptance criteria must not approve:

- protected full-text storage;
- secrets, tokens, credentials, private data, or paywalled full-text copies;
- investment advice;
- Buy/Sell/Hold outputs;
- price targets as recommendations;
- broker integration;
- real data ingestion in this planning package.
