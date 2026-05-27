# Architecture

ForesightGraph is designed as an evidence-first local intelligence and research system built around a knowledge graph.

## Goals

- Ingest local evidence sources and register them in a source catalog.
- Extract structured evidence and claims from source content.
- Normalize entities and edges into an evidence graph.
- Support human review, note-taking, and evidence-backed reporting.
- Enable evaluation of methodology and evidence quality.

## Core components

1. Source Registry
   - Track local evidence sources (files, journals, notes, snippets).
   - Store source metadata such as title, type, path, author, and timestamp.
2. Extraction Engine
   - Parse registered sources to surface evidence items and claims.
   - Convert raw text into structured fragments with provenance.
3. Evidence Graph
   - Model evidence, claims, entities, and edges as graph nodes + relationships.
   - Connect evidence to claims and source records.
4. Human Review Layer
   - Record reviewer annotations, verification status, and flags.
   - Capture review decisions tied to evidence and claims.
5. Knowledge Graph Interface
   - Query and traverse evidence relationships.
   - Support export or reporting of evidence-backed conclusions.

## Data model

- Source: registry entry for an information asset.
- Evidence: extracted fact or observation tied to a Source.
- Claim: interpretive statement derived from Evidence.
- Entity: normalized concept or subject referenced by Evidence/Claims.
- Edge: typed relationship linking Entities, Claims, or Evidence.
- Review: human assessment attached to Evidence and Claims.

## Storage and implementation

- Start with local file-based storage (JSON/YAML) for prototypes.
- Keep the core model in Python dataclasses or simple domain classes.
- Use a lightweight graph representation in memory for MVP, with optional persistence.
- Separate ingestion, extraction, graph-building, and review flows.

## Interfaces

- Command-line or Python API for registering sources and building the graph.
- Simple functions for querying evidence by source, claim, entity, and review status.
- Export-friendly methods for report generation and methodology summaries.
- Future extension points: UI, notebook workflows, and evaluation dashboards.
