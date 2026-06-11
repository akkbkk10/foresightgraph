# Manual Review Workflow

## Purpose

This document defines the Phase 1 manual review workflow for ForesightGraph research objects. It operationalizes `REVIEW_PROTOCOL.md`, `EVIDENCE_RULES.md`, `NEWS_SOURCE_TIERS.md`, `DATA_POLICY.md`, and `GOLDEN_SET_ACCEPTANCE_CRITERIA.md`.

This is documentation only. It does not add real Sources, Evidence, Claims, Entities, Edges, NewsItems, Reports, AgentTasks, ProviderCandidates, schemas, validators, runners, or ingestion.

## Review Inputs

Manual review may evaluate:

- Sources;
- Evidence;
- NewsItems;
- Claims;
- Entities;
- Edges;
- Reviews;
- Reports;
- AgentTasks;
- ProviderCandidates;
- benchmark questions.

## Review Flow

```text
draft -> needs_review -> accepted | rejected | quarantined | superseded
```

Use object-level `status` and `review_status` from the relevant Phase 1 docs. `accepted` in this workflow means accepted for the specific review scope; it does not override weak evidence, source tier limits, or product boundaries.

## Step-by-Step Review

1. Confirm the object type and intended use.
2. Check required metadata against `SCHEMA_LITE.md`.
3. Check Evidence, locator, Source Tier, and source date or accessed date.
4. Check data boundaries: no protected full text, secrets, private data, or paywalled full-text copies.
5. Check claim boundaries: no unsupported facts, no investment advice, no Buy/Sell/Hold output, no price target recommendation, no broker integration.
6. Assign a review decision and notes.
7. Mark follow-up needs, supersession, quarantine, or rejection clearly.

## Decision Outcomes

| Decision | Use when | Required notes |
|---|---|---|
| `accepted` | Object meets metadata, evidence, review, and boundary requirements for its scope. | Evidence references, locator quality, caveats. |
| `needs_review` | Object is plausible but incomplete or ambiguous. | Missing metadata or unresolved review question. |
| `rejected` | Object is unsupported, unsafe, out of scope, or misleading. | Reason for rejection. |
| `quarantined` | Object is rumor-like, weakly sourced, risky, or license-sensitive. | Risk and stronger confirmation needed. |
| `superseded` | A newer reviewed object replaces this one. | Replacement reference and reason. |

## Productive Object Gates

- Productive Claims require Evidence and Review status.
- Productive Edges require Evidence and Review status.
- NewsItems remain raw material until reviewed and converted into Evidence-backed Claims.
- Tier 4 and Tier 5 sources must not become productive facts without stronger confirmation.
- ProviderCandidate decisions must pass gates and must not rely on manufacturer claims alone.
- AgentTask outputs are drafts until reviewed and must not autonomously finalize productive research objects.

## Reviewer Notes

Reviewer notes should be short, factual, and traceable. They should include:

- decision;
- object reference;
- Evidence or Source reference;
- locator quality;
- uncertainty or conflict;
- follow-up action;
- reviewer placeholder or reviewer identity when appropriate.

## Stop Conditions

Stop review and escalate if:

- required source or locator metadata is missing;
- protected full text or paywalled content appears;
- secrets, credentials, tokens, private data, or personal portfolio data appear;
- the object implies runtime integration, live ingestion, provider adoption, autonomous agents, or premium data;
- the object includes trading logic, Buy/Sell/Hold output, price target recommendation, broker integration, or investment advice.
