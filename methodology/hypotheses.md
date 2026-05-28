# Methodology Scaffold: Initial Hypotheses

This document contains the initial v0.1 methodology hypotheses for ForesightGraph. These are minimal scaffold hypotheses to guide early experimentation and evaluation.

## Hypothesis 1: Evidence-first Hallucination Reduction
- **ID**: HYP-001
- **Short Hypothesis**: Implementing evidence-first prompting strategies will reduce hallucinations in generated responses by 30% compared to baseline approaches.
- **Metric**: Hallucination rate measured as percentage of factually incorrect claims in generated responses
- **MVP Test Idea**: Deploy evidence-first prompting on a subset of eval questions and compare response quality against baseline prompting using human evaluation
- **Acceptance Note**: If evidence-first prompting shows statistically significant improvement in hallucination reduction, proceed to full evaluation

## Hypothesis 2: Multi-hop Question Answering
- **ID**: HYP-002
- **Short Hypothesis**: Multi-hop question answering capabilities will improve response accuracy by 25% when dealing with complex queries requiring information synthesis.
- **Metric**: Accuracy of multi-hop answers measured as percentage of correctly synthesized information
- **MVP Test Idea**: Test with 20 multi-hop questions from golden sets and measure accuracy against baseline approaches
- **Acceptance Note**: If multi-hop capability shows measurable improvement in accuracy, proceed to broader evaluation

## Hypothesis 3: Citation/Source Accuracy
- **ID**: HYP-003
- **Short Hypothesis**: Implementing citation tracking will increase source accuracy in responses by 40% compared to non-citation approaches.
- **Metric**: Percentage of claims with correct source attribution in generated responses
- **MVP Test Idea**: Evaluate citation accuracy on 100 sample responses using human verification of source attribution
- **Acceptance Note**: If citation tracking shows significant improvement in source accuracy, proceed to integration testing

## Hypothesis 4: RAG vs Wiki Baseline Comparison
- **ID**: HYP-004
- **Short Hypothesis**: Retrieval-Augmented Generation (RAG) approach will outperform wiki baseline approach by 35% in answer quality for factual questions.
- **Metric**: Answer quality measured using human evaluation scoring (1-5 scale)
- **MVP Test Idea**: Run controlled comparison between RAG and wiki baseline on shared question set with human evaluation scoring
- **Acceptance Note**: If RAG shows statistically significant improvement over wiki baseline, proceed to full implementation