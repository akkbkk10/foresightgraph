# ForesightGraph

**Evidence-first research system for structured knowledge discovery.**

## Status

Private local MVP scaffold. Early-stage development.

## Core Concept

ForesightGraph is an evidence-first research system that prioritizes sourced information and structured evidence collection over speculation.

## Local Setup

1. Ensure Python 3.8+ is installed
2. Navigate to the project directory
3. Install dependencies (when ready):
   ```bash
   pip install -e .
   ```

## Testing

Run the test suite:

```bash
python -m pytest tests
```

## Safety & Workflow Rules

All changes are reviewed with the following checks:

1. **Review changes**: `git diff`
2. **Run tests**: `python -m pytest tests`
3. **Check status**: `git status`

This ensures code quality and prevents unintended changes.