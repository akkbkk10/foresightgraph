# Baseline Comparison Methodology

## Purpose

This document defines the methodology for comparing different baseline approaches in ForesightGraph evaluations. The comparison focuses on RAG-style, Wiki-style, Hybrid Wiki/Search, and Evidence/Graph-assisted approaches to establish a foundation for future benchmarking and evaluation.

## Compared Baselines

### A. Raw/RAG-style
A retrieval-augmented generation approach that retrieves relevant context from a knowledge base and generates answers using that context.

### B. Wiki-style
A traditional wiki-based approach that relies on structured knowledge organization and linking, similar to Wikipedia's approach to information organization.

### C. Hybrid Wiki/Search
A combined approach that leverages both structured wiki-style knowledge organization and search-based retrieval to provide comprehensive answers.

### D. Evidence/Graph-assisted (later)
A graph-based approach that utilizes knowledge graph structures and evidence chains to provide answers with provenance and reasoning capabilities.

## What Each Baseline is Allowed to Use

### Raw/RAG-style
- Retrieval from knowledge base using vector similarity search
- Context window for answer generation
- Pre-trained language models for answer synthesis
- Document-level evidence for context

### Wiki-style
- Structured knowledge organization and linking
- Entity and relationship definitions
- Hierarchical knowledge organization
- Cross-referencing capabilities

### Hybrid Wiki/Search
- All capabilities of Wiki-style and Raw/RAG-style approaches
- Combined retrieval and organization methods
- Multi-modal knowledge access

### Evidence/Graph-assisted (later)
- Knowledge graph structures and relationships
- Evidence chains and provenance tracking
- Multi-hop reasoning capabilities
- Graph traversal algorithms

## What Each Baseline Must Not Use

### Raw/RAG-style
- No access to external knowledge sources beyond the local knowledge base
- No pre-trained models for reasoning (only generation from retrieved context)
- No graph structures or evidence chains

### Wiki-style
- No external search capabilities
- No vector similarity search
- No generative models for answer synthesis

### Hybrid Wiki/Search
- No external knowledge sources beyond the local knowledge base
- No pre-trained reasoning models
- No graph structures or evidence chains

### Evidence/Graph-assisted (later)
- No external knowledge sources beyond the local knowledge base
- No pre-trained models for generation (only graph-based reasoning)
- No vector similarity search or traditional retrieval methods

## Required Inputs

- Multi-hop questions from the golden set schema
- Knowledge base content organized in ForesightGraph format
- Human-reviewed question sets (approved status required)
- Evidence chains and provenance data for graph approaches

## Required Outputs

- Answer to the multi-hop question
- Evidence support for the answer
- Confidence scores for generated answers
- Retrieval results (for RAG-style approaches)
- Graph traversal paths (for graph approaches)

## Metrics to Compare

### RAGAS/EACL 2024 Metrics
- **Faithfulness**: Measures adherence to factual content of retrieved context documents
- **Answer Relevancy**: Measures relevance of generated answer to the question
- **Context Precision**: Measures precision of retrieved context documents
- **Context Recall**: Measures recall of retrieved context documents

### NIST AI RMF 1.0 Metrics
- **Governance**: Measures adherence to evaluation protocols and review processes
- **Mapping**: Measures consistency of answer paths with knowledge graph structures
- **Measurement**: Measures reproducibility and consistency of evaluation results
- **Risk Management**: Measures reliability and trustworthiness of generated answers

## Human Review Requirement

All benchmark results must undergo human review and approval before being considered valid. No real benchmark result should be claimed without proper human review and documentation. Questions must be marked as "approved" before being used in official evaluations.

## Limitations

- Current implementation focuses on baseline comparison methodology only
- Graph-based approaches are not yet implemented
- No external knowledge sources are available for any approach
- Evaluation is limited to the current knowledge base content
- No automated RAGAS evaluation pipeline is implemented yet

## Next Improvement

1. Implement the evaluation framework for baseline comparison
2. Develop the GraphRAG approach following Microsoft's GraphRAG patterns
3. Integrate full RAGAS automation pipeline
4. Add Vector DB implementation for improved retrieval
5. Expand benchmark question sets with more diverse multi-hop scenarios