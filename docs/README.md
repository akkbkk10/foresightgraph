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
- [Historical MVP Roadmap](roadmap.md)
- [Hermes Workflow Policy](HERMES_WORKFLOW_POLICY.md)
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
