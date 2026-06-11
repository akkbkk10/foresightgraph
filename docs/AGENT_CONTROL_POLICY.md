# Agent Control Policy

## Purpose

This document defines the active agent workflow for ForesightGraph Phase 1. It is governed by `../ForesightGraph_Intelligence_OS_Roadmap_v2.md` and `../ForesightGraph_Codex_Prompt_Standard.md`.

## Active Workflow

- Codex is the primary implementation and review agent for repository work.
- ChatGPT reviews Codex reports and provides architecture, planning, and prompt guidance.
- The user remains the final authority for critical architecture, product, security, data, provider, licensing, release, and investment-boundary decisions.
- Hermes is not part of the active workflow unless the user explicitly re-enables it in a later task.

## Codex Responsibilities

Codex may:

- inspect repository state and changed files;
- create bounded documentation or test Pull Requests;
- run existing checks and report factual results;
- self-review low-risk changes when the task explicitly allows it;
- merge low-risk documentation or test PRs only when the task explicitly delegates merge permission and every safety gate passes.

Codex must not treat its own output as final truth for productive Claims, Edges, Signals, or Reports. Agent outputs remain drafts until reviewed under the Review Protocol.

## Delegated Low-Risk Merge Rule

Codex may self-review and merge a PR only when all conditions are true:

1. The task explicitly delegates merge permission.
2. The PR is low-risk documentation or test work, or another explicitly approved low-risk scope.
3. The branch is not `main`.
4. The PR targets `main`.
5. Changed files are exactly within the expected scope.
6. Tests pass.
7. `git diff --check` passes.
8. GitHub checks pass.
9. The diff contains no forbidden content.
10. The repository is clean after merge.
11. The final report is factual and includes checks, merge status, cleanup status, blockers, and next step.

If any gate fails or is unclear, Codex must not merge and must report the blocker.

## Critical Stop Boundaries

Codex must stop and report before changing or approving:

- dependencies;
- provider or runtime integration;
- UI implementation;
- GraphRAG;
- Vector DB;
- live data ingestion or scraping;
- autonomous agents;
- premium data integrations;
- productive Claims, Edges, Signals, or Reports;
- data licensing risks;
- secrets, tokens, credentials, or private data;
- security policy changes;
- releases, tags, deployments, or GitHub settings;
- trading logic, Buy/Sell/Hold outputs, price targets, broker integration, or investment advice.

## Forbidden Agent Behavior

Codex must not:

- push directly to `main` outside a GitHub PR merge;
- auto-merge critical changes;
- install dependencies without explicit approval;
- expose secrets, tokens, credentials, or private data;
- store copyrighted full-text news or paywalled article copies;
- finalize productive research objects without human Review;
- create releases, tags, or deployments without explicit approval.

## Required Merge-Gate Report

A delegated merge report must state:

- PR and branch;
- base branch;
- changed files;
- safety-gate result;
- tests and checks run;
- merge status and merge commit if merged;
- post-merge verification result;
- branch cleanup result;
- open PRs after merge;
- blockers;
- recommended next step.
