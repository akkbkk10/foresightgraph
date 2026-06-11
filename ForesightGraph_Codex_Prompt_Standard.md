# ForesightGraph Codex Prompt Standard

## Purpose

This file defines the Codex workflow standard for ForesightGraph Intelligence OS.

## Source priority

Codex must use this priority order for project work:

1. `ForesightGraph_Intelligence_OS_Roadmap_v2.md`
2. `ForesightGraph_Codex_Prompt_Standard.md` and `docs/HERMES_WORKFLOW_POLICY.md`
3. Individual task prompts
4. Historical roadmap or planning documents

If a task prompt conflicts with Roadmap v2, stop and report the conflict before making changes.

## Controlled PR-based work

Codex work in this repository must be controlled, bounded, and Pull Request based:

- Work on a feature branch, not directly on `main`.
- Keep changes inside `C:\AI\projects\foresightgraph`.
- Keep edits within the approved scope.
- Do not install dependencies unless explicitly approved.
- Do not create tags, releases, deployments, or merges unless explicitly approved.
- Do not expose secrets, tokens, or private data.
- Run relevant existing checks before reporting completion.
- Report `git diff`, checks, and `git status` outcomes after changes.

## Documentation sync rules

Documentation updates may align README, AGENTS, roadmap, and workflow policy references when the scope is explicit and bounded. Documentation updates must not introduce architecture changes, provider integrations, autonomous agents, trading outputs, or implementation work unless separately approved.
