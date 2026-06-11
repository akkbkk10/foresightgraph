# AgentTask Governance

## Purpose

This document defines how AgentTask records should be planned, reviewed, and audited in Phase 1. It supports the Codex-first workflow in `AGENT_CONTROL_POLICY.md` and the schema-lite object model in `SCHEMA_LITE.md`.

Hermes is not part of the active workflow unless the user explicitly re-enables it in a later task.

## AgentTask Record

Purpose: document bounded agent work before it is accepted into project history or used to support productive research objects.

Recommended fields:

- `id`
- `agent_name`
- `task_type`
- `goal`
- `allowed_actions`
- `forbidden_actions`
- `input_refs`
- `output_refs`
- `approval_status`
- `review_status`
- `created_at`
- `updated_at`

## Approval Status Values

```text
draft
approved_for_read_only
approved_for_docs
approved_for_tests
approved_for_low_risk_merge
needs_review
blocked
completed
rejected
superseded
```

## Allowed Action Categories

Allowed actions must be explicitly scoped. Examples:

- repository inspection;
- documentation edits;
- test or check execution;
- PR creation;
- low-risk docs/test merge only when explicitly delegated and all safety gates pass;
- post-merge verification;
- safe branch cleanup after successful merge and tests.

## Forbidden Action Categories

AgentTasks must stop and report before:

- dependencies;
- provider or runtime integration;
- UI implementation;
- GraphRAG;
- Vector DB;
- live data ingestion or scraping;
- autonomous agents;
- premium data integrations;
- productive Claims, Edges, Signals, or Reports;
- security policy changes;
- data licensing risk;
- secrets, tokens, credentials, or private data;
- protected full-text storage;
- releases, tags, deployments, or GitHub settings;
- trading logic, Buy/Sell/Hold outputs, price targets, broker integration, or investment advice.

## Codex-First Delegated Merge Behavior

Codex may self-review and merge a low-risk documentation or test PR only when:

1. the task explicitly delegates merge permission;
2. the branch is not `main`;
3. the PR targets `main`;
4. changed files are inside the approved scope;
5. tests pass;
6. `git diff --check` passes;
7. GitHub checks pass;
8. no forbidden content or scope expansion is present;
9. post-merge verification passes;
10. a factual final report is provided.

Codex must not auto-merge critical changes.

## AuditLogEntry Relationship

Every meaningful AgentTask should have an AuditLogEntry or equivalent report trail that records:

- actor;
- action;
- object or PR reference;
- timestamp;
- result;
- checks run;
- blockers;
- follow-up recommendation.

Audit entries must not expose secrets, tokens, credentials, private data, or protected full text.

## Productive Research Boundary

AgentTask outputs are drafts. They must not autonomously finalize productive Claims, Edges, Signals, or Reports. Human Review remains final for productive research objects.
