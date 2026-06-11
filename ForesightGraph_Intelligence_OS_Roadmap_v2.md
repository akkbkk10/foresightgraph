---
title: "ForesightGraph Intelligence OS - Roadmap v2"
version: "2.0"
date: "2026-06-11"
status: "Project source candidate / Roadmap"
language: "de"
project: "ForesightGraph Intelligence OS"
intended_use: "Projektquelle fuer Roadmap, Architektur, Methodik, Open-Source-Grenzen und kontrollierte Agentenarbeit"
financial_disclaimer: "Research-Unterstuetzung; keine Anlageberatung; keine Kauf-, Verkaufs- oder Halteempfehlung."
---

# ForesightGraph Intelligence OS - Roadmap v2

## 1. Kernaussage

ForesightGraph Intelligence OS wird als local-first, evidence-first und provider-neutrales Research-Agent-System mit visueller Windows-orientierter Intelligence Workbench aufgebaut.

Der Core bleibt methodisch pruefbar: Jede wichtige Aussage benoetigt Quelle, Datum, Locator, Claim-Status und Review-Status. NVIDIA bleibt der erste fachliche Reference Track, aber nicht Projektname, nicht Core-Abhaengigkeit, nicht offizielle Partnerschaft und kein Vendor-Lock-in.

Die Roadmap v2 verschiebt den Schwerpunkt von einer reinen Architektur-Roadmap zu einer produktfaehigen, aber kontrollierten Research-Workbench: Quellen erfassen, Claims ableiten, Entitaeten und Beziehungen pruefen, News validieren, Graphen und Reports erzeugen, Agenten kontrolliert einsetzen und die Qualitaet ueber Golden Sets, Benchmarks und Human Review messen.

## 2. Architekturentscheidung v2

Die zentrale Entscheidung lautet:

```text
ForesightGraph baut zuerst einen belastbaren Evidence- und Methodology-Core.
Workbench, News Layer, Agent Control und Graph-Funktionen werden darauf gestuft aufgebaut.
GraphRAG, Vector DB, Agenten-Runtimes und Premium-Daten kommen erst nach messbarem Bedarf.
```

### Entscheidungspunkte

1. **Evidence-first bleibt nicht verhandelbar.** Kein produktiver Claim, keine produktive Edge und kein Report ohne nachvollziehbare Quelle und Review-Status.
2. **Provider-Neutralitaet bleibt Core-Prinzip.** Modelle, Agenten, Datenbanken, Retrieval-Systeme und UI-Technologien muessen austauschbar bleiben.
3. **Verified News wird eigener Layer.** Nachrichten werden nicht ungeprueft aggregiert, sondern in Source Tiers, Claims, Evidence und Review-Prozesse ueberfuehrt.
4. **Windows Workbench wird Produktziel.** Die erste nutzbare Oberflaeche soll lokal, verstaendlich und fuer Einzelanwender praktikabel sein.
5. **Hermes und Codex bleiben kontrollierte Arbeitswerkzeuge.** Sie duerfen vorbereiten, analysieren, strukturieren und PRs erzeugen, aber produktive Projektdateien, Claims, Edges und Reports nicht ohne Human Review finalisieren.
6. **Investment-Bezug bleibt Research-Unterstuetzung.** Keine Buy/Sell/Hold-Ausgaben, keine Kursziele als Empfehlung, keine Broker-Integration und keine automatisierte Anlageentscheidung.

## 3. Zielbild

ForesightGraph soll ein spezialisiertes Intelligence OS fuer komplexe Technologie- und Firmenoekosysteme werden. Der erste konkrete Track ist das NVIDIA-Oekosystem.

Das System soll:

- Quellen, News, Filings, Reports und technische Dokumente strukturiert erfassen.
- Aus Quellen atomare Claims extrahieren.
- Firmen, Produkte, Technologien, Personen, Regionen, Lieferketten und Risiken als Entitaeten modellieren.
- Beziehungen als evidenzgebundene Edges verwalten.
- Widersprueche, Unsicherheiten und veraltete Aussagen sichtbar machen.
- Research-Signale und Oekosystemmuster nachvollziehbar darstellen.
- Graphen, Timelines, Matrizen und Reports erzeugen.
- Agentenaufgaben kontrollieren, protokollieren und reviewpflichtig machen.
- Qualitaet ueber Golden Sets, Benchmarks und Methodology Review verbessern.

## 4. Systemprinzipien

| Prinzip | Roadmap-Regel |
|---|---|
| Local-first | Projektwissen, Claims und Graph-Daten bleiben zuerst lokal kontrollierbar. |
| Evidence-first | Keine wichtige Aussage ohne Quelle, Datum, Locator und Review-Status. |
| Source-first | Quellen werden vor Interpretation und Signalbildung dokumentiert. |
| Provider-neutral | Kein Anbieter wird Core-Identitaet oder harte Abhaengigkeit. |
| Human Review | Menschen oder explizite Review-Regeln finalisieren produktive Claims, Edges und Reports. |
| Schema-lite zuerst | Datenmodelle werden frueh standardisiert, aber nicht zu schwer gebaut. |
| Benchmark-first | Neue Technologie wird nur ueber messbaren Nutzen eingefuehrt. |
| Open-source-safe | Keine geschuetzten Volltexte, API-Keys, privaten Daten oder persoenlichen Investmententscheidungen im Repository. |
| Agent-controlled | Agenten arbeiten nur mit klaren Rechten, Audit Log und Approval Gates. |
| MVP-diszipliniert | Komplexe Infrastruktur kommt erst nach konkretem Problem und Akzeptanzkriterium. |

