---
title: "ForesightGraph Codex Prompt Standard"
version: "1.0"
date: "2026-06-11"
status: "Project source / Codex workflow standard"
language: "de"
project: "ForesightGraph Intelligence OS"
intended_use: "Kompakter Standard fuer kontrolliert-autonome Codex-Aufgaben"
---

# ForesightGraph Codex Prompt Standard

## 1. Zweck

Dieses Dokument definiert, wie Codex-Prompts fuer ForesightGraph formuliert werden sollen.

Ziel ist:

```text
mehr Autonomie fuer Codex,
aber nur innerhalb klarer Projekt-, Sicherheits- und Review-Grenzen.
```

Codex soll zusammenhaengende kleine Aufgaben effizient buendeln duerfen, aber keine Architektur-, Provider-, Daten-, Sicherheits- oder Investment-Grenzen ueberschreiten.

## 2. Kanonische Projektquelle

Die aktive Projektquelle ist:

```text
ForesightGraph_Intelligence_OS_Roadmap_v2.md
```

Bei Konflikten gilt immer die Roadmap v2.

## 3. Grundprinzip

```text
Ein Codex-Prompt = ein klares Ziel + ein Risiko-Profil + ein pruefbarer Pull Request.
```

Codex soll nicht „das ganze Projekt bauen“, sondern einen zusammenhaengenden Roadmap-Schritt umsetzen.

## 4. Wann Aufgaben gebuendelt werden duerfen

Codex darf mehrere kleine Aufgaben in einem Prompt buendeln, wenn sie:

- dasselbe Roadmap-Ziel unterstuetzen,
- denselben Repo-Bereich betreffen,
- dasselbe Risiko-Profil haben,
- gemeinsam testbar oder reviewbar sind,
- keine neue Architekturentscheidung erzwingen.

Gute Buendel-Beispiele:

```text
Evidence Rules
News Source Tiers
Review Protocol
Provider Gates
Data Boundaries
README-Links
```

Nicht gemeinsam buendeln:

```text
Methodik + UI
Evidence Rules + Live-Daten-Ingestion
Doku + Provider-Runtime
Graph-Schema + GraphRAG
Research-Daten + Trading-Logik
Repo-Hygiene + Release/Deployment
```

## 5. Eigenschaften eines guten Codex-Prompts

Jeder Codex-Prompt soll diese Bloecke enthalten:

```text
Mode
Task size
Decision freedom
Goal
Project source
Context
Scope
Out of scope
Allowed changes
Forbidden changes
Implementation rules
Tests/checks
Stop rules
Done when
Final report
```

## 6. Autonomie-Regel

Codex darf innerhalb des definierten Scopes selbst entscheiden:

- welche bestehenden Dateien verbessert werden,
- ob kleine neue Markdown-, Template-, Schema- oder Testdateien sinnvoll sind,
- ob README-Links ergaenzt werden,
- welche bestehenden Checks auszufuehren sind,
- ob kleine Inkonsistenzen im beruehrten Scope korrigiert werden.

Codex muss stoppen und berichten bei:

- fehlender Roadmap v2,
- unklarer Repo-Struktur,
- neuen Dependencies,
- Architekturkonflikten,
- Security-, Secret-, Lizenz- oder Datenrisiken,
- produktiven Claims, Edges oder Reports,
- Investment-/Trading-Ausgaben,
- Scope-Ausweitung ueber die definierte Phase hinaus.

## 7. Feste Grenzen

Codex darf nicht:

- direkt auf `main` pushen,
- Pull Requests selbst mergen,
- Tags, Releases oder Deployments erstellen,
- neue Dependencies ohne Stop-Bericht einbauen,
- Provider-SDKs oder Runtime-Integrationen ungefragt einfuehren,
- UI, GraphRAG, Vector DB oder Premium-Daten starten, wenn nicht explizit im Scope,
- autonome Agenten produktiv einsetzen,
- geschuetzte News-Volltexte speichern,
- Secrets, Tokens oder private Daten ausgeben,
- Trading-Logik, Buy/Sell/Hold-Ausgaben, Kursziele oder Broker-Integration erzeugen.

## 7a. Codex-first workflow

Der aktive Workflow ist Codex-first. Hermes ist nicht Teil des aktiven Workflows, sofern ein Task Hermes nicht ausdruecklich wieder freigibt.

Codex darf Low-Risk-Dokumentations- oder Test-PRs nur dann selbst mergen, wenn der jeweilige Task dies ausdruecklich delegiert und alle Safety Gates bestehen. Kritische Aenderungen muessen immer stoppen und berichtet werden.

## 8. Standardvorlage fuer kontrolliert-autonome Codex-Prompts

