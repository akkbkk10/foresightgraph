# ForesightGraph Hermes Workflow Policy

## Purpose
Hermes wird in ForesightGraph als begrenztes Orchestrations‑ und Ausführungswerkzeug eingesetzt. Ziel ist, strukturierte Untersuchungen, Prüfungen, Validierungen und nachvollziehbare Audit‑Reports zu ermöglichen, ohne dass Hermes ungeprüfte Änderungen am Code, an der Konfiguration oder an persistenter Projektinfrastruktur vornimmt.

## Roles
- Human user / maintainer
  - Endgültige Entscheidungsinstanz für Code, Merges, Architektur, Provider‑ und Betriebsentscheidungen.
- ChatGPT reviewer / prompt author
  - Autor und Prüfer von Prompts, liefert höhere‑level Review, Validierungs‑Urteile und formuliert Prüfpflichten.
- Hermes executor / reporter
  - Führt ausdrücklich erlaubte, dokumentierte Tasks aus (Lesen, Tests, Validierung, strukturierte Berichte). Liefert den verbindlichen Task‑Report an Human/ChatGPT.
- GitHub as audit trail
  - Alle genehmigten Änderungen müssen durch Pull Requests, Review und Merge in GitHub nachvollziehbar sein.

## Autonomy levels
- read_only
  - Nur Lesen: Dateien lesen, Status prüfen, Tests ausführen, Validierungen.
- audit
  - Erweitertes Lesen + Berichte: zusätzlich Erzeugen strukturierter Audit‑Reports, Checklisten‑Füllung, Vorschläge für Dokumentationstexte.
- edit_allowed
  - Schreibzugriff auf eindeutig genehmigte, enge Dokumentationsscope (z. B. docs/HERMES_WORKFLOW_POLICY.md). Erfordert explizite menschliche Genehmigung vor Commit/Push.
- merge_allowed_low_risk
  - Sehr eng begrenzte Merges (z. B. winzige Dokumentations‑PRs) nur nach expliziter menschlicher Zustimmung und nach Bestehen aller Safety Gates.
- forbidden_without_RFC
  - Höhere Risiken (Architektur, CI, Dependencies, Cron, MCP, Skills, Memory, Plugins) sind verboten ohne separaten RFC + Review + explizite Genehmigung.