## 5. Zielarchitektur als Layer-Modell

| Layer | Zweck | MVP-Umfang | Spaeterer Ausbau | Akzeptanzkriterium |
|---|---|---|---|---|
| 1. User Interface Layer | Lokale Workbench fuer Review, Navigation, Reports und Graphen. | Streamlit oder lokale Web-App fuer erste Workbench. | React/FastAPI, Tauri oder Desktop Shell. | Einzelanwender kann Quellen, Claims, Review Queue und Reports lokal bedienen. |
| 2. Agent Interface Layer | Schnittstelle fuer ChatGPT, Codex, Hermes und lokale LLMs. | Prompt-/Task-Schnittstelle, keine autonome Produktivaktion. | Adapter fuer weitere Agenten und Tools. | Jede Agentenaktion ist einem Task und Audit Log zugeordnet. |
| 3. Agent Control Layer | Rechte, Approval, Sandboxing, Rollback, Stop-Regeln. | Allowed/Forbidden Actions, Review Gate, no direct write. | Rollen, Profiles, Checkpoints, Rollback-Policy. | Kein Agent darf produktive Daten ohne Freigabe finalisieren. |
| 4. Source Layer | Quellen erfassen, klassifizieren, referenzieren. | Source Registry mit URL, Datum, Typ, Locator. | Hashes, Rechtepruefung, API-Adapter. | Jede verwendete Quelle ist wiederauffindbar. |
| 5. Ingestion Layer | Dokumente und News in strukturierte Rohobjekte ueberfuehren. | Manuelle oder assistierte Erfassung. | API-Feeds, Filings, Watchlists. | Ingestion erzeugt keine ungeprueften produktiven Claims. |
| 6. Evidence Layer | Belegstellen, Auszuege, Locator und Quellengewicht verwalten. | Evidence-Objekt mit Source-Verweis und Locator. | Evidence Strength, Konfliktlogik, Zeitgueltigkeit. | Jeder produktive Claim besitzt Evidence. |
| 7. Claim Layer | Atomare Aussagen aus Evidence erzeugen. | Claim Store mit Status und Confidence. | Claim-Deduplikation, Superseded-Logik. | Jeder Claim ist atomar, pruefbar und statusbehaftet. |
| 8. Entity Layer | Firmen, Technologien, Produkte, Orte und Personen normalisieren. | Entity Registry mit Aliasen. | Entity Resolution, externe IDs. | Wiederkehrende Entitaeten werden konsistent benannt. |
| 9. Relationship / Edge Layer | Beziehungen zwischen Entitaeten modellieren. | Edge mit Evidence und Review-Status. | Edge-Typen, Zeitachsen, Gewichtung. | Keine Edge ohne Evidence und Review-Status. |
| 10. Verified News Layer | Nachrichten in gepruefte Oekosystemsignale ueberfuehren. | Source Tiers, NewsItem, News-to-Claim-Prozess. | APIs, Alerts, News Impact Timeline. | News erzeugt nur nach Review produktive Claims. |
| 11. Signal Layer | Research-Signale, Risiken und Muster ableiten. | Signal als Interpretation mit Trace zu Claims. | Signal Scoring, Szenarien, Dashboards. | Jedes Signal ist rueckverfolgbar bis zur Quelle. |
| 12. Knowledge/Evidence Graph | Claims, Entities, Edges und Evidence visualisieren und abfragen. | Kleiner Graph aus geprueften Edges. | Graph DB, GraphRAG nach Benchmark. | Graph beantwortet erste Multi-Hop-Fragen nachvollziehbar. |
| 13. Evaluation Layer | Qualitaet messen und Regressionen erkennen. | Golden Set, Benchmark-Runner, Review-Metriken. | RAGAS/DeepEval/OpenTelemetry-Integration. | Neue Architekturentscheidungen basieren auf Messdaten. |
| 14. Visualization Layer | Graphen, Timelines, Matrizen und Dashboards erzeugen. | Relationship Graph, Source Quality Matrix, Risk Matrix. | Sankey, Heatmaps, Benchmark Dashboards. | Visualisierungen zeigen Datenbasis und Unsicherheit. |
| 15. Report Layer | Lesbare Research-Berichte erzeugen. | Markdown/PDF-Reports mit Quellenbindung. | Report Builder, Exportprofile. | Jeder Bericht ist bis zu Source/Evidence rueckverfolgbar. |
| 16. Tool & Provider Adapter Layer | Modelle, Datenquellen, DBs und Tools austauschbar anbinden. | Kleine Adapter-Contracts. | Plugin-System, Premium Data Adapter. | Kein Provider wird ohne Adaptergrenze hart verdrahtet. |
| 17. Security & Governance Layer | Secrets, Rechte, Audit, Policies, Review schuetzen. | No-Secrets-Regel, SECURITY, DATA_POLICY. | Secret Scanning, Policies, Rollenmodell. | Keine API-Keys oder privaten Daten im Repo. |
| 18. Open Source Boundary Layer | Definiert, was oeffentlich sein darf. | Lizenz, Disclaimer, Datenregeln. | Contributor-Prozess, Datenlizenzpruefung. | Repo enthaelt keine problematischen Volltexte oder privaten Entscheidungen. |

