# Multi-Hop Questions

This directory contains multi-hop benchmark questions used for evaluating ForesightGraph's reasoning capabilities.

## Purpose

The questions in this directory are designed to test multi-hop reasoning capabilities by requiring connections between multiple knowledge sources. These questions form the basis for evaluating different baseline approaches in the ForesightGraph evaluation protocol.

## Question File Structure

Questions are stored in JSONL (JSON Lines) format, where each line is a complete JSON object representing a single question.

### File Naming Convention

Question files should be named following this pattern:
- `questions_vX.Y.jsonl` - for versioned question sets
- `sample_questions_vX.Y.jsonl` - for sample question sets
- `benchmark_questions_vX.Y.jsonl` - for official benchmark question sets

### Question Format

Each question follows the schema defined in `evals/golden_sets/multi_hop_question_schema.md`. Questions must be reviewed and approved before being used in official evaluations.

## Review Process

All questions must undergo a review process before being marked as "approved":

1. **Draft Stage**: Questions are created and initially formatted
2. **Expert Review**: Questions are reviewed by domain experts for accuracy and appropriateness
3. **Approval**: Questions are marked as "approved" after successful review
4. **Usage**: Approved questions can be used in benchmark evaluations

## Usage Guidelines

### For Evaluation

- Only use questions marked as "approved" for official benchmark results
- All benchmark results must include human review documentation
- Do not claim benchmark performance without proper review

### For Development

- Use sample questions for testing and development
- Create new questions following the established schema
- Maintain version control of question sets

## Sample Questions

The `sample_questions_v0.1.jsonl` file contains example questions that demonstrate the expected format and structure. These are for demonstration purposes only and should not be used for actual benchmarking.

## Note on Benchmark Results

**No real benchmark result should be claimed without proper human review and approval.** All evaluation results must undergo human verification before being considered valid for publication or performance claims.