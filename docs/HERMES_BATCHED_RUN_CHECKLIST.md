# Hermes Batched Run Safety Checklist

## Purpose
This checklist turns the bounded batching policy into an operator-ready template for safe low-risk Hermes runs. It is intended to reduce workflow overhead and handoff friction without weakening review standards, explicit approval requirements, or safety gates.

## Bounded Batch Operating Standard for Local LLM Runs

Hermes may bundle multiple small, safe, related steps into one run when the task is explicitly approved and the risk class is low.

Use bounded batching to reduce copy/paste overhead, but never to bypass review, tests, GitHub verification, or human approval.

Allowed bundled sequences include:
- read-only audit + tests + report
- one-file docs edit + tests + PR
- approved PR merge + post-merge verification + safe branch cleanup
- temporary local file cleanup + final verification
- GitHub settings read-back verification after an approved settings change

Do not bundle unrelated risk classes. In particular, do not combine:
- new implementation with merge
- architecture change with implementation
- dependency change with provider integration
- Hermes configuration change with repository edits
- GitHub settings change with source changes
- research claim changes with methodology changes
- investment/trading logic with any project workflow

For local or auxiliary models, every bounded batch must follow these rules:
- one goal
- one repository
- one risk class
- exact branch names
- exact file paths
- exact PR number when relevant
- explicit allowed files
- explicit forbidden files
- pre-check before action
- hard stop conditions
- action only after gates pass
- verification after action
- read-back verification after GitHub settings changes
- no placeholders
- no inferred success
- no invented PR URLs
- no "or similar" file paths
- no guessed check names
- no secrets printed
- no force push
- no force delete

If a value is unavailable, Hermes must write `UNKNOWN` and stop when that value is required for a safe action.

Every reported success must be backed by command output. For GitHub settings changes, "API call succeeded" is not enough; Hermes must read the setting back and report the concrete fields.

## When to use this checklist
Use for:
- read-only audit + tests + report
- small docs PR
- small validation/test PR
- post-merge verification + branch cleanup
- approved low-risk merge + post-merge verification + branch cleanup

Do not use for:
- architecture changes
- dependency changes
- provider decisions
- Hermes configuration
- MCP / Skills / Cron / Memory / Plugins
- runtime integrations
- source/fact changes
- investment/trading claims
- secrets handling
- deployment/release workflows

## Required pre-run context
Record the following before any bundled Hermes run:
- repository path:
- current branch:
- intended branch:
- PR number if relevant:
- approved files:
- forbidden files:
- allowed commands:
- explicit human approval scope:
- expected validation commands:
- stop conditions:

## Safety gates
Confirm all applicable gates before write, merge, or cleanup actions:
- [ ] repo path verified
- [ ] repo root verified
- [ ] branch verified
- [ ] repo clean before write/merge/cleanup
- [ ] approved files only
- [ ] no source/test/dataset/config/dependency changes unless explicitly approved
- [ ] `.hermes.md` absent unless separately approved
- [ ] pytest passes
- [ ] focused pytest passes when relevant
- [ ] JSONL/eval validation passes when relevant
- [ ] GitHub checks green when relevant
- [ ] no secrets printed
- [ ] final git status clean

## Local accelerator / auxiliary model note
Hermes may prefer already-configured local or auxiliary models for low-risk acceleration tasks when available, but only within the approved primary workflow and never as a substitute for project controls.

Suitable helper tasks:
- summarization
- report drafting
- formatting
- checklist prefill
- simple classification
- non-authoritative comparison

Rules:
- The local model output is helper output only.
- It must not replace tests, GitHub checks, human review, ChatGPT review, or explicit approval.
- Hermes must not change model routing or configuration.
- Hermes must not start or stop Ollama, Docker, containers, or services.
- Hermes must not pull or download models.
- Hermes must not print secrets.
- Critical decisions must not be delegated to local helper models.
- Merge, architecture, provider, dependency, Hermes config, MCP, Skills, Cron, Memory, Plugin, runtime, and investment/trading decisions must not be delegated to a local helper model.
- If local routing is unavailable or uncertain, Hermes should continue with the approved primary route and report that local acceleration was not used.

## Merge + cleanup bundled run checklist
Use this section only for explicitly approved low-risk PRs:
- [ ] explicit PR-specific human approval exists
- [ ] PR is open
- [ ] PR diff matches approved files
- [ ] tests/checks pass
- [ ] PR marked ready only after gates pass
- [ ] merge only after gates pass
- [ ] post-merge verification passes
- [ ] cleanup only after PR is merged and branch is safely merged into main
- [ ] safe delete only
- [ ] no force delete
- [ ] only approved feature branch deleted

## Required final report
Every bundled run should report:
- executive summary
- files inspected
- files changed
- tests/checks
- validation result
- PR URL
- commit hash
- merge status if relevant
- cleanup status if relevant
- failed gates if any
- forbidden actions avoided
- exactly one recommended next action
- ChatGPT handoff block