## 6. Minimales Datenmodell

Das Datenmodell bleibt am Anfang bewusst klein, aber erweiterbar. Alle Objekte erhalten mindestens `id`, `created_at`, `updated_at`, `status` und `review_status`, sofern sinnvoll.

| Objekt | Pflichtfelder | Zweck | Beziehungen |
|---|---|---|---|
| Source | id, title, source_type, url_or_file, source_date, accessed_at, tier, license_note | Quelle registrieren. | Evidence, NewsItem |
| Evidence | id, source_id, locator, excerpt_or_summary, evidence_type, confidence | Belegstelle dokumentieren. | Source, Claim, Edge |
| NewsItem | id, source_id, title, published_at, tier, topic, quarantine_status | Nachricht erfassen. | Source, Claim, Signal |
| Claim | id, text, claim_type, evidence_ids, status, confidence, last_checked | Atomare Aussage verwalten. | Evidence, Entity, Edge, Signal |
| Entity | id, name, entity_type, aliases, identifiers, status | Firmen, Produkte, Technologien normalisieren. | Claim, Edge, Report |
| Edge | id, source_entity_id, target_entity_id, relationship_type, evidence_ids, status | Beziehung modellieren. | Entity, Evidence, Graph |
| Signal | id, title, signal_type, claim_ids, horizon, uncertainty, interpretation | Research-Signal ableiten. | Claim, Report, Visualization |
| Review | id, object_type, object_id, reviewer, decision, reviewed_at, notes | Menschliche Pruefung dokumentieren. | Alle reviewpflichtigen Objekte |
| BenchmarkRun | id, benchmark_id, dataset_version, system_version, metrics, result, date | Evaluation reproduzieren. | Claim, Report, ArchitectureDecision |
| AgentTask | id, agent_name, task_type, allowed_actions, output_refs, approval_status | Agentenarbeit kontrollieren. | AuditLogEntry, Review |
| Report | id, title, report_type, source_ids, claim_ids, generated_at, status | Research-Bericht erzeugen. | Source, Claim, Signal |
| ResearchTrack | id, name, scope, status, lead_entities, acceptance_criteria | NVIDIA und spaetere Tracks organisieren. | Entity, Report, BenchmarkRun |
| ProviderCandidate | id, provider_name, provider_type, use_case, gate_status, evidence | Provider pruefen. | BenchmarkRun, ArchitectureDecision |
| ToolAdapter | id, tool_name, adapter_type, permissions, status | Tool-Anbindung kapseln. | AgentTask, ProviderCandidate |
| VisualizationConfig | id, view_type, input_objects, filters, risk_notes | Diagramme reproduzierbar machen. | Entity, Edge, Signal |
| AuditLogEntry | id, actor, action, object_ref, timestamp, result | Nachvollziehbarkeit sichern. | AgentTask, Review |

### Statuswerte

```text
draft
needs_review
confirmed
disputed
rejected
superseded
outdated
rumor
quarantined
not_reproduced
manufacturer_claim
project_decision
```

### Beispiel: Claim

```yaml
id: claim_nvidia_supply_001
text: "Company A supplies component B for product family C."
claim_type: fact
status: needs_review
confidence: medium
evidence_ids:
  - evidence_001
related_entities:
  - entity_company_a
  - entity_product_c
last_checked: 2026-06-11
review_status: needs_review
```

## 7. Verified News & Ecosystem Intelligence Layer

Der Verified News Layer verhindert, dass ForesightGraph ein ungepruefter News-Aggregator wird. Nachrichten sind Rohmaterial, keine automatisch gesicherten Fakten.

### Source Tiers

| Tier | Quellenart | Nutzung | Claim-Gewicht | Review-Regel | Open-Source-Regel |
|---|---|---|---|---|---|
| Tier 1 | Primaerquellen: Filings, Geschaeftsberichte, IR, offizielle technische Dokumente | Bevorzugte Faktenbasis. | Hoch | Review erforderlich, aber geringere Quarantaene. | Metadaten, Links, kurze Auszuege, eigene Claims. |
| Tier 2 | Nachrichtenagenturen und hochwertige Finanzmedien | Ereignis- und Kontextvalidierung. | Mittel bis hoch | Mindestens Source/Tier-Pruefung; bei kritischen Claims Zweitquelle. | Keine Volltexte; nur Metadaten, Link, kurze zulaessige Exzerpte, eigene Zusammenfassung. |
| Tier 3 | Branchen- und Techmedien | Fruehe Signale und technische Einordnung. | Mittel | Gegenpruefung bei produktiven Claims. | Keine Volltexte; klare Kennzeichnung als Sekundaerquelle. |
| Tier 4 | Blogs, Podcasts, YouTube, Social Media | Ideen, Hinweise, Expertenmeinungen. | Niedrig | Nicht als Fakt ohne Primaer- oder Tier-2-Bestaetigung. | Nur Link, Metadaten und eigene Notiz. |
| Tier 5 | Geruechte und unbestaetigte Hinweise | Watchlist, Hypothesen, Quarantaene. | Sehr niedrig | Immer `rumor` oder `quarantined`. | Nicht als bestaetigte Erkenntnis veroeffentlichen. |

