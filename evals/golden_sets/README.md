# Golden Sets

This directory contains golden sets and dataset snapshots used for evaluating ForesightGraph's reasoning capabilities.

## Purpose

Golden sets define the standard benchmarks and evaluation datasets used in ForesightGraph's evaluation protocol. They ensure reproducible and consistent evaluation by providing stable, reviewed datasets that can be traced back to specific data states.

## Dataset Snapshots

Dataset snapshots capture the complete state of evaluation data at specific points in time. They ensure reproducible benchmark results by including questions, contexts, answers, and review status information.

### Snapshot Structure

Each snapshot follows the schema defined in `dataset_snapshot_schema.md` and contains:
- A unique identifier and version
- A collection of questions following the multi-hop question schema
- Metadata about creation and review status
- Tags and source context information

### Relationship to Multi-Hop Questions

Dataset snapshots are built from the multi-hop questions defined in the parent `evals/multi_hop_questions/` directory. Each snapshot references questions from this collection but provides a complete, reviewed, and versioned dataset for benchmarking.

## Usage Guidelines

### For Evaluation

- Only use snapshots marked as "approved" for official benchmark results
- All benchmark results must include human review documentation
- No real benchmark result should be claimed without proper review and approval
- Snapshots must be referenced in any evaluation reports to ensure reproducibility

### For Development

- Use sample snapshots for testing and development
- Create new snapshots following the established schema
- Maintain version control of snapshot sets
- Ensure all snapshots undergo human review before approval

## Snapshot Naming Convention

Snapshots should be named following this pattern:
- `snapshot_vX.Y.Z.json` - for versioned snapshots
- `sample_snapshot_vX.Y.Z.json` - for sample snapshots
- `benchmark_snapshot_vX.Y.Z.json` - for official benchmark snapshots

Where X.Y.Z represents the semantic version number.

## Important Notes

1. **Human Review Required**: All snapshots must undergo human review before being marked as "approved"
2. **Reproducibility**: Snapshots must be sufficient to reproduce the exact same benchmark results
3. **No Real Facts**: Snapshots should not contain real market, company, legal, or investment facts to avoid potential issues
4. **Future Work**: GraphRAG, Vector DB, and full RAGAS automation are future work and should not be implemented now

## Current Snapshots

- `sample_dataset_snapshot_v0.1.json` - Sample snapshot for demonstration purposes