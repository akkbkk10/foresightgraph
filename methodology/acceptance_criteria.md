# Methodology Acceptance Criteria v0.1

This document defines minimal acceptance criteria for methodology evaluations. These criteria serve as initial research gates for the methodology layer, not absolute proof of performance.

## Evidence-first Hallucination Reduction

**Related Hypothesis:** Implementing evidence-first prompting reduces hallucinations by 30% compared to standard prompting approaches.

**Metric Reference:** F1 score for factual accuracy in generated responses (measured against gold standard evidence).

**Required Test Data:** Golden set of questions with verified evidence chains (minimum 50 examples).

**MVP Acceptance Rule:** Model must achieve ≥ 0.70 F1 score on factual accuracy metric.

**Human Review Note:** Manual verification of top-50% of responses required for each evaluation run.

## Multi-hop Question Answering

**Related Hypothesis:** Multi-hop question answering capability improves by 25% with structured evidence chains.

**Metric Reference:** Success rate for multi-hop questions (questions requiring 2-3 evidence sources).

**Required Test Data:** Golden set of multi-hop questions (minimum 30 examples).

**MVP Acceptance Rule:** Model must answer ≥ 60% of multi-hop questions correctly.

**Human Review Note:** Manual validation of evidence chains and reasoning steps required.

## Citation/Source Accuracy

**Related Hypothesis:** Source accuracy improves by 40% with explicit citation mechanisms.

**Metric Reference:** Precision of cited sources (percentage of cited sources matching actual evidence).

**Required Test Data:** Golden set of questions with source verification (minimum 40 examples).

**MVP Acceptance Rule:** Model must achieve ≥ 0.80 precision for cited sources.

**Human Review Note:** Full manual verification of all citations required for each evaluation run.

## RAG vs Wiki Baseline Comparison

**Related Hypothesis:** RAG implementation provides 15% improvement over wiki baseline for factual accuracy.

**Metric Reference:** F1 score for factual accuracy (comparing RAG vs wiki baseline).

**Required Test Data:** Shared test set of 100 questions with gold standard answers.

**MVP Acceptance Rule:** RAG must achieve ≥ 0.05 higher F1 score than wiki baseline.

**Human Review Note:** Statistical significance testing required for baseline comparison.

## Notes

These acceptance criteria are initial v0.1 research gates and should be refined based on experimental results. They represent minimum thresholds for methodology validation, not final performance requirements.