### News-to-Claim-Prozess

```text
NewsItem -> Source Tier -> Relevanzpruefung -> Evidence -> Claim Draft -> Review -> Confirmed/Rejected/Disputed -> Signal/Report
```

MVP-Regel: Eine Nachricht darf im MVP keine produktive Edge und kein produktives Signal erzeugen, wenn sie nicht mindestens eine Evidence-Stelle, Source Tier, Locator und Review-Status besitzt.

## 8. NVIDIA Ecosystem MVP

Der NVIDIA Track ist der erste fachliche Reference Track. Er dient dazu, das System an einem realen, komplexen AI-Infrastruktur-Oekosystem zu testen.

### Scope des ersten Tracks

| Bereich | MVP-Ziel |
|---|---|
| NVIDIA | zentrale Entity, Produktfamilien, offizielle Quellen, Risiken. |
| Hyperscaler & Cloud | Kunden-/Partner-/Infrastrukturbeziehungen erfassen. |
| Foundries, HBM, Packaging, Networking | Lieferketten- und Abhaengigkeitsbeziehungen modellieren. |
| Server, Racks, Rechenzentren, Energie, Kuehlung | Infrastruktur- und Engpasssignale erfassen. |
| Enterprise AI, Robotics, Healthcare, Automotive, Industrial AI, AI-RAN, Edge AI | Anwendungsoekosysteme als Track-Unterbereiche vorbereiten. |
| Wettbewerber und Risiken | Konkurrenz, Export Controls, Geopolitik, Kundenkonzentration. |

### MVP-Output

- `ResearchTrack: NVIDIA Ecosystem`
- erste kuratierte Firmen- und Technologie-Liste
- Source Registry fuer Primaerquellen und hochwertige Nachrichten
- 20 gepruefte Sources
- 20 gepruefte Claims
- 30 gepruefte Edges
- 10 Widerspruchs- oder Unsicherheitsfaelle
- erste Relationship-Graph-Ansicht
- erster Report mit Rueckverfolgbarkeit bis Source/Evidence

## 9. Scientific Methodology Framework

ForesightGraph wird nicht nur gebaut, sondern als ueberpruefbares Forschungsinstrument gefuehrt.

### Hypothesen fuer v2

| ID | Hypothese | Messgroesse | MVP-Test |
|---|---|---|---|
| H1 | Evidence-first reduziert unbelegte Aussagen. | Anteil produktiver Claims mit Source/Evidence/Locator. | Stichprobe aus 20 Claims. |
| H2 | Source Tiering verbessert Signalqualitaet. | Anteil korrigierter oder verworfener News-Claims je Tier. | Vergleich Tier 1-5 in News Review. |
| H3 | Verified News Layer verbessert Aktualitaet ohne Qualitaetsverlust. | Data Freshness, News Verification Accuracy, Claim Error Rate. | 30 NewsItems im NVIDIA Track. |
| H4 | Human Review reduziert kritische Fehler bei Claims und Edges. | abgelehnte/korrigierte Vorschlaege, Edge Error Rate. | Review Log. |
| H5 | Graph-Visualisierung verbessert Multi-Hop-Verstaendnis. | UI Task Completion, Multi-Hop Correctness. | 10 Relationship-Fragen. |
| H6 | Hybrid Search bringt erst ab messbarer Schwelle Mehrwert. | Context Precision/Recall, Latenz, Kosten. | Baseline vs. Hybrid Vergleich. |
| H7 | GraphRAG lohnt sich nur bei corpus-globalen oder multi-hop Fragen. | Antwortqualitaet je Query-Typ. | GraphRAG-Pilot erst nach Golden Set. |
| H8 | Agenten erhoehen Geschwindigkeit nur akzeptabel mit Audit Log und Approval. | Agent Task Accuracy, Review Overturn Rate. | kontrollierte AgentTasks. |

### Golden Set v2

MVP-Golden-Set:

```text
20 Sources
20 Claims
30 Entities
30 Edges
20 NewsItems
10 Multi-Hop-Fragen
10 Widerspruchsfaelle
5 Reports
5 AgentTasks
```

### Metriken

```text
Citation Accuracy
Faithfulness
Locator Quality
Claim Accuracy
Source Quality
News Verification Accuracy
Multi-Hop Correctness
Entity Disambiguation
Edge Error Rate
Contradiction Detection
Signal Traceability
Human Review Accuracy
Reproducibility
Data Freshness
Agent Task Accuracy
UI Task Completion
```

## 10. Technologiepfad

Die Roadmap empfiehlt Variante B als Zielarchitektur, aber mit Variante A als schnellem Lern-MVP.

### Variantenentscheidung

