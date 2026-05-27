# Metric Definitions

## Evidence Quality

### Evidence Relevance Score
**Purpose:** Measure how relevant retrieved evidence is to the query
**Method:** Binary classification (relevant/not relevant) - manually review 100 samples

### Evidence Completeness
**Purpose:** Measure coverage of evidence for claims
**Method:** Count supporting vs. contradicting evidence per claim

### Evidence Consistency
**Purpose:** Measure agreement between multiple evidence sources
**Method:** Calculate agreement percentage between 3+ sources

## Retrieval/Answer Quality

### Answer Accuracy
**Purpose:** Measure correctness of generated answers
**Method:** Manual verification of 50 answers against ground truth

### Answer Completeness
**Purpose:** Measure coverage of answer content
**Method:** Check if all query aspects are addressed (1-5 scale)

### Retrieval Precision
**Purpose:** Measure proportion of relevant results
**Method:** Calculate precision@k (k=10) from top results

## Graph/Wiki Health

### Graph Density
**Purpose:** Measure connectivity of knowledge graph
**Method:** Calculate ratio of actual edges to possible edges

### Entity Coverage
**Purpose:** Measure proportion of entities covered
**Method:** Count unique entities vs. total entities in knowledge base

### Claim Consistency
**Purpose:** Measure internal consistency of claims
**Method:** Count conflicting claims per entity

## Operational Quality

### Query Response Time
**Purpose:** Measure system performance
**Method:** Record average time for 100 queries

### System Availability
**Purpose:** Measure uptime reliability
**Method:** Track system downtime percentage over 24h period

### Error Rate
**Purpose:** Measure system reliability
**Method:** Count failed queries vs. total queries (1000 sample)