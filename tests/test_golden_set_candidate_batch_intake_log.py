from __future__ import annotations

from pathlib import Path


LOG_PATH = Path("reports/methodology/golden_set_candidate_batch_intake_log_v0.1.md")
REQUIRED_HEADINGS = (
    "# Golden Set Candidate Batch Intake Log v0.1",
    "## Purpose",
    "## Batch Metadata",
    "## Candidate Source Summary",
    "## Candidate Item Summary",
    "## Review Boundary",
    "## Required Evidence Checks",
    "## Required Conservative Wording Checks",
    "## Uncertainty and Contradiction Checks",
    "## Forbidden Changes",
    "## Reviewer Decision Log",
    "## Follow-up Actions",
    "## Done Criteria",
)
REQUIRED_MARKERS = (
    "does not add new Golden Set records",
    "batch_id",
    "candidate_count",
    "source_count",
    "review status",
    "reviewer notes",
    "source",
    "locator",
    "conservative wording",
    "uncertainty",
    "contradiction",
    "nvidia_ai_004",
    "small PRs",
    "pytest validation",
    "JSONL",
    "investment/trading",
    "Buy/Sell/Hold",
    "price targets",
    "broker integration",
    "runtime provider integration",
    "provider SDK",
)
FORBIDDEN_OVERCLAIM_MARKERS = (
    "benchmark proven",
    "production ready",
    "guaranteed",
    "autonomous trading",
    "investment recommendation",
)


def test_golden_set_candidate_batch_intake_log_exists() -> None:
    assert LOG_PATH.exists(), f"Intake log file is missing: {LOG_PATH}"


def test_golden_set_candidate_batch_intake_log_has_required_headings() -> None:
    text = LOG_PATH.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS:
        assert heading in text, f"Missing required heading: {heading}"


def test_golden_set_candidate_batch_intake_log_has_required_markers() -> None:
    text = LOG_PATH.read_text(encoding="utf-8")
    text_lower = text.lower()
    missing = [marker for marker in REQUIRED_MARKERS if marker.lower() not in text_lower]
    assert not missing, f"Missing required markers: {missing}"


def test_golden_set_candidate_batch_intake_log_avoids_forbidden_overclaims() -> None:
    text = LOG_PATH.read_text(encoding="utf-8")
    text_lower = text.lower()
    present = [marker for marker in FORBIDDEN_OVERCLAIM_MARKERS if marker in text_lower]
    assert not present, f"Forbidden overclaim markers present: {present}"
