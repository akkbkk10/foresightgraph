# Multi-Hop Question Golden Set Schema

## Purpose

This schema defines the structure for multi-hop benchmark questions used in ForesightGraph's evaluation protocol. The schema ensures consistent question formatting, clear answer paths, and proper evidence chaining for reproducible evaluation of multi-hop reasoning capabilities.

## Required Fields

### `question_id`
- **Type**: string
- **Description**: Unique identifier for the question
- **Format**: `mhq_XXX` where XXX is a sequential number
- **Example**: `"mhq_001"`

### `question`
- **Type**: string
- **Description**: The multi-hop question that requires traversing multiple knowledge sources
- **Requirements**: 
  - Must require at least two logical connections between entities
  - Must be answerable using the knowledge graph structure
  - Must be clear and unambiguous
- **Example**: `"What is the relationship between the discovery of penicillin and the development of antibiotics?"`

### `answer_path`
- **Type**: array of objects
- **Description**: The logical chain of entities that must be traversed to answer the question
- **Structure**: Each object contains `entity` and `description`
- **Example**: 
```json
[
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
]
```

### `ground_truth_evidence`
- **Type**: array of strings
- **Description**: Ground truth evidence statements that support each step in the answer path
- **Requirements**:
  - Each evidence statement must be verifiable and factual
  - Must support the logical connections in the answer path
  - Must be traceable to primary sources
- **Example**:
```json
[
  "Alexander Fleming discovered penicillin in 1928",
  "Penicillin was the first antibiotic used in medicine",
  "The discovery led to the development of many other antibiotics"
]
```

### `expected_answer`
- **Type**: string
- **Description**: The complete, well-formed answer that integrates all evidence and entities
- **Requirements**:
  - Must fully answer the question
  - Must integrate all entities from the answer path
  - Must be logically consistent with the evidence chain
- **Example**: `"Alexander Fleming's discovery of penicillin in 1928 led to the development of antibiotics, as penicillin was the first antibiotic used in medicine and paved the way for many other antibiotics."`

## Optional Fields

### `review_status`
- **Type**: string
- **Description**: Current review status of the question
- **Values**: `"draft"`, `"reviewed"`, `"approved"`, `"deprecated"`
- **Default**: `"draft"`

### `source_context`
- **Type**: string
- **Description**: Information about the source or context from which the question was derived
- **Example**: `"Historical science textbook chapter 5"`

### `difficulty_level`
- **Type**: string
- **Description**: Difficulty rating for the question
- **Values**: `"beginner"`, `"intermediate"`, `"advanced"`
- **Default**: `"intermediate"`

### `tags`
- **Type**: array of strings
- **Description**: Classification tags for the question
- **Example**: `["history", "science", "medicine"]`

## Review Status Values

- **`draft`**: Question is being created or modified
- **`reviewed`**: Question has been reviewed by at least one expert
- **`approved`**: Question has been approved for use in benchmark evaluation
- **`deprecated`**: Question is outdated and should not be used

## Evidence Chain Structure

The evidence chain must follow a logical progression that supports the answer path:

1. **Entity Connection**: Each entity in the answer path must be connected to the next through logical relationships
2. **Evidence Support**: Each connection must be supported by at least one ground truth evidence statement
3. **Temporal/Logical Flow**: The chain should follow a clear temporal or logical sequence
4. **Verifiability**: All evidence statements must be verifiable and traceable to reliable sources

## Scoring Notes

### Multi-hop Correctness
- Measures whether the complete answer path is correctly identified and traversed
- Must include all entities from the answer path in the correct order
- Logical connections between entities must be maintained

### Citation Accuracy
- Evaluates precision of cited sources and evidence
- All cited evidence must be verifiable and traceable
- No fabricated or non-existent citations

### Faithfulness
- Assesses adherence to factual content of retrieved context documents
- Answer must not introduce false information
- All claims must be supported by evidence

### Answer Completeness
- Measures coverage of all relevant information required to answer the question fully
- Must address all aspects of the question's scope

## Acceptance Notes

1. **Human Review Required**: All questions must undergo human review before being marked as "approved"
2. **Source Quality**: Evidence must be sourced from primary documents or peer-reviewed publications
3. **Logical Consistency**: Answer paths must maintain logical consistency throughout
4. **Reproducibility**: Questions must be structured to allow for reproducible evaluation
5. **No Real Facts**: Questions should not contain real market, company, legal, or investment facts to avoid potential issues

## Example Record

```json
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
  "review_status": "approved",
  "difficulty_level": "intermediate",
  "tags": ["history", "science", "medicine"]
}