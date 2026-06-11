# AGENTS.md

## Arbeitsregeln für Cline

- Dieses Projekt darf nur innerhalb dieses Repository-Ordners bearbeitet werden.
- Keine Änderungen außerhalb von `C:\AI\projects\foresightgraph`.
- Kanonische aktive Projektquelle: `ForesightGraph_Intelligence_OS_Roadmap_v2.md`.
- Priorität bei Konflikten: Roadmap v2 > Codex/Hermes prompt standards > einzelne Task-Prompts > historische Roadmaps.
- Codex muss kontrolliert und PR-basiert arbeiten: Feature-Branch verwenden, kleine geprüfte Änderungen, kein direkter Push auf `main`.
- Aktiver Workflow ist Codex-first; Hermes ist nur aktiv, wenn es ausdrücklich wieder freigegeben wird.
- Delegierte Low-Risk-Merges durch Codex sind nur erlaubt, wenn der Task dies ausdrücklich erlaubt und alle Safety Gates bestehen.
- Zuerst nur analysieren, nicht ändern.
- Dateien nur nach ausdrücklicher Freigabe ändern.
- Keine Git-Commits ohne ausdrückliche Freigabe.
- Keine Paketinstallationen ohne ausdrückliche Freigabe.
- Keine externen Dienste, Browser, MCP-Server oder API-Keys verwenden.
- Nach Änderungen immer `git diff`, Tests und `git status` prüfen.
- Codex workflow standard: see `ForesightGraph_Codex_Prompt_Standard.md`
- Agent control policy: see `docs/AGENT_CONTROL_POLICY.md`
- Hermes workflow policy, inactive unless explicitly re-enabled: see docs/HERMES_WORKFLOW_POLICY.md
