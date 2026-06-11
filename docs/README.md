# ForesightGraph Documentation Index

This directory contains the core project documentation for ForesightGraph Intelligence OS.

ForesightGraph is an evidence-first, methodology-first, provider-neutral research and intelligence system. This index is only a navigation aid. It does not change project policy, roadmap scope, runtime behavior, or methodology rules.

## Core documentation

- [Active Roadmap v2](../ForesightGraph_Intelligence_OS_Roadmap_v2.md)
- [Codex Prompt Standard](../ForesightGraph_Codex_Prompt_Standard.md)
- [Architecture](architecture.md)
- [Evidence Rules](EVIDENCE_RULES.md)
- [News Source Tiers](NEWS_SOURCE_TIERS.md)
- [Review Protocol](REVIEW_PROTOCOL.md)
- [Provider Gates](PROVIDER_GATES.md)
- [Data Policy](DATA_POLICY.md)
- [Agent Control Policy](AGENT_CONTROL_POLICY.md)
- [Schema-Lite Data Model](SCHEMA_LITE.md)
- [Golden Set v2 Plan](GOLDEN_SET_V2_PLAN.md)
- [Golden Set Acceptance Criteria](GOLDEN_SET_ACCEPTANCE_CRITERIA.md)
- [Benchmark Question Design](BENCHMARK_QUESTION_DESIGN.md)
- [Manual Review Workflow](MANUAL_REVIEW_WORKFLOW.md)
- [Golden Set Release Checklist](GOLDEN_SET_RELEASE_CHECKLIST.md)
- [AgentTask Governance](AGENT_TASK_GOVERNANCE.md)
- [ProviderCandidate Governance](PROVIDER_CANDIDATE_GOVERNANCE.md)
- [Historical MVP Roadmap](roadmap.md)
- [Hermes Workflow Policy](HERMES_WORKFLOW_POLICY.md) (inactive unless explicitly re-enabled)
- [Hermes Batched Run Checklist](HERMES_BATCHED_RUN_CHECKLIST.md)

## Methodology reports

Methodology reports are stored outside this directory:

- [Methodology reports](../reports/methodology/)

These reports support evidence-first evaluation, citation accuracy, conservative wording, and methodology review.

## Tests and validation

Tests are stored outside this directory:

- [Tests](../tests/)

Important current validation areas include:

- real NVIDIA micro golden set structural checks
- conservative `nvidia_ai_004` consistency checks
- pytest CI using `python -m pytest -q`

## MVP boundaries

This documentation index does not introduce or approve:

- runtime provider integration
- Hermes configuration changes
- new dependencies
- provider SDK installation
- autonomous agents on real project files
- trading logic
- Buy/Sell/Hold outputs
- price targets
- broker or trading integration
- investment advice

## Maintenance note

Update this index when major documentation files are added, renamed, or removed.