| Variante | Beschreibung | Bewertung | Entscheidung |
|---|---|---|---|
| A. Schneller MVP | Streamlit/Gradio, Python, SQLite, Markdown/JSON, einfache Graph-Ansicht. | Schnell, einfach, gut fuer Proof of Workflow. | Als erster Prototyp geeignet. |
| B. Professionelle Workbench | React oder Next.js, FastAPI, SQLite zuerst, spaeter PostgreSQL, React Flow/Cytoscape.js, Audit Log. | Besser fuer langfristige Workbench und Agent Control. | Empfohlene Zielrichtung. |
| C. Agent Platform | Plugin-System, Event Bus, Agent Sandbox, Graph DB, Vector DB, Observability. | Stark, aber zu schwer fuer fruehen MVP. | Spaeter, nach Methodik- und Workbench-Reife. |

### Empfohlener Technologiepfad

| Bereich | MVP | Ziel nach MVP | Gate |
|---|---|---|---|
| UI | Streamlit oder lokale Web-App | React/FastAPI oder Next.js/FastAPI; optional Tauri | UI Task Completion und Wartbarkeit. |
| Backend | Python Services / FastAPI | FastAPI mit klaren Adapter-Contracts | API-Stabilitaet. |
| Datenhaltung | Markdown/JSON + SQLite | SQLite/DuckDB; spaeter PostgreSQL | Datenmenge, Multi-User, Query-Bedarf. |
| Retrieval | Volltextsuche | Hybrid Search | Besserer Recall/Precision bei akzeptabler Komplexitaet. |
| Vector DB | nicht im MVP | Qdrant, LanceDB, Weaviate oder FAISS nach Test | messbarer Mehrwert. |
| Graph | NetworkX/JSON oder einfache DB | Neo4j/ArangoDB/RDF nur bei Bedarf | Multi-Hop- und Graph-Benchmark. |
| Visualisierung | einfache Graph-Komponente | Cytoscape.js, React Flow, D3 nach Bedarf | Graph-Interaktion und UI-Komplexitaet. |
| Agenten | Codex/Hermes als Arbeitswerkzeuge | LangGraph/AutoGen/CrewAI nur nach Use Case | Agent Task Accuracy und Security Gate. |
| Evaluation | eigenes Benchmarking | RAGAS, DeepEval, OpenTelemetry | reproduzierbare Metriken. |

## 11. UI / UX Workbench Concept

Die Workbench soll nicht wie ein Entwickler-Tool wirken, sondern wie eine Research-Zentrale fuer einen Einzelanwender auf Windows.

### MVP-Seiten

| Seite | Zweck | MVP-Funktion |
|---|---|---|
| Home Dashboard | Gesamtstatus zeigen. | offene Reviews, neue Sources, neue News, Risiken. |
| NVIDIA Ecosystem Map | erste Track-Uebersicht. | Firmen, Beziehungen, Risikokategorien. |
| Company View | Entity-zentrierte Recherche. | Quellen, Claims, Edges, Signale je Firma. |
| News Intelligence | News pruefen. | Source Tier, News-to-Claim, Quarantaene. |
| Source Registry | Quellen verwalten. | Quelle, Datum, Tier, Locator, Lizenznotiz. |
| Evidence Viewer | Belege pruefen. | Excerpt/Summary, Locator, zugehoerige Claims. |
| Claim Review Queue | produktive Claims freigeben oder ablehnen. | Needs Review, Confirmed, Rejected, Disputed. |
| Relationship Graph | Beziehungen sichtbar machen. | kleine Graph-Ansicht mit Evidence-Link. |
| Signal Dashboard | Research-Signale und Risiken betrachten. | Signaltyp, Zeithorizont, Unsicherheit. |
| Benchmark Dashboard | Qualitaet messen. | Golden Set Ergebnisse, Regressionen. |
| Agent Control Panel | Agentenaufgaben kontrollieren. | Task, Rechte, Status, Output, Approval. |
| Report Builder | Berichte erzeugen. | Markdown/PDF-Report mit Quellenbindung. |
| Data Quality Dashboard | Projektgesundheit zeigen. | fehlende Sources, offene Reviews, veraltete Claims. |
| Settings / Config | lokale Konfiguration. | Provider, Pfade, Review-Regeln, API-Key-Hinweise ohne Speicherung im Repo. |
| Audit Log | Nachvollziehbarkeit. | wer/was/wann, AgentTask, Ergebnis. |

## 12. Visualisierungskonzept

| Visualisierung | Datenbasis | Nutzen | MVP? | Hauptrisiko |
|---|---|---|---|---|
| Relationship Graph | Entity + Edge + Evidence | Partnerschaften und Lieferketten verstehen. | Ja | Scheinpraezision bei schwachen Edges. |
| Evidence Graph | Source + Evidence + Claim | Rueckverfolgbarkeit. | Ja | Ueberladung. |
| News Impact Timeline | NewsItem + Claim + Signal | Ereignisse zeitlich einordnen. | Ja | News-Rauschen. |
| Source Quality Matrix | Source Tier + Review Ergebnis | Quellenqualitaet sichtbar machen. | Ja | Tier wird mit Wahrheit verwechselt. |
| Risk Matrix | Signal + Risiko + Impact | Risiken strukturieren. | Ja | subjektive Gewichtung. |
| Company Comparison Matrix | Entities + Claims + Metrics | Firmen vergleichbar machen. | Spaeter | falsche Gleichsetzung unterschiedlicher Quellen. |
| Sankey Diagram | Lieferketten-Edges | Abhaengigkeiten darstellen. | Spaeter | unvollstaendige Daten wirken vollstaendig. |
| Benchmark Dashboard | BenchmarkRun + Metrics | Architekturentscheidungen messen. | Ja | Metriken als absolute Wahrheit missverstehen. |
| Technology Adoption Map | Entities + Products + Signals | Adoption und Oekosystemverschiebungen erkennen. | Spaeter | Bias durch selektive Quellen. |

## 13. Agent Control Layer

Agenten sind Beschleuniger, nicht Autoritaeten. Jede produktive Uebernahme bleibt reviewpflichtig.

### Rollen

| Agent | Rolle | Erlaubt | Nicht erlaubt im MVP |
|---|---|---|---|
| ChatGPT | Research, Review, Prompt-Erstellung. | Analyse, Roadmap, Review, Prompts. | direkte Repo-Aenderungen ohne Codex/Hermes-Workflow. |
| Codex | Code- und Doku-Aenderungen ueber Branch/PR. | Tests, kleine PRs, Dokumentation, Validatoren. | Merge, Releases, Tags, ungefragte Provider-Integration. |
| Hermes | Bounded Batch, lokale Pruefungen, Monitoring, Research-Ops. | Berichte, Checks, strukturierte Outputs. | produktive Claims/Edges ohne Review finalisieren. |
| Lokale LLMs | Assistenz bei Extraktion und Zusammenfassung. | Drafts und Vorschlaege. | gesicherte Fakten ohne Evidence erzeugen. |
| Cloud-LLMs | optionaler Provider. | nach Provider-Gate. | harte Core-Abhaengigkeit. |

### Agenten-Gates

1. Task muss Ziel, Scope und erlaubte Aktionen enthalten.
2. Agent darf keine Secrets ausgeben oder speichern.
3. Agent darf keine produktiven Dateien ohne Branch/PR oder Freigabe veraendern.
4. Agent-Output bekommt AuditLogEntry.
5. Kritische Outputs gehen in Review Queue.
6. Merge und produktive Uebernahme bleiben menschlich kontrolliert.

## 14. Tool- und Provider-Strategie

Provider sind Kandidaten, keine Architekturidentitaet.

### Provider-Gates

| Gate | Mindestanforderung |
|---|---|
| Fit Gate | konkreter Use Case im Projekt. |
| Evidence Gate | Herstellerclaim mit Quelle und Locator. |
| Security Gate | File-, Netzwerk-, Shell-, Secret- und Datenpolicy. |
| Evaluation Gate | Benchmark gegen Baseline. |
| License Gate | Lizenz und Datenrechte dokumentiert. |
| Cost/Latency Gate | Kosten und Latenz akzeptabel. |
| Maintainability Gate | kleine Adapterflaeche. |
| Lock-in Gate | Daten, Prompts und Benchmarks bleiben portabel. |
| Adoption Gate | wiederholbarer Mehrwert, nicht nur Demo-Eindruck. |

### Provider-Statuswerte

```text
candidate
manufacturer_claim
not_reproduced
needs_benchmark
rejected_for_mvp
accepted_for_pilot
accepted_with_constraints
project_decision
```

## 15. Open Source Governance & Data Boundaries

### Offen im Repository

- Quellcode, Schemata, Validatoren, Templates, Tests.
- Roadmaps, ADRs, Policies, leere oder synthetische Beispieldaten.
- Eigene strukturierte Claims, wenn Quellen nur referenziert und rechtlich sauber genutzt werden.
- Eigene Zusammenfassungen, sofern keine geschuetzten Volltexte reproduziert werden.

### Nicht ins Repository

- API-Keys, Tokens, Secrets, lokale Zugangsdaten.
- Volltexte von Reuters, Bloomberg, FT, WSJ, CNN oder anderen geschuetzten Quellen ohne klare Rechtebasis.
- Paywall-Inhalte als Kopie.
- private Investmententscheidungen, persoenliche Portfolio-Daten, vertrauliche Dokumente.
- persoenliche Daten ohne Zweck, Rechtsgrundlage und Policy.

### Lizenzempfehlung

Empfehlung: **Apache-2.0** fuer Code und technische Dokumentation, sofern keine Gegenanforderung besteht.

Begruendung: Apache-2.0 ist permissiv, verbreitet, open-source-tauglich und enthaelt eine explizite Patentlizenz. MIT ist einfacher, aber ohne explizite Patentklausel. AGPL-3.0 ist sinnvoll, wenn Netzwerk-Copyleft gewuenscht ist, erhoeht aber die Einstiegshuerde fuer Beitraege und Nutzung.

Erforderliche Dateien:

```text
LICENSE
README.md
CONTRIBUTING.md
SECURITY.md
DATA_POLICY.md
DISCLAIMER.md
CODE_OF_CONDUCT.md
```

## 16. Security & Governance

MVP-Regeln:

