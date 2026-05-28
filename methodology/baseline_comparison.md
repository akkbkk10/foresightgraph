# Baseline Comparison Methodology

This document outlines the baseline approaches for comparing different methodology approaches in the ForesightGraph project. These comparisons serve as research indicators to guide development priorities and understanding of different approaches, rather than providing absolute proof of superiority.

## Classic RAG

**Description:** Traditional Retrieval-Augmented Generation approach that retrieves relevant documents from a vector database and uses them to augment LLM responses.

**Expected Strength:** 
- Well-established approach with proven effectiveness
- Good at providing factual information from retrieved documents
- Clear separation of retrieval and generation components

**Expected Limitation:** 
- Lacks contextual understanding of relationships between entities
- May struggle with complex multi-hop queries
- Dependent on quality of vector embeddings and retrieval

**MVP Comparison Idea:** 
- Implement basic retrieval from existing document store
- Compare response quality with and without retrieval augmentation
- Measure retrieval accuracy and relevance scores

## LLM-Wiki / Markdown Knowledge Base

**Description:** Approach using LLMs to process and query markdown-based knowledge bases, treating documentation as structured information sources.

**Expected Strength:** 
- Leverages existing documentation structure
- Can handle domain-specific terminology well
- Easy to maintain and update documentation
- Natural language processing of structured content

**Expected Limitation:** 
- Limited to information present in documentation
- May not capture implicit relationships or emerging knowledge
- Requires good documentation quality and consistency
- Difficult to handle dynamic or rapidly changing information

**MVP Comparison Idea:** 
- Create markdown-based knowledge base from existing documentation
- Implement query interface for LLM to access structured content
- Compare response accuracy with traditional documentation approaches

## Hybrid Wiki Search

**Description:** Combination of traditional search (keyword-based) and semantic search approaches to provide more comprehensive results.

**Expected Strength:** 
- Combines the precision of keyword search with semantic understanding
- Can handle both explicit and implicit information retrieval
- Provides multiple search dimensions for better coverage
- More robust than single approach

**Expected Limitation:** 
- Increased complexity in implementation
- Requires careful tuning of search weights and parameters
- May introduce noise from combining different search approaches
- Higher computational overhead

**MVP Comparison Idea:** 
- Implement both keyword and semantic search components
- Create weighting system to combine search results
- Evaluate effectiveness of hybrid approach vs. individual approaches

## Graph-augmented Approach

**Description:** Approach that leverages graph structures to enhance information retrieval and generation by understanding relationships between entities.

**Expected Strength:** 
- Captures complex relationships and connections between entities
- Enables multi-hop reasoning and inference
- Provides contextual understanding of information
- Can handle emergent knowledge patterns

**Expected Limitation:** 
- Requires graph construction and maintenance
- May be computationally expensive
- Difficult to scale with large datasets
- Requires expertise in graph theory and implementation

**MVP Comparison Idea:** 
- Implement basic graph structure with entity relationships
- Compare response quality with and without graph augmentation
- Measure ability to handle relationship-based queries