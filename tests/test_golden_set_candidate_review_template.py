from __future__ import annotations

from pathlib import Path


TEMPLATE_PATH = Path("reports/methodology/golden_set_candidate_review_template_v0.1.md")
REQUIRED_HEADINGS = (
    "# Golden Set Candidate Review Template v0.1",
    "## Purpose",
    "## Candidate Metadata",
    "## Source and Locator Review",
    "## Claim and Wording Review",
    "## Evidence Traceability",
    "## Uncertainty and Contradiction Review",
    "## Conservative Output Boundary",
    "## Forbidden Outputs",
    "## Reviewer Decision",
    "## Done Criteria",
)
REQUIRED_MARKERS = (
    "does not add new Golden Set records",
    "source",
    "locator",
    "item_type",
    "review status",
    "reviewer notes",
    "conservative wording",
    "uncertainty",
    "contradiction",
    "nvidia_ai_004",
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


def test_golden_set_candidate_review_template_exists() -> None:
    assert TEMPLATE_PATH.exists(), f"Template file is missing: {TEMPLATE_PATH}"


def test_golden_set_candidate_review_template_has_required_headings() -> None:
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS:
        assert heading in text, f"Missing required heading: {heading}"


def test_golden_set_candidate_review_template_has_required_markers() -> None:
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    text_lower = text.lower()
    missing = [marker for marker in REQUIRED_MARKERS if marker.lower() not in text_lower]
    assert not missing, f"Missing required markers: {missing}"


def test_golden_set_candidate_review_template_avoids_forbidden_overclaims() -> None:
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    text_lower = text.lower()
    present = [marker for marker in FORBIDDEN_OVERCLAIM_MARKERS if marker in text_lower]
    assert not present, f"Forbidden overclaim markers present: {present}"