- Keine Secrets im Repository.
- Keine produktiven Agentenaktionen ohne Audit Log.
- Kein direkter Push auf `main`.
- Branch/PR/Review fuer Aenderungen.
- Keine Releases, Tags oder Deployments ohne explizite Freigabe.
- Keine Provider-/Runtime-Integration ohne ADR und Gates.
- Keine geschuetzten Volltexte in Open Source.
- Keine automatische Anlageentscheidung.

Governance-Artefakte:

```text
docs/ARCHITECTURE_DECISION_RECORDS.md
docs/DATA_POLICY.md
docs/EVIDENCE_RULES.md
docs/NEWS_SOURCE_TIERS.md
docs/AGENT_CONTROL_POLICY.md
docs/PROVIDER_GATES.md
docs/REVIEW_PROTOCOL.md
```

## 17. Roadmap-Phasen

| Phase | Ziel | Kernlieferung | Nicht Teil der Phase |
|---|---|---|---|
| 0. Roadmap v2 Foundation | Zielbild und Scope konsolidieren. | Roadmap v2, Begriffe, Open-Source-Grenzen. | Implementierung. |
| 1. Methodology Foundation | Datenmodell, Source Tiers, Statuswerte und Review-Protokoll definieren. | Evidence Rules, News Tiers, Review Protocol, Provider Gates. | UI, GraphRAG, Vector DB. |
| 2. Minimal Evidence System | Sources, Evidence, Claims, Entities und Reviews abbilden. | Source Registry, Claim Store, Review Queue. | automatische News-Pipeline. |
| 3. Verified News Layer | News-to-Claim-Prozess einfuehren. | NewsItem, Source Quality, Rumor Quarantine. | Volltextspeicherung geschuetzter Medien. |
| 4. NVIDIA Ecosystem MVP | ersten Track mit geprueften Daten fuellen. | Firmenliste, Edges, erste Reports, Graph View. | Provider-Runtime-Integration. |
| 5. Visual Research Workbench | lokale Windows-nutzbare Oberflaeche bauen. | Dashboard, Source/Claim/Graph/Report Views. | komplexe Desktop-App, Voice. |
| 6. ForesightGraph Research Agent | kontrollierte Agent-Aufgaben. | Agent Control Panel, Audit Log, Approval Gates. | autonome produktive Aktionen. |
| 7. Benchmarking & Evaluation | Qualitaet messbar machen. | Golden Sets, Citation Accuracy, Multi-Hop-Fragen. | grosse Benchmark-Automatisierung ohne Datenbasis. |
| 8. Controlled Hermes/Codex Integration | Arbeitsworkflow stabilisieren. | Branch/PR/Tests/Review, bounded batches. | Auto-Merge, Releases. |
| 9. Advanced Graph & Retrieval | Hybrid Search und Graph-Nutzen pruefen. | Hybrid Benchmark, GraphRAG Pilot nur bei Gate. | GraphRAG als Default. |
| 10. Premium Data & Scalable Intelligence | Datenanbieter und Skalierung pruefen. | Lizenzpruefung, API Adapter, Kosten-Nutzen. | ungeregelte Paywall-Daten. |
| 11. Optional Voice / Natural Agent Interface | Sprachschnittstelle pruefen. | Voice-to-task nur fuer unkritische Aktionen. | kritische Aktionen ohne Bestaetigung. |

## 18. Akzeptanzkriterien

1. Jede wichtige Aussage hat Quelle, Datum, Locator und Review-Status.
2. Jede News ist einem Source Tier zugeordnet.
3. Jeder produktive Claim ist mit Evidence verbunden.
4. Jede produktive Edge im Graph braucht Evidence und Review.
5. Geruechte werden getrennt von bestaetigten Fakten gespeichert.
6. Kein Agent darf produktive Dateien oder Daten ohne Freigabe finalisieren.
7. Kein YOLO- oder Auto-Merge-Modus fuer produktive Research-Daten.
8. Kein Systemteil erzeugt automatische Buy/Sell/Hold-Empfehlungen.
9. Keine Kursziele als direkte Empfehlung.
10. Keine Broker-Integration.
11. Jede neue Technologie braucht eine dokumentierte Begruendung.
12. Jede groessere Architekturentscheidung braucht Benchmark oder klaren Use Case.
13. Die UI ist fuer einen Einzelanwender auf Windows praktisch nutzbar.
14. Spaetere Tools werden ueber Adapter angebunden.
15. Agentenaktionen sind im Audit Log nachvollziehbar.
16. Reports sind bis zur Quelle rueckverfolgbar.
17. Das Open-Source-Repository enthaelt keine urheberrechtlich problematischen Volltexte, API-Keys oder privaten Investmententscheidungen.

## 19. Risiken und Gegenmassnahmen

