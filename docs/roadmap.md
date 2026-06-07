# Roadmap

This roadmap defines a practical MVP for ForesightGraph, focused on local evidence capture and graph-based reasoning.

## Phase 1: MVP

1. Define domain model
   - Implement `Source`, `Evidence`, `Claim`, `Entity`, `Edge`, and `Review` types.
   - Use Python dataclasses or simple classes for the core data model.
2. Build source registry
   - Add API to register and list local sources.
   - Persist registry metadata to local JSON/YAML for MVP.
3. Add extraction scaffolding
   - Implement basic extraction flow that maps source content to evidence and claims.
   - Preserve provenance links from extracted items to source records.
4. Construct evidence graph
   - Build graph relationships between evidence, claims, entities, and edges.
   - Provide a simple in-memory graph view and save/load support.
5. Human review support
   - Add review metadata to evidence/claims.
   - Enable review status and notes to be stored alongside graph data.

## Phase 2: Validation and reporting

1. Query and traversal APIs
   - Implement functions to retrieve evidence by source, claim, and entity.
   - Support edge-based graph traversal for evidence chains.
2. Report generation
   - Add export of evidence-backed summaries and methodology notes.
   - Provide a text-based report or notebook-friendly output.
3. Evaluation workflows
   - Define a minimal evaluation checklist for evidence quality and methodology.
   - Capture evaluation results tied to sources and claims.

## Phase 3: Stabilization

1. Tests
   - Add unit tests for model objects, registry, extraction, and graph builders.
   - Validate persistence and load/save behavior.
2. Documentation
   - Expand docs with implementation notes and examples.
   - Add usage examples for a local research workflow.
3. Infrastructure
      - Add CI hooks once the basic Python package and tests are stable.\n\n## Current stabilization baseline\n- pytest CI workflow exists\n- real NVIDIA micro golden set structural validation exists\n- nvidia_ai_004 conservative consistency guard exists\n- Hermes workflow policy and batched-run checklist exist\n\nNext direction: small evidence-first dataset and methodology expansion under existing review gates.
