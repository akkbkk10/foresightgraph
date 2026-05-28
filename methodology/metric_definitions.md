# Metric Definitions

## Evidence Coverage
**Purpose:** Measure the extent to which retrieved evidence supports claims in generated responses
**Method:** Count supporting evidence items per claim, calculate percentage of claims with evidence
**MVP Acceptance:** If evidence coverage shows measurable improvement over baseline, proceed to integration testing

## Citation/Source Accuracy
**Purpose:** Measure correctness of source attribution in generated responses
**Method:** Verify source citations against original documents, calculate accuracy percentage
**MVP Acceptance:** If citation accuracy exceeds 70% threshold, proceed to full evaluation

## Unsupported-Claim Rate
**Purpose:** Measure proportion of claims in responses that lack supporting evidence
**Method:** Identify claims without evidence, calculate percentage of total claims
**MVP Acceptance:** If unsupported-claim rate is below 15%, consider acceptable for MVP

## Multi-hop Correctness
**Purpose:** Measure accuracy of responses requiring information synthesis across multiple sources
**Method:** Human evaluation of multi-hop answers against ground truth, calculate accuracy percentage
**MVP Acceptance:** If multi-hop accuracy exceeds 60% threshold, proceed to broader testing

## RAG vs Wiki Baseline Answer Quality
**Purpose:** Compare answer quality between RAG and wiki baseline approaches
**Method:** Human evaluation scoring (1-5 scale) on shared question set
**MVP Acceptance:** If RAG shows statistically significant improvement over wiki baseline, proceed to full implementation