```text
Mode:
Controlled autonomous implementation

Task size:
Medium bounded batch

Decision freedom:
Medium within the defined scope.
Do not ask for confirmation for small directly related decisions.
Stop and report for architecture, dependency, security, data, provider, licensing, investment or scope-risk decisions.

Goal:
Implement [ROADMAP_PHASE_OR_WORK_PACKAGE] from `ForesightGraph_Intelligence_OS_Roadmap_v2.md` as the next smallest useful project step.

Project source:
Use `ForesightGraph_Intelligence_OS_Roadmap_v2.md` as the canonical project source.
If it is missing, stop and report.
If older files conflict with Roadmap v2, follow Roadmap v2 and report the conflict.

Context:
ForesightGraph Intelligence OS is a local-first, evidence-first and provider-neutral Research-Agent-System with a future Windows-oriented Intelligence Workbench.
The project first builds a reliable Evidence and Methodology Core before UI, GraphRAG, Vector DB, agent runtimes or premium data.
NVIDIA is the first Reference Track, but not the project name, not a core dependency, not an official partnership and not a vendor lock-in.

Scope:
[LIST INCLUDED SUBTASKS]

Out of scope:
[LIST EXPLICIT EXCLUSIONS]

Allowed changes:
- Inspect the repository structure.
- Improve existing relevant files instead of creating duplicates.
- Create small Markdown, template, schema or test files only if directly needed.
- Update README links if useful.
- Run existing tests, linters, validators or documentation checks.
- Keep all changes inside the defined roadmap phase.

Forbidden changes:
- Do not push directly to `main`.
- Do not merge the PR.
- Do not create releases, tags or deployments.
- Do not add dependencies without stopping first.
- Do not add provider SDKs or runtime integrations.
- Do not implement UI unless explicitly in scope.
- Do not implement GraphRAG.
- Do not add a Vector DB.
- Do not add live news ingestion or scraping unless explicitly in scope.
- Do not store copyrighted full-text news content.
- Do not add trading logic, Buy/Sell/Hold outputs, price targets, broker integration or investment advice.
- Do not expose secrets, tokens, credentials or private data.

Implementation rules:
- Keep changes minimal, complete and reviewable.
- Bundle only tasks with the same goal and risk profile.
- Prefer existing repo conventions.
- Keep documentation practical and non-duplicative.
- Productive Claims and Edges must require Evidence and Review status.
- NewsItems are raw material, not confirmed facts.
- Tier 4 and Tier 5 sources must not become productive facts without stronger confirmation.
- Agent outputs are drafts until reviewed.
- Provider decisions require gates: Fit, Evidence, Security, Evaluation, License, Cost/Latency, Maintainability, Lock-in and Adoption.

Tests/checks:
- Run existing tests/checks if available.
- Run Markdown/documentation checks if available.
- If no tests/checks exist, report that clearly.
- Never claim tests passed unless they were actually run.

Stop rules:
Stop and report instead of improvising if:
- Roadmap v2 is missing,
- repo structure is unclear,
- required files conflict with Roadmap v2,
- new dependencies are required,
- work would exceed the defined roadmap phase,
- security, secret, licensing or data boundary risks appear,
- productive Claims, Edges, Reports or investment outputs would be affected,
- tests cannot be run,
- branch or GitHub state is unsafe.

Done when:
- The requested roadmap work package is complete.
- Related small tasks are bundled only where coherent.
- No forbidden scope was introduced.
- Files changed are minimal and reviewable.
- Tests/checks are run or clearly reported as unavailable.
- A Pull Request is created.
- The final report is factual and contains no placeholders.
- If the task explicitly delegates low-risk merge permission, Codex may merge only after every stated safety gate passes; otherwise do not merge.

Final report:
Return exactly this report:

1. Branch:
2. Pull Request:
3. Roadmap phase/work package:
4. Files inspected:
5. Files created:
6. Files changed:
7. Tests/checks run:
8. Tests/checks result:
9. Bundled tasks completed:
10. Scope confirmation:
11. Forbidden items avoided:
12. Autonomy decisions made:
13. Stop-rule issues:
14. Open questions:
15. Recommended next step:

Do not merge the PR.
```

## 9. Empfohlener erster Einsatz

Naechster sinnvoller Codex-Lauf:

```text
Goal:
Implement Phase 1: Methodology Foundation.

Scope:
Evidence Rules, News Source Tiers, Review Protocol, Provider Gates, Agent Control Policy, Data Boundaries and minimal templates if useful.

Out of scope:
UI, GraphRAG, Vector DB, provider runtime integration, live data ingestion, autonomous agents, premium data, trading logic.
```

## 10. Kurzregel

```text
Codex bekommt Autonomie im Weg,
aber keine Autonomie bei Grenzen.
```
