# Data Quality Metrics

## Purpose

Data quality metrics help ForesightGraph decide whether Sources, Evidence, Claims, Edges, NewsItems, Reviews, Reports, AgentTasks, and ProviderCandidates are ready for review, Golden Set use, or later tooling.

Metrics are decision-support signals, not absolute truth. They should guide review and prioritization, but they do not replace Evidence, Source Tiers, Review status, or human judgment.

This document is compatible with future validators, but does not implement validators, schemas, dashboards, runners, or application code.

## Metric Set

| Metric | Measures | Why it matters | Minimum useful signal | Related objects |
|---|---|---|---|---|
| Source quality | Source tier, recoverability, source date or accessed date, license note, and locator presence. | Weak or unrecoverable Sources weaken every downstream object. | Source has tier, locator, date metadata, and license note. | Source, Evidence, NewsItem |
| Evidence completeness | Evidence has `source_id`, locator, excerpt or summary, evidence type, confidence, status, and review_status. | Evidence is the bridge between Sources and productive Claims or Edges. | Evidence can be traced back to one Source and one precise locator. | Evidence, Source, Claim, Edge |
| Locator precision | Locator points to a specific URL, page, section, paragraph, table, figure, or timestamp. | Reviewers must be able to reproduce the evidence trail. | Locator is specific enough for another reviewer to find the support. | Source, Evidence, Claim, Edge, Report |
| Claim readiness | Claim is atomic, evidence-backed, status-bearing, confidence-bearing, and reviewed or ready for review. | Claims are the core factual units of the system. | Claim has Evidence references, status, review_status, and `last_checked` where relevant. | Claim, Evidence, Entity, Edge |
| Entity quality | Entity has stable name, type, aliases or identifiers when useful, and review_status. | Ambiguous Entities create false Claims and Edges. | Entity can be distinguished from similarly named objects. | Entity, Claim, Edge |
| Edge quality | Edge has clear source and target Entities, relationship type, Evidence, status, and review_status. | Edges shape the graph and can mislead if under-evidenced. | No productive Edge exists without Evidence and Review status. | Edge, Entity, Evidence, Claim |
| News verification quality | NewsItem has Source Tier, publication metadata, quarantine or review status, and no full-text copy. | News is raw material and must not become fact too early. | NewsItem remains draft, quarantined, or reviewed before supporting Claims. | NewsItem, Source, Evidence, Claim |
| Review throughput | Count and age of objects in `needs_review`. | Stale review queues hide risk and slow progress. | Review backlog and oldest pending item are visible. | Review, Claim, Edge, NewsItem, ProviderCandidate, AgentTask |
| Review accuracy | Rate of accepted, rejected, disputed, quarantined, superseded, or corrected items. | Review decisions should improve quality, not rubber-stamp outputs. | Review outcomes include notes and can be audited. | Review, Claim, Edge, Report |
| Contradiction handling | Disputed, outdated, superseded, and uncertainty cases are marked and traceable. | Contradictions are core evidence, not noise to hide. | Contradiction or uncertainty cases have status and follow-up notes. | Claim, Evidence, Review, Report |
| Golden Set readiness | Golden Set records meet acceptance criteria and versioning guidance. | Golden Sets anchor repeatable evaluation. | Required metadata, version, review outcome, and boundary checks are present. | Source, Evidence, Claim, Entity, Edge, NewsItem, Report, AgentTask |
| AgentTask auditability | AgentTask has allowed actions, approval status, outputs, checks, and audit trail. | Agent work must be reviewable and bounded. | AgentTask has approval status and AuditLogEntry or equivalent report trail. | AgentTask, AuditLogEntry, Review |
| ProviderCandidate gate readiness | ProviderCandidate has gate status, evidence, security, license, cost, lock-in, and review notes. | Providers must be evaluated, not accepted from vendor claims alone. | Fit, Evidence, Security, Evaluation, License, Cost/Latency, Maintainability, Lock-in, and Adoption gates are addressed. | ProviderCandidate, Evidence, Review |
| Report traceability | Report links back to Sources, Evidence, Claims, status, and review_status. | Reports must not present unreviewed objects as confirmed knowledge. | Report can be traced to reviewed Claims and Evidence. | Report, Source, Evidence, Claim, Review |

## Metric Interpretation

- A high metric value is not proof of truth.
- A low metric value is a review priority signal.
- Metrics should preserve uncertainty and source-tier limits.
- Tier 4 and Tier 5 material must not become productive fact through scoring alone.
- ProviderCandidate metrics must remain gate-based, not vendor-claim-based.
- AgentTask metrics must measure auditability, not grant autonomy.

## Future Validator Compatibility

Future validators may turn these metrics into checks, but this document does not implement them.

Validator-ready checks should prefer simple outcomes:

```text
pass
fail
needs_review
not_applicable
```

Any future validator must still preserve human Review for productive Claims, Edges, and Reports.

## Boundaries

This document does not approve:

- real data ingestion;
- runtime schemas;
- validators;
- benchmark runners;
- UI or dashboard code;
- GraphRAG;
- Vector DB;
- provider runtime integration;
- live ingestion or scraping;
- autonomous agents;
- premium data;
- trading logic or investment advice.