| Risiko | Wahrscheinlichkeit | Auswirkung | Gegenmassnahme | MVP-Regel |
|---|---|---|---|---|
| Overengineering | hoch | langsamer Fortschritt | Phasen, Gates, einfache Baseline. | kein GraphRAG/Vector DB ohne Benchmark. |
| Vendor-Lock-in | mittel | Austauschbarkeit sinkt | Adapter, Provider-Gates. | keine harte Provider-Abhaengigkeit. |
| schlechte Quellenqualitaet | hoch | falsche Claims | Source Tiers, Review, Quarantaene. | Tier 4/5 nie als Fakt. |
| Halluzinationen | hoch | falsche Reports | Evidence-first, Human Review. | keine Claims ohne Evidence. |
| falsche Entity-Zuordnung | mittel | falsche Graphen | Entity Registry, Aliase, Review. | kritische Entities pruefen. |
| falsche Edges | hoch | irrefuehrende Beziehungen | Edge Review, Evidence Pflicht. | keine Edge ohne Evidence. |
| veraltete Daten | mittel | falsche Einschatzung | last_checked, outdated Status. | alte Claims markieren. |
| Nachrichtenrauschen | hoch | Scheinsignale | Source Tiering, News Review. | Rumor Quarantine. |
| Confirmation Bias | mittel | einseitige Interpretation | Gegenquellen, Widerspruchsfaelle. | disputed sichtbar machen. |
| Investment Bias | mittel | Scheinberatung | Disclaimer, keine Empfehlungen. | keine Buy/Sell/Hold-Outputs. |
| Datenlizenzrisiken | hoch | rechtliche Risiken | DATA_POLICY, keine Volltexte. | nur Metadaten/Links/kurze Auszuege. |
| API-Kosten | mittel | Betrieb wird teuer | Kostenmetriken, Provider-Gates. | keine Premium-Daten ohne Kostenplan. |
| Agenten-Sicherheitsrisiken | hoch | Daten-/Repo-Schaden | Allowed/Forbidden Actions, Audit. | keine produktive Aktion ohne Approval. |
| zu komplexe UI | mittel | schlechte Nutzbarkeit | MVP-Seiten priorisieren. | erst Review/Source/Claim/Graph. |
| unkontrollierter Terminalzugriff | mittel | Sicherheitsrisiko | Sandbox, explizite Rechte. | kein broad shell allow. |
| Open-Source-Missbrauch | niedrig-mittel | Reputationsrisiko | License, Security, Disclaimer. | klare Grenzen dokumentieren. |

## 20. Konkrete naechste Roadmap-Schritte

1. Roadmap v2 als Projektquelle aufnehmen.
2. Altbezeichnungen `WIKI Omid` in neuen Projektquellen vermeiden oder klar als historische Quelle markieren.
3. `docs/EVIDENCE_RULES.md`, `docs/NEWS_SOURCE_TIERS.md`, `docs/REVIEW_PROTOCOL.md` und `docs/PROVIDER_GATES.md` vorbereiten.
4. Minimales Datenmodell fuer Source, Evidence, Claim, Entity, Edge, NewsItem, Review und AuditLogEntry definieren.
5. Golden Set v2 mit NVIDIA Track starten: 20 Sources, 20 Claims, 30 Entities, 30 Edges, 20 NewsItems.
6. Workbench-MVP fachlich spezifizieren, aber noch nicht implementieren.
7. Erst nach Methodology Foundation ueber UI-Prototyp entscheiden.
8. GraphRAG, Vector DB, Runtime-Provider und Premium-Daten ausdruecklich spaeter pruefen.

## 21. Quellenbasis

Diese Roadmap wurde aus der bisherigen ForesightGraph-Projektquelle, der finalen Architektur-Roadmap, dem Roadmap-v2-Deep-Research-Brief und aktuellen technischen Primär-/Referenzquellen verdichtet.

Projektquellen:

- ForesightGraph Project Source v0.3, bereitgestellt im Projektkontext.
- ForesightGraph Intelligence OS - Final Architecture Roadmap, 2026-06-01.
- Deep Research Prompt: ForesightGraph Intelligence OS Roadmap v2, 2026-06-11.
- Codex/Hermes Workflow- und Bounded-Batch-Kontext, bereitgestellt im Projektkontext.

Technische Referenzen:

- OpenAI Codex Documentation: https://developers.openai.com/codex/cloud
- OpenAI Codex AGENTS.md Guide: https://developers.openai.com/codex/guides/agents-md
- GitHub Protected Branches: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub Secret Scanning / Push Protection: https://docs.github.com/en/code-security/secret-scanning
- Microsoft GraphRAG: https://microsoft.github.io/graphrag/
- GraphRAG Paper: https://arxiv.org/abs/2404.16130
- PostgreSQL Full Text Search: https://www.postgresql.org/docs/current/textsearch-intro.html
- SQLite FTS5: https://sqlite.org/fts5.html
- FastAPI: https://fastapi.tiangolo.com/
- Streamlit: https://docs.streamlit.io/
- Tauri: https://tauri.app/
- Cytoscape.js: https://js.cytoscape.org/
- React Flow: https://reactflow.dev/
- RAGAS: https://docs.ragas.io/
- DeepEval: https://github.com/confident-ai/deepeval
- OpenTelemetry: https://opentelemetry.io/docs/
- Open Source Initiative - Apache-2.0: https://opensource.org/license/Apache-2.0
- Open Source Initiative - MIT: https://opensource.org/license/mit
- Open Source Initiative - AGPL-3.0: https://opensource.org/license/agpl-3.0