## Low‑risk actions Hermes may perform with explicit approval
- Lesen des Repository‑Zustands (git status, git log, branch list).
- Ausführen von Tests/Checks (z. B. python -m pytest -q) und Melden der Ergebnisse.
- Validierung von JSONL/Schema Dateien (z. B. evals/golden_sets/*.jsonl).
- Erzeugen von Dokumentations‑Branches und Draft‑PRs mit ausschließlich dokumentationsbezogenen Änderungen (docs/ oder README/kleine Link‑Anpassungen), wenn vorher genehmigt.
- Commit/Push von eng gefasstem Dokumentations‑Content (nur nach menschlicher Prüfung und Zustimmung vor Commit).
- Merge von kleinen Dokumentations‑PRs nur nach: (1) Hermes‑Report, (2) ChatGPT‑Review falls angefordert, (3) ausdrücklicher menschlicher Merge‑Bestätigung.
- Löschen gemergter Feature‑Branches nur nach ausdrücklicher Zustimmung und nach Verifikation, dass keine ungeprüften Änderungen verloren gehen.

## Critical actions that must return to ChatGPT/user
Hermes MUSS bei folgenden Aktionen stoppen, einen vollständigen Task‑Report erzeugen und menschliche/ChatGPT‑Review anfordern:
- Architekturänderungen oder -vorschläge mit Auswirkung auf Design/Modulstruktur.
- Hinzufügen oder Aktualisieren von Projekt‑Dependencies.
- CI/CD Konfiguration oder Workflow‑Änderungen.
- Runtime‑Integrationen oder dauerhaft laufende Dienste (Gateways, Cronjobs, MCP Servers).
- Provider‑Entscheidungen oder API‑Key Aufnahme/Rotation.
- Code‑Änderungen außerhalb des eng genehmigten Dokumentations‑Scopes.
- Änderungen an Hermes Konfiguration (~/.hermes/config.yaml) oder projektweiten .hermes.md‑Dateien.
- Aktivierung oder Erzeugung von Skills, Cronjobs, Memory‑Einträgen oder Plugins.
- Einführung neuer Quellen/Fakten oder forschungsrelevante Schlussfolgerungen ohne menschliche Überprüfung.
- Inhalte mit Investment/Trading‑Relevanz oder rechtliche/advisory Implikationen.

## MVP forbidden features
Während der MVP‑Phase sind folgende Features untersagt:
- Hinzufügen einer .hermes.md zum Repository.
- Änderungen an Hermes Einstellungen oder Konfigurationen.
- Erzeugung persistenter, vom Agenten selbst geschriebener Skills.
- Autonome Cronjobs oder Scheduler‑Aktivierung.
- Breite MCP‑Aktivierung oder Verbindung zu externen MCP‑Servern.
- Multi‑Agent Kanban/Dispatcher‑Setups.
- Entwicklung oder Installation von Kern‑Hermes‑Plugins in diesem Repo.
- Automatische Schreibzugriffe auf Memory oder persistente Agenten‑Speicher.
- Automatische, unüberwachte Merges in Code oder risky PRs.
- Kopieren von Hermes Quellcode in dieses Projekt.

## Context‑file policy
- AGENTS.md bleibt die kurze, kanonische Quelle für Repo‑Agentenregeln.
- Detaillierte Hermes‑Betriebsregeln leben in docs/HERMES_WORKFLOW_POLICY.md.
- .hermes.md darf nicht hinzugefügt werden ohne separaten PR, Review und explizite Präzedenzklärung in AGENTS.md.

## Standard Hermes task report template (verlangt)
Jeder Hermes‑Task muss einen strukturierten Report liefern; dieses kompakte Format ist verbindlich:
- task_id: <string>
- mode: read_only | audit | edit_allowed | merge_allowed_low_risk
- repo_path: C:\AI\projects\foresightgraph
- branch: <branch-name>
- git_status_before: <git status -sb>
- files_inspected: [ ... ]
- files_changed: [ ... ]
- commands_run: [ {cmd: "python -m pytest -q", exit_code: 0, summary: "..."}, ... ]
- tests_result: { exit_code: N, summary: "x passed, y failed" }
- validation_result: short summary or snippet
- pr_url: <if applicable>
- commit_hash: <if applicable>
- push_merge_result: <if applicable>
- source_evidence_status: [ {source_id|url, status, note}, ... ]
- safety_gates_passed: [ ... ]
- safety_gates_failed: [ ... ]
- forbidden_actions_attempted: yes|no + details
- merge_readiness: READY | NOT_READY + reason
- recommended_next_action: single clear sentence
- chatgpt_handoff_block: compact summary for ChatGPT/human reviewer
- web_tooling_preflight:
  required: yes|no
  docker_status: running|not_running|unknown
  firecrawl_status: running|stopped|unreachable|unknown
  searxng_status: running|stopped|unreachable|unknown
  web_extract_status: success|failed|not_attempted
  fallback_used: yes|no
  failure_category: Docker not running|Firecrawl unavailable|SearXNG unavailable|env var missing|Hermes backend not configured|local LLM routing issue|page extraction issue|unknown

## Standard ChatGPT→Hermes prompt rules (verbindlich)
Jeder Prompt von ChatGPT an Hermes MUSS folgende Konventionen einhalten:
1. one autonomous prompt only — ein zusammenhängender Auftrag pro Run.
2. clear mode — deklariere mode=read_only|audit|edit_allowed|merge_allowed_low_risk.
3. known state — füge repo_path, branch, git_status_before, commit_hash bei.
4. autonomy level — liste erlaubte Toolsets und Kommandos (z. B. read_file, search_files, terminal:pytest).
5. allowed actions — genaue Auflistung der erlaubten Aktionen.
6. forbidden actions — eindeutige Aufzählung (push, merge, write_file, config set, cron create, skill publish, etc.).
7. safety gates — Bedingungen, die erfüllt sein müssen (z. B. tests exit_code==0, no_schema_errors).
8. stop conditions — bei Gate‑Fehlschlag: sofort stoppen, Report erstellen, human notify.
9. If the task requires live web sources, include a Web Tooling Preflight section that requires Hermes to run preflight checks listed below before any web_search/web_extract/source verification or live citation checking.
10. exact output structure — zwingend das "Standard Hermes task report template" plus eine einzige empfohlene nächste Aktion.
11. one next action only — am Ende genau eine atomare Handlungsempfehlung.

### Web Search / Web Extraction Preflight
Add a short preflight block to prompts that need live web sources. The preflight must verify local web tooling availability and not assume LLM as primary failure cause.
- Local tooling in use:
  - SearXNG for web search
  - Firecrawl for web extraction/page retrieval
- First checks (before attempting extraction):
  - Docker running
  - Firecrawl container running
  - SearXNG container running (if search required)
  - Firecrawl API reachable
  - SearXNG reachable
  - Relevant env vars visible to Hermes (FIRECRAWL_API_URL, FIRECRAWL_API_KEY, SEARXNG_URL)
  - Hermes web backend configured
- Allowed preflight commands (check only):
  - docker ps
  - docker ps -a
  - docker compose ls
  - hermes tools
  - hermes config check
  - check presence only of FIRECRAWL_API_URL, FIRECRAWL_API_KEY, SEARXNG_URL
  - safe HTTP status checks to configured local Firecrawl/SearXNG URLs
- Forbidden preflight actions (without explicit user approval):
  - do not start/stop/restart Docker or containers
  - do not run docker compose up
  - do not change Hermes config
  - do not edit .env
  - do not print secrets
- Failure behavior:
  - If Docker, Firecrawl or SearXNG is unavailable, Hermes must stop and report.
  - Do not silently rely on local skill summaries.
  - Do not claim primary‑source verification if web extraction failed.
  - Report likely failure category: Docker not running | Firecrawl unavailable | SearXNG unavailable | env var missing | Hermes backend not configured | local LLM routing issue | page extraction issue | unknown

## Legal / attribution note
- Konzepte und Muster aus Hermes dürfen als Workflow‑Ideen verwendet werden.
- Kopieren von Hermes Quellcode ist nicht erlaubt ohne gesonderte Lizenz‑ und Attribution‑Prüfung.
- Jede spätere Code‑Wiederverwendung bedarf separater rechtlicher Prüfung und PR mit Lizenzhinweis.

## Review cadence
- Policy‑Änderungen dürfen nur per Review‑PR erfolgen.
- Diese Policy wird nach realer Hermes‑Nutzung erneut überprüft und angepasst.
