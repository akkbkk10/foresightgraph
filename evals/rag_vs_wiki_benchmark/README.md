# RAG vs Wiki Benchmark

## Purpose

This directory contains the methodology scaffolding for comparing different information retrieval and knowledge base approaches in ForesightGraph evaluations. The benchmark framework will evaluate and compare:

- Classic RAG (Retrieval-Augmented Generation)
- LLM-Wiki / Markdown knowledge base
- Hybrid Wiki search
- Graph-augmented approach

## Expected Inputs

- Benchmark questions in standard format
- Knowledge base content for each approach
- Evaluation criteria and scoring guidelines

## Expected Outputs

- Comparative analysis of all baseline approaches
- Performance metrics for each methodology
- Benchmark result files for each approach

## Metrics Reference

Benchmark results will be evaluated using standard information retrieval metrics including:
- Precision and Recall
- F1-Score
- Relevance scoring
- Response quality metrics

## Human Review Requirement

All benchmark results must undergo human review before being considered valid for publication or performance claims. No automated result should be claimed without proper human verification.

## Out-of-Scope Items

This directory currently contains only methodology scaffolding and does not include:
- Executable benchmark automation
- RAGAS integration
- Vector DB implementation
- GraphRAG implementation
- Ingestion pipelines
- Scoring algorithms
- Alerts or notifications
- Trading logic (Buy/Sell/Hold)
- Price targets
- Browser automation
- MCP server integrations
- External API connections
- Dependencies beyond basic Python libraries