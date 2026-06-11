# Architecture Decision Records

## Purpose

Architecture Decision Records (ADRs) document significant ForesightGraph decisions so they can be reviewed, revisited, and audited. ADRs are for decisions that affect project direction, technology choices, data boundaries, provider adoption, runtime behavior, or long-term maintainability.

This is documentation guidance only. It does not approve implementation work.

## When an ADR Is Required

Create an ADR before:

- major technology choices;
- provider or runtime integration;
- UI or dashboard implementation;
- GraphRAG;
- Vector DB;
- live ingestion or scraping;
- premium data integration;
- security or data-boundary policy changes;
- architecture changes that affect multiple modules;
- decisions that need benchmark evidence or a Roadmap gate.

Major technology decisions need benchmark evidence or a clear Roadmap gate before implementation.

## When an ADR Is Not Required

An ADR is usually not required for:

- small documentation updates;
- typo fixes;
- link updates;
- narrow test documentation;
- changes already covered by an accepted ADR and current task scope;
- low-risk planning docs that do not approve implementation.

## ADR Status Values

```text
proposed
accepted
rejected
superseded
needs_benchmark
needs_review
```

## Minimum ADR Fields

An ADR should include:

- `id`
- `title`
- `status`
- `date`
- `decision_owner`
- `context`
- `decision`
- `options_considered`
- `evidence_or_benchmark_reference`
- `risks`
- `consequences`
- `rollback_or_revisit_trigger`
- `related_docs`

## Decision Boundaries

ADRs may document and evaluate options, but they must not bypass safety gates. These areas require explicit gates before implementation:

- UI;
- GraphRAG;
- Vector DB;
- provider runtime integration;
- live ingestion or scraping;
- premium data;
- autonomous agents;
- releases, tags, or deployments.

ADRs must not introduce secrets, private data, protected full text, trading logic, Buy/Sell/Hold outputs, price targets as recommendations, broker integration, or investment advice.

## Related Docs

- `ForesightGraph_Intelligence_OS_Roadmap_v2.md`
- `PROVIDER_GATES.md`
- `PROVIDER_CANDIDATE_GOVERNANCE.md`
- `PROVIDER_EVALUATION_NOTES.md`
- `DATA_POLICY.md`
- `AGENT_CONTROL_POLICY.md`
- `REVIEW_PROTOCOL.md`
