# RAG vs Wiki Benchmark

## Purpose

This directory contains the benchmark framework for comparing RAG-style and Wiki-style approaches in ForesightGraph evaluations. The benchmark setup establishes the methodology for evaluating different baseline approaches before implementing full GraphRAG or Vector DB solutions.

## Expected Future Benchmark Files

- `rag_results.jsonl` - Results from RAG-style baseline evaluations
- `wiki_results.jsonl` - Results from Wiki-style baseline evaluations  
- `hybrid_results.jsonl` - Results from Hybrid Wiki/Search baseline evaluations
- `graph_results.jsonl` - Results from Evidence/Graph-assisted baseline evaluations (planned)
- `benchmark_comparison.csv` - Comparative analysis of all baseline approaches

## Important Notes

### Human Review Requirement
No benchmark result should be claimed without reviewed data. All evaluation results must undergo human verification before being considered valid for publication or performance claims.

### Current Limitations
- No GraphRAG implementation has been developed yet
- No Vector DB implementation has been implemented yet
- Current evaluation focuses only on baseline methodology and comparison framework
- All questions must be human-reviewed and marked as "approved" before use

### Future Implementation Plan
Following the baseline comparison methodology defined in `methodology/baseline_comparison.md`, this directory will be expanded to include:
1. Implementation of RAG-style evaluation pipeline
2. Implementation of Wiki-style evaluation pipeline  
3. Implementation of Hybrid approach evaluation pipeline
4. Implementation of Graph-assisted evaluation pipeline
5. Full RAGAS automation integration

## Usage Guidelines

### For Development
- Use sample questions from `evals/multi_hop_questions/` for testing
- Follow the golden set schema for question formatting
- Ensure all questions are marked as "approved" before benchmark use

### For Evaluation
- Only use questions marked as "approved" for official benchmark results
- All benchmark results must include human review documentation
- Do not claim benchmark performance without proper review