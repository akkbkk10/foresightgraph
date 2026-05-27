# Dataset Snapshot Schema

## Purpose

This schema defines the structure for dataset snapshots used in ForesightGraph's evaluation protocol. Dataset snapshots ensure reproducible benchmark results by capturing the exact state of evaluation data at a specific point in time, including questions, contexts, answers, and review status. This enables traceability from benchmark results back to specific data states.

## Required Fields

### `snapshot_id`
- **Type**: string
- **Description**: Unique identifier for the dataset snapshot
- **Format**: `ds_XXX` where XXX is a sequential number
- **Example**: `"ds_001"`

### `snapshot_name`
- **Type**: string
- **Description**: Human-readable name for the snapshot
- **Example**: `"Multi-hop Benchmark v0.1"`

### `version`
- **Type**: string
- **Description**: Semantic version of the snapshot
- **Format**: `X.Y.Z` where X is major, Y is minor, Z is patch
- **Example**: `"0.1.0"`

### `questions`
- **Type**: array of objects
- **Description**: Array of question objects that form the benchmark
- **Structure**: Each object follows the multi-hop question schema
- **Example**: 
```json
[
  {
    "question_id": "mhq_001",
    "question": "What is the relationship between the discovery of penicillin and the development of antibiotics?",
    "answer_path": [
      {
        "entity": "Alexander Fleming",
        "description": "Scottish bacteriologist who discovered penicillin"
      }
    ],
    "ground_truth_evidence": [
      "Alexander Fleming discovered penicillin in 1928"
    ],
    "expected_answer": "Alexander Fleming's discovery of penicillin in 1928 led to the development of antibiotics...",
    "review_status": "approved"
  }
]
```

### `created_at`
- **Type**: string (ISO 8601 format)
- **Description**: Timestamp when the snapshot was created
- **Example**: `"2024-01-15T10:30:00Z"`

### `created_by`
- **Type**: string
- **Description**: Identifier of who created the snapshot
- **Example**: `"human_reviewer_001"`

## Optional Fields

### `description`
- **Type**: string
- **Description**: Detailed description of what the snapshot contains
- **Example**: `"Initial benchmark set for multi-hop reasoning evaluation"`

### `review_status`
- **Type**: string
- **Description**: Current review status of the snapshot
- **Values**: `"draft"`, `"reviewed"`, `"approved"`, `"deprecated"`
- **Default**: `"draft"`

### `tags`
- **Type**: array of strings
- **Description**: Classification tags for the snapshot
- **Example**: `["benchmark", "multi-hop", "v0.1"]`

### `source_context`
- **Type**: string
- **Description**: Information about the source or context from which the snapshot was derived
- **Example**: `"Derived from multi-hop question golden set v0.1"`

### `dependencies`
- **Type**: array of strings
- **Description**: List of other snapshots or datasets this snapshot depends on
- **Example**: `["ds_001", "ds_002"]`

## Review Status Values

- **`draft`**: Snapshot is being created or modified
- **`reviewed`**: Snapshot has been reviewed by at least one expert
- **`approved`**: Snapshot has been approved for use in benchmark evaluation
- **`deprecated`**: Snapshot is outdated and should not be used

## Snapshot Naming Convention

Snapshots should be named following this pattern:
- `snapshot_vX.Y.Z.json` - for versioned snapshots
- `sample_snapshot_vX.Y.Z.json` - for sample snapshots
- `benchmark_snapshot_vX.Y.Z.json` - for official benchmark snapshots

Where X.Y.Z represents the semantic version number.

## Reproducibility Notes

1. **Complete State Capture**: All snapshots must capture the complete state of the evaluation data including questions, contexts, and ground truth answers
2. **Version Control**: Each snapshot must have a unique version identifier to track changes
3. **Timestamps**: All snapshots must include creation timestamps for audit trail
4. **Source Attribution**: Snapshots must clearly indicate their source and derivation
5. **Reproducible Results**: Snapshots must be sufficient to reproduce the exact same benchmark results

## Human Review Notes

1. **Review Required**: All snapshots must undergo human review before being marked as "approved"
2. **Source Quality**: All questions and evidence in snapshots must be sourced from primary documents or peer-reviewed publications
3. **Logical Consistency**: Answer paths must maintain logical consistency throughout
4. **Reproducibility**: Snapshots must be structured to allow for reproducible evaluation
5. **No Real Facts**: Snapshots should not contain real market, company, legal, or investment facts to avoid potential issues

## Example Snapshot

```json
{
  "snapshot_id": "ds_001",
  "snapshot_name": "Multi-hop Benchmark v0.1",
  "version": "0.1.0",
  "questions": [
    {
      "question_id": "mhq_001",
      "question": "What is the relationship between the discovery of penicillin and the development of antibiotics?",
      "answer_path": [
        {
          "entity": "Alexander Fleming",
          "description": "Scottish bacteriologist who discovered penicillin"
        },
        {
          "entity": "Penicillin",
          "description": "First antibiotic discovered by Alexander Fleming"
        },
        {
          "entity": "Antibiotics",
          "description": "Class of drugs that inhibit bacterial growth"
        }
      ],
      "ground_truth_evidence": [
        "Alexander Fleming discovered penicillin in 1928",
        "Penicillin was the first antibiotic used in medicine",
        "The discovery led to the development of many other antibiotics"
      ],
      "expected_answer": "Alexander Fleming's discovery of penicillin in 1928 led to the development of antibiotics, as penicillin was the first antibiotic used in medicine and paved the way for many other antibiotics.",
      "review_status": "approved"
    }
  ],
  "created_at": "2024-01-15T10:30:00Z",
  "created_by": "human_reviewer_001",
  "description": "Initial benchmark set for multi-hop reasoning evaluation",
  "review_status": "approved",
  "tags": ["benchmark", "multi-hop", "v0.1"]
}