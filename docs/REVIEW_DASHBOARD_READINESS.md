# Review Dashboard Readiness

## Purpose

This document defines what must be ready before any future review dashboard or data quality dashboard implementation. It is a planning document only and does not choose a frontend framework, implement UI, add dashboard code, or connect live data.

The dashboard concept should serve review and data quality work. It must not become a shortcut around Evidence, Source Tiers, Review status, or human judgment.

## Minimum Readiness Criteria

Before any UI or dashboard PR is considered, these docs and concepts must exist:

- Source, Evidence, Claim, and Review objects are defined in `SCHEMA_LITE.md`.
- `review_status` and review decisions are documented in `REVIEW_PROTOCOL.md`.
- Golden Set acceptance criteria are documented in `GOLDEN_SET_ACCEPTANCE_CRITERIA.md`.
- Benchmark question design is documented in `BENCHMARK_QUESTION_DESIGN.md`.
- Manual review workflow is documented in `MANUAL_REVIEW_WORKFLOW.md`.
- Data quality metrics are documented in `DATA_QUALITY_METRICS.md`.

## First Dashboard Sections

| Section | Purpose | Inputs | Readiness signal |
|---|---|---|---|
| Open review queue | Show objects waiting for review. | Review, Claim, Edge, NewsItem, AgentTask, ProviderCandidate | Pending objects have type, age, status, and review_status. |
| Source quality overview | Show Source tier and recoverability. | Source, Evidence, NewsItem | Sources have tier, date, locator, and license note. |
| Evidence completeness | Show Evidence records missing required metadata. | Evidence, Source | Evidence has source_id, locator, excerpt or summary, confidence, status, review_status. |
| Claim readiness | Show Claims ready or not ready for productive use. | Claim, Evidence, Review | Productive Claims have Evidence and Review status. |
| Edge review status | Show graph relationships by review state. | Edge, Entity, Evidence, Review | No productive Edge lacks Evidence and Review status. |
| News quarantine | Show NewsItems that remain raw, rumor, or quarantined. | NewsItem, Source | Tier 4 and Tier 5 material is not promoted without stronger confirmation. |
| Contradiction and disputed items | Show unresolved conflicts and outdated records. | Claim, Evidence, Review, Report | Disputed, outdated, superseded, and uncertainty cases are visible. |
| Agent task auditability | Show AgentTasks by approval and audit trail. | AgentTask, AuditLogEntry, Review | AgentTask has allowed actions, approval status, outputs, and auditability. |
| Provider candidate gate status | Show ProviderCandidates by gate readiness. | ProviderCandidate, Evidence, Review | Provider decisions are gate-based, not vendor-claim-based. |

## What Must Not Happen Yet

- No UI implementation.
- No frontend framework decision.
- No dashboard code.
- No live data ingestion.
- No scraping.
- No provider runtime integration.
- No autonomous agents.
- No premium data integration.
- No trading logic, Buy/Sell/Hold output, price target recommendation, broker integration, or investment advice.

## Future UI PR Readiness Checklist

A future UI or dashboard PR should not start until:

- [ ] Dashboard data inputs are documented.
- [ ] Required object fields are stable enough for a small prototype.
- [ ] Data quality metrics are selected for the first screen.
- [ ] Review decisions and status values are clear.
- [ ] Empty, missing, disputed, and quarantined states are handled.
- [ ] No protected full text, secrets, private data, or paywalled full-text copies are required.
- [ ] The PR scope explicitly excludes live ingestion and provider runtime integration.
- [ ] A rollback or removal path exists for prototype code.

## Dashboard Interpretation Rules

- Dashboard counts are operational signals, not truth.
- Source Tier is not a truth label.
- Review backlog is a risk signal, not a quality score by itself.
- Metrics must expose uncertainty, not hide it.
- Human Review remains final for productive Claims, Edges, and Reports.

## Boundary

This document is the readiness gate before UI work. It does not itself authorize UI implementation or dashboard code.
