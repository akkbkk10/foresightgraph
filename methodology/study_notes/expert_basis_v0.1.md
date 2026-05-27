# Expert Basis for Multi-Hop Evaluation

## Purpose
This document provides expert guidance and source notes for evaluating multi-hop reasoning capabilities in ForesightGraph, serving as a foundation for the first reproducible protocol.

## Expert Notes

- **Karpathy LLM Wiki**: Persistent Markdown/wiki knowledge can act as a lightweight human-readable knowledge layer that supports multi-hop reasoning by providing interconnected information sources that can be traversed sequentially.

- **Microsoft GraphRAG**: Graph-based retrieval and query-focused summarization are useful for private corpora, but should be benchmarked later as part of the evaluation framework rather than implemented as part of the current baseline.

- **RAGAS/EACL 2024**: Faithfulness, Answer Relevancy, Context Precision, and Context Recall are useful RAG evaluation metrics that provide comprehensive assessment of retrieval-augmented generation quality for multi-hop questions.

- **NIST AI RMF 1.0**: AI evaluation should include governance, mapping, measurement, and management of risks, ensuring that multi-hop evaluation considers potential biases and limitations in the reasoning process.

- **Project roadmap v0.6**: ForesightGraph should be a testable research instrument with hypotheses, baselines, metrics, reproducibility, and human review, aligning with the need for structured evaluation protocols.

## Impact on ForesightGraph

Each expert note provides guidance for developing robust evaluation protocols that ensure ForesightGraph's multi-hop reasoning capabilities are properly tested and validated against established benchmarks and best practices in the field.