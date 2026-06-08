from __future__ import annotations

from pathlib import Path


CHECKLIST_PATH = Path("reports/methodology/golden_set_expansion_readiness_checklist_v0.1.md")
REQUIRED_HEADINGS = (
    "# Golden Set Expansion Readiness Checklist v0.1",
    "## Purpose",
    "## Methodology Files Required",
    "## Test Guardrails Required",
    "## Candidate Intake Readiness",
    "## Candidate Review Readiness",
    "## Candidate Decision Readiness",
    "## Source and Locator Readiness",
    "## Conservative Wording Readiness",
    "## Uncertainty and Contradiction Readiness",
    "## Forbidden Start Conditions",
    "## Start Criteria for First Candidate Batch",
    "## Done Criteria",
)
REQUIRED_MARKERS = (
    "does not add new Golden Set records",
    "protocol",
    "review template",
    "intake log",
    "decision log",
    "pytest guardrails",
    "source",
    "locator",
    "conservative wording",
    "uncertainty",
    "contradiction",
    "nvidia_ai_004",
    "small PRs",
    "pytest validation",
    "human review",
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


def test_golden_set_expansion_readiness_checklist_exists() -> None:
    assert CHECKLIST_PATH.exists(), f"Readiness checklist file is missing: {CHECKLIST_PATH}"


def test_golden_set_expansion_readiness_checklist_has_required_headings() -> None:
    text = CHECKLIST_PATH.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS:
        assert heading in text, f"Missing required heading: {heading}"


def test_golden_set_expansion_readiness_checklist_has_required_markers() -> None:
    text = CHECKLIST_PATH.read_text(encoding="utf-8")
    text_lower = text.lower()
    missing = [marker for marker in REQUIRED_MARKERS if marker.lower() not in text_lower]
    assert not missing, f"Missing required markers: {missing}"


def test_golden_set_expansion_readiness_checklist_avoids_forbidden_overclaims() -> None:
    text = CHECKLIST_PATH.read_text(encoding="utf-8")
    text_lower = text.lower()
    present = [marker for marker in FORBIDDEN_OVERCLAIM_MARKERS if marker in text_lower]
    assert not present, f"Forbidden overclaim markers present: {present}"
