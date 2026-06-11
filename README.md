# ForesightGraph

**Evidence-first research system for structured knowledge discovery.**

## Status

Public early-stage MVP scaffold. Methodology-first development.

## Active Project Source

The canonical active project source is [ForesightGraph Intelligence OS Roadmap v2](ForesightGraph_Intelligence_OS_Roadmap_v2.md).

Use this priority order for project instructions:

1. `ForesightGraph_Intelligence_OS_Roadmap_v2.md`
2. `ForesightGraph_Codex_Prompt_Standard.md` and `docs/HERMES_WORKFLOW_POLICY.md`
3. Individual task prompts
4. Historical roadmap or planning documents

The previous MVP roadmap in `docs/roadmap.md` is retained as historical reference.

## Core Concept

ForesightGraph is an evidence-first research system that prioritizes sourced information and structured evidence collection over speculation.

## Methodology Foundation

Phase 1 methodology documentation lives in `docs/`: [Evidence Rules](docs/EVIDENCE_RULES.md), [News Source Tiers](docs/NEWS_SOURCE_TIERS.md), [Review Protocol](docs/REVIEW_PROTOCOL.md), [Provider Gates](docs/PROVIDER_GATES.md), and [Data Policy](docs/DATA_POLICY.md).

The active agent and schema-lite references are [Agent Control Policy](docs/AGENT_CONTROL_POLICY.md) and [Schema-Lite Data Model](docs/SCHEMA_LITE.md).

Planning references for the next Phase 1 package are [Golden Set v2 Plan](docs/GOLDEN_SET_V2_PLAN.md), [AgentTask Governance](docs/AGENT_TASK_GOVERNANCE.md), and [ProviderCandidate Governance](docs/PROVIDER_CANDIDATE_GOVERNANCE.md).

Golden Set review and benchmark planning are covered by [Golden Set Acceptance Criteria](docs/GOLDEN_SET_ACCEPTANCE_CRITERIA.md) and [Benchmark Question Design](docs/BENCHMARK_QUESTION_DESIGN.md).

Manual review and future Golden Set release gates are documented in [Manual Review Workflow](docs/MANUAL_REVIEW_WORKFLOW.md) and [Golden Set Release Checklist](docs/GOLDEN_SET_RELEASE_CHECKLIST.md).

Data quality and future dashboard readiness are documented in [Data Quality Metrics](docs/DATA_QUALITY_METRICS.md) and [Review Dashboard Readiness](docs/REVIEW_DASHBOARD_READINESS.md).

Architecture and provider decision guidance is documented in [Architecture Decision Records](docs/ARCHITECTURE_DECISION_RECORDS.md) and [Provider Evaluation Notes](docs/PROVIDER_EVALUATION_NOTES.md).

## Local Setup

1. Ensure Python 3.8+ is installed
2. Navigate to the project directory
3. Install dependencies (when ready):
   ```bash
   pip install -e .
   ```

## Testing

Run the current test suite:

```bash
python -m pytest -q
```

## Safety & Workflow Rules

All changes are reviewed with the following checks:

1. **Review changes**: `git diff`
2. **Run tests**: `python -m pytest -q`
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
- **ForesightGraphRepository**: facade that initializes and exposes all stores as attributes: `sources`, `evidence`, `claims`, `entities`, `edges`, `reviews`, `signals`.
- **SignalStore**: store and manage `RelationshipSignalRecord` items with indexing capabilities (signal_id, source_company, target_company, relationship_type, signal_category, orientation, evidence_ids, confidence, signal_strength, status, observed_at, last_verified_at, review_due_at).

## SignalStore Documentation

### What SignalStore is
The SignalStore is an in-memory store for managing relationship signal records. It provides CRUD operations and indexing capabilities for relationship signals, enabling efficient querying by source company, target company, signal category, and status.

### Why signal_id exists
The `signal_id` field is required and stable because:
- It serves as the primary key for each relationship signal record
- It ensures unique identification of signals across the system
- It maintains data integrity and enables reliable referencing
- It's used as the key in internal data structures for efficient lookups

### Basic SignalStore operations
- **add**: Add a new relationship signal record to the store
- **get**: Retrieve a specific signal by its signal_id
- **list_all**: Retrieve all signals in the store
- **list_by_source**: List signals by source company
- **list_by_target**: List signals by target company
- **list_by_category**: List signals by signal category
- **list_by_status**: List signals by status
- **update**: Update an existing signal record
- **delete**: Remove a signal record from the store

### SignalStore integration with ForesightGraphRepository
- **repo.signals**: Access the SignalStore instance through the repository facade
- **repo.add_signal()**: Add a signal record via the repository facade, delegating to SignalStore.add()

### Testing Requirements
After any changes to the documentation, pytest must pass to ensure all functionality remains intact.

## Current Test Status

- Run `python -m pytest -q` for the current test suite.

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

### SignalStore Usage Example

```python
from foresightgraph.repository import ForesightGraphRepository
from foresightgraph.signal_store import RelationshipSignalRecord
from datetime import datetime

repo = ForesightGraphRepository()
now = datetime.now()

# Add a signal using the repository facade
signal = RelationshipSignalRecord(
    signal_id="sig1",
    source_company="Company A",
    target_company="Company B",
    relationship_type="partnership",
    signal_category="commercial_deal_signal",
    orientation="partnership_likely",
    evidence_ids=["e1"],
    confidence="high",
    signal_strength=7,
    status="confirmed_partnership",
    observed_at=now,
    last_verified_at=None,
    review_due_at=now
)

repo.add_signal(signal)
print(repo.signals.get("sig1"))
```

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

## JSON Persistence Example

Example showing direct imports from foresightgraph for JSON persistence:

```python
from foresightgraph import ForesightGraphRepository, save_repository, load_repository

# Create repository
repo = ForesightGraphRepository()

# Save to JSON file
save_repository(repo, "my_repository.json")

# Load from JSON file
loaded_repo = load_repository("my_repository.json")
```

## Package Imports

The following imports are available at the package level:

```python
from foresightgraph import SignalStore, RelationshipSignalRecord
```

```python
from foresightgraph import ForesightGraphRepository, save_repository, load_repository

# Create repository
repo = ForesightGraphRepository()

# Save to JSON file
save_repository(repo, "my_repository.json")

# Load from JSON file
loaded_repo = load_repository("my_repository.json")
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
