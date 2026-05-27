# Multi-Hop Experiment Protocol

## Purpose
This protocol defines the first reproducible evaluation method for testing multi-hop reasoning capabilities in ForesightGraph, establishing baseline comparisons and evaluation metrics.

## Hypothesis Covered
ForesightGraph's multi-hop reasoning capabilities will demonstrate improved performance over traditional RAG-style approaches when answering complex questions requiring information traversal across multiple knowledge sources.

## Required Dataset Snapshot
- A curated dataset of multi-hop questions with known answer paths
- Ground truth evidence chains showing the logical connections between entities
- Context documents that support the multi-hop reasoning process

## Required Question Format
Questions must be structured to require at least two logical connections between entities, with clear expected answer paths that can be traced through the knowledge graph.

## Compared Baselines

### A. Raw/RAG-style answer
Standard retrieval-augmented generation approach without graph assistance

### B. Wiki-style answer  
Answer based on persistent Markdown/wiki knowledge layer (Karpathy's approach)

### C. Evidence/graph-assisted answer (later)
Answer incorporating graph-based evidence traversal and reasoning

## Metrics

### Primary Metrics
- **Multi-hop correctness**: Percentage of questions where the complete answer path is correctly identified and traversed
- **Citation accuracy**: Precision of cited sources and evidence in supporting the answer
- **Faithfulness**: Adherence to the factual content of retrieved context documents
- **Answer completeness**: Coverage of all relevant information required to answer the question fully

### Secondary Metrics
- **Human review decision**: Expert evaluation of overall reasoning quality and logical flow

## Step-by-Step Protocol

1. **Preparation**: Load dataset snapshot and establish baseline models
2. **Execution**: Run each baseline approach on all questions in the dataset
3. **Evaluation**: Apply all defined metrics to each answer set
4. **Analysis**: Compare results across baselines and identify performance patterns
5. **Documentation**: Record findings and prepare for next iteration

## Acceptance Check
- All required dataset questions are processed by each baseline
- All metrics are computed and documented
- Human review component is completed for sample questions
- Protocol can be reproduced with documented steps

## Limitations
- Current evaluation focuses on specific question types and may not generalize
- Baseline C (graph-assisted) is not yet implemented
- Limited by the quality and coverage of the initial dataset
- Human review is subjective and may introduce bias

## Next Improvement
- Implement graph-assisted baseline (C)
- Expand dataset with more diverse question types
- Add automated evaluation components for scalability
- Incorporate additional RAGAS metrics for more comprehensive assessment