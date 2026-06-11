# Golden Set v2 Plan

## Purpose

Golden Set v2 is the Phase 1 planning baseline for evaluating ForesightGraph as an evidence-first, review-controlled research system. It defines the minimum reviewed objects needed before later work on richer ingestion, workbench UI, graph retrieval, or provider integrations.

This is a planning document only. It does not add real Sources, Claims, Entities, Edges, NewsItems, Reports, AgentTasks, runtime schemas, validators, or ingestion pipelines.

## First Reference Track

The first reference track is the NVIDIA Ecosystem because it is a complex AI infrastructure ecosystem with companies, products, supply chains, news, risks, and technical sources.

NVIDIA is not:

- the project name;
- a core dependency;
- an official partnership;
- a vendor lock-in.

## MVP Target Counts

| Object type | Target count |
|---|---:|
| Sources | 20 |
| Claims | 20 |
| Entities | 30 |
| Edges | 30 |
| NewsItems | 20 |
| Multi-Hop questions | 10 |
| Contradiction or uncertainty cases | 10 |
| Reports | 5 |
| AgentTasks | 5 |

## Object Readiness Criteria

| Object type | Ready when |
|---|---|
| Source | Source has title, source type, date or accessed date, locator, tier, and license note. |
| Evidence | Evidence references a Source and locator and stores only a short allowed excerpt or original summary. |
| NewsItem | NewsItem has Source Tier, publication metadata when available, topic, quarantine or review status, and no full-text copy. |
| Claim | Claim is atomic, evidence-backed, has status, confidence, last checked date, and review status. |
| Entity | Entity has a stable name, type, aliases or identifiers when useful, and review status. |
| Edge | Edge connects two reviewed Entities, has relationship type, Evidence references, status, and review status. |
| Multi-Hop question | Question can be answered only by connecting multiple reviewed objects and has expected source traceability. |
| Contradiction or uncertainty case | Case identifies disputed, outdated, superseded, or ambiguous evidence and the required follow-up. |
| Report | Report references reviewed Sources, Evidence, Claims, and uncertainty notes. |
| AgentTask | AgentTask has allowed actions, forbidden actions, approval status, output references, and AuditLogEntry relationship. |

## Review Requirements

- Productive Claims require Evidence and Review status.
- Productive Edges require Evidence and Review status.
- Reports must not present unreviewed Claims, Edges, NewsItems, or agent outputs as confirmed.
- Tier 4 and Tier 5 material remains `rumor`, `quarantined`, or draft unless stronger confirmation exists.
- Human Review remains final for productive Claims, Edges, and Reports.

## Open-Source-Safe Data Boundaries

Golden Set v2 planning and later data work must follow `DATA_POLICY.md`:

- Store metadata, links, locators, short allowed excerpts, and original summaries.
- Do not store protected full-text news, paywalled article copies, licensed data, or proprietary reports without a documented rights basis.
- Do not store secrets, tokens, credentials, private data, personal portfolio data, or confidential documents.
- Do not store private investment decisions.

## Investment Boundary

Golden Set v2 must not contain or produce:

- investment advice;
- Buy/Sell/Hold outputs;
- price targets as recommendations;
- broker integration;
- automated trading logic.

## Planning Sequence

1. Confirm object fields against `SCHEMA_LITE.md`.
2. Select candidate Source categories without ingesting data.
3. Define review workflow using `REVIEW_PROTOCOL.md`.
4. Define tier handling using `NEWS_SOURCE_TIERS.md`.
5. Define AgentTask boundaries using `AGENT_TASK_GOVERNANCE.md`.
6. Define provider evaluation boundaries using `PROVIDER_CANDIDATE_GOVERNANCE.md`.
7. Create a later, separately approved PR for any actual Golden Set data.
