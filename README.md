# ForesightGraph

**Evidence-first research system for structured knowledge discovery.**

## Status

Private local MVP scaffold. Early-stage development.

## Core Concept

ForesightGraph is an evidence-first research system that prioritizes sourced information and structured evidence collection over speculation.

## Local Setup

1. Ensure Python 3.8+ is installed
2. Navigate to the project directory
3. Install dependencies (when ready):
   ```bash
   pip install -e .
   ```

## Testing

Run the test suite:

```bash
python -m pytest tests
```

## Safety & Workflow Rules

All changes are reviewed with the following checks:

1. **Review changes**: `git diff`
2. **Run tests**: `python -m pytest tests`
3. **Check status**: `git status`

This ensures code quality and prevents unintended changes.

## MVP Modules

This MVP implements a set of small, in-memory stores that form the core data layer:

- **SourceRegistry**: store and retrieve `SourceRecord` entries (source_id, title, type, path, created_at).
- **EvidenceStore**: manage `EvidenceRecord` items linked to sources (evidence_id, source_id, locator, text_excerpt, created_at).
- **ClaimStore**: manage `ClaimRecord` items linked to evidence (claim_id, evidence_id, text, confidence, review_status, created_at).
- **EntityStore**: manage `EntityRecord` entries (entity_id, name, entity_type, aliases, created_at) with alias/name lookup.
- **EdgeStore**: store `EdgeRecord` relationships between nodes (edge_id, from_id, to_id, edge_type, evidence_id, created_at).
- **ReviewStore**: simple review records for targets (review_id, target_id, target_type, status, reviewer, comment, created_at).
- **ForesightGraphRepository**: facade that initializes and exposes all stores as attributes: `sources`, `evidence`, `claims`, `entities`, `edges`, `reviews`.

## Current Test Status

- Test suite: 69 passing tests (local run when this README was updated).

## Quick Example

Minimal example creating the repository and adding a source:

```python
from datetime import datetime
from foresightgraph.repository import ForesightGraphRepository
from foresightgraph.source_registry import SourceRecord

repo = ForesightGraphRepository()
now = datetime.now()
src = SourceRecord("src1", "Example Title", "article", "/path/to/src", now)
repo.sources.add(src)

print(repo.sources.get("src1"))
```

## Workflow Notes

Typical local workflow:

```bash
# run tests
python -m pytest -q

# inspect changes
git diff --staged --stat

# when ready, stage and commit
git add <files>
git commit -m "Add description of changes"
git push
```

Follow the project's review steps before pushing changes to the remote.