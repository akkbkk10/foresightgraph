from __future__ import annotations

from pathlib import Path


PROTOCOL_PATH = Path("reports/methodology/golden_set_expansion_protocol_v0.1.md")
REQUIRED_HEADINGS = (
    "# Golden Set Expansion Protocol v0.1",
    "## Purpose",
    "## Current Baseline",
    "## Expansion Principles",
    "## Candidate Item Requirements",
    "## Source and Locator Requirements",
    "## Conservative Wording Requirements",
    "## Required Review Fields",
    "## Validation Requirements",
    "## Forbidden Additions",
    "## Suggested Next Batches",
    "## Done Criteria",
)
REQUIRED_MARKERS = (
    "does not add new Golden Set records",
    "conservative wording",
    "source",
    "locator",
    "review status",
    "nvidia_ai_004",
    "small PRs",
    "investment/trading",
    "runtime provider integration",
    "provider SDK",
)
FORBIDDEN_OVERCLAIM_PATTERNS = (
    "benchmark proven",
    "production ready",
    "buy",
    "sell",
    "hold",
    "price target",
    "broker integration",
)


def test_golden_set_expansion_protocol_exists() -> None:
    assert PROTOCOL_PATH.exists(), f"Protocol file is missing: {PROTOCOL_PATH}"


def test_golden_set_expansion_protocol_has_required_headings() -> None:
    text = PROTOCOL_PATH.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS:
        assert heading in text, f"Missing required heading: {heading}"


def test_golden_set_expansion_protocol_has_required_markers() -> None:
    text = PROTOCOL_PATH.read_text(encoding="utf-8")
    text_lower = text.lower()
    missing = [marker for marker in REQUIRED_MARKERS if marker.lower() not in text_lower]
    assert not missing, f"Missing required markers: {missing}"


def test_golden_set_expansion_protocol_avoids_forbidden_overclaims() -> None:
    text = PROTOCOL_PATH.read_text(encoding="utf-8")
    text_lower = text.lower()
    present = [pattern for pattern in FORBIDDEN_OVERCLAIM_PATTERNS if pattern in text_lower]
    assert not present, f"Forbidden overclaim patterns present: {present}"
