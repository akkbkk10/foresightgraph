from __future__ import annotations

import json
from pathlib import Path


# Conservative drift guard only:
# These tests do not verify NVIDIA claims as factual truth.
# They verify that nvidia_ai_004 remains bounded to traceability,
# conservative wording, and explicit non-verification limitations
# across the golden set and the paired methodology reports.

REPO_ROOT = Path(__file__).resolve().parents[1]
GOLDEN_SET_PATH = REPO_ROOT / "evals/golden_sets/real_nvidia_ai_micro_v0.1.jsonl"
CHECKLIST_PATH = (
    REPO_ROOT
    / "reports/methodology/citation_accuracy_checklist_nvidia_ai_micro_v0.1.md"
)
CONTROLLED_REPORT_PATH = (
    REPO_ROOT
    / "reports/methodology/nvidia_ai_micro_controlled_answer_generation_results_v0.1.md"
)
MANUAL_REPORT_PATH = (
    REPO_ROOT / "reports/methodology/nvidia_ai_micro_manual_eval_results_v0.1.md"
)
ITEM_ID = "nvidia_ai_004"
STRICT_CHECKLIST_TERMS = (
    "needs_citation_fix",
    "wording must remain limited to vendor claims",
    "must not imply independent production readiness",
    "benchmark performance",
    "reproduced scalability",
    "operational validation",
)
BOUNDARY_LIMITATION_TERMS = (
    "no independent technical verification",
    "no benchmark result",
    "no investment conclusion",
    "no trading conclusion",
    "reviewed_vendor_claim_only",
    "manufacturer_claim",
    "not_reproduced",
    "draft",
)
CONTROLLED_ALLOWED_TRACEABILITY_STATUSES = (
    "PASS_EVIDENCE_BOUND",
    "NEEDS_CITATION_FIX",
    "NEEDS_MANUAL_REVIEW",
    "TRACEABILITY_ONLY_REVIEW_REQUIRED",
)
MANUAL_ALLOWED_TRACEABILITY_STATUSES = (
    "PASS_WITH_REVIEWED_EVIDENCE",
    "NEEDS_CITATION_FIX",
    "NEEDS_MANUAL_REVIEW",
    "TRACEABILITY_ONLY_REVIEW_REQUIRED",
)
FORBIDDEN_OVERCLAIM_TERMS = (
    "independent production readiness",
    "benchmark performance",
    "reproduced scalability",
    "operational validation",
    "real-world production validation",
    "independent technical proof",
    "investment/trading conclusion",
)


def _read_text(path: Path) -> str:
    assert path.exists(), f"Required file is missing: {path}"
    return path.read_text(encoding="utf-8")


def _load_jsonl(path: Path) -> list[dict]:
    assert path.exists(), f"Golden-set file is missing: {path}"
    rows = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise AssertionError(f"Invalid JSON on line {line_number} of {path}: {exc}") from exc
        assert isinstance(row, dict), f"JSONL row {line_number} must decode to an object"
        rows.append(row)
    return rows


def _line_containing(text: str, marker: str) -> str:
    marker_lower = marker.lower()
    for line in text.splitlines():
        if marker_lower in line.lower():
            return line
    raise AssertionError(f"Could not find marker {marker!r} in text")


def _markdown_table_row(text: str, item_id: str) -> str:
    prefix = f"| {item_id.lower()} |"
    for line in text.splitlines():
        if line.lower().startswith(prefix):
            return line
    raise AssertionError(f"Could not find markdown table row for {item_id!r}")


def _assert_contains_all(text: str, terms: tuple[str, ...]) -> None:
    text_lower = text.lower()
    missing = [term for term in terms if term.lower() not in text_lower]
    assert not missing, f"Missing expected terms: {missing}"


def _assert_contains_any(text: str, terms: tuple[str, ...]) -> None:
    text_lower = text.lower()
    assert any(term.lower() in text_lower for term in terms), (
        f"Expected one of {terms!r} in text, but none were present"
    )


def _assert_not_contains_any(text: str, forbidden_terms: tuple[str, ...]) -> None:
    text_lower = text.lower()
    present = [term for term in forbidden_terms if term.lower() in text_lower]
    assert not present, f"Forbidden overclaim terms present: {present}"


def test_nvidia_ai_004_exists_across_golden_set_and_reports():
    records = _load_jsonl(GOLDEN_SET_PATH)
    records_by_id = {record.get("item_id"): record for record in records}
    assert ITEM_ID in records_by_id, f"Expected {ITEM_ID} in golden set"
    assert records_by_id[ITEM_ID].get("item_type") == "claim", (
        f"Expected {ITEM_ID} to remain a claim item"
    )

    for path in (CHECKLIST_PATH, CONTROLLED_REPORT_PATH, MANUAL_REPORT_PATH):
        text = _read_text(path)
        assert ITEM_ID in text, f"Expected {ITEM_ID} in {path}"


def test_nvidia_ai_004_checklist_preserves_strict_conservative_status():
    checklist_text = _read_text(CHECKLIST_PATH)
    checklist_line = _markdown_table_row(checklist_text, ITEM_ID)

    assert "NEEDS_CITATION_FIX" in checklist_line, (
        "The citation checklist must remain the strictest reference point for nvidia_ai_004"
    )
    _assert_contains_all(checklist_text, STRICT_CHECKLIST_TERMS)


def test_nvidia_ai_004_reports_preserve_traceability_not_verification_boundary():
    controlled_text = _read_text(CONTROLLED_REPORT_PATH)
    manual_text = _read_text(MANUAL_REPORT_PATH)

    controlled_line = _markdown_table_row(controlled_text, ITEM_ID)
    manual_line = _markdown_table_row(manual_text, ITEM_ID)

    # Current reports use PASS-style traceability labels, but future report fixes may
    # tighten them to stricter conservative statuses. The invariant here is the
    # traceability-vs-verification boundary, not the exact current PASS label.
    _assert_contains_any(controlled_line, CONTROLLED_ALLOWED_TRACEABILITY_STATUSES)
    _assert_contains_any(manual_line, MANUAL_ALLOWED_TRACEABILITY_STATUSES)

    _assert_contains_all(controlled_text, BOUNDARY_LIMITATION_TERMS)
    _assert_contains_all(manual_text, (
        "no independent technical verification",
        "no independent benchmarking or performance assessment",
        "investment thesis or trading conclusions",
        "draft status",
    ))

    assert "does not treat vendor claims as independently verified facts" in controlled_text.lower(), (
        "Controlled report must distinguish traceability from factual proof"
    )
    assert "traceability and evidence verification only" in manual_text.lower(), (
        "Manual report must distinguish traceability from factual or operational proof"
    )


def test_nvidia_ai_004_wording_does_not_introduce_forbidden_overclaims():
    checklist_text = _read_text(CHECKLIST_PATH).lower()
    checklist_line = _markdown_table_row(checklist_text, ITEM_ID).lower()
    controlled_line = _markdown_table_row(_read_text(CONTROLLED_REPORT_PATH), ITEM_ID).lower()
    manual_line = _markdown_table_row(_read_text(MANUAL_REPORT_PATH), ITEM_ID).lower()

    # The checklist is allowed to mention forbidden ideas only as warnings.
    _assert_contains_all(
        checklist_line,
        (
            "needs_citation_fix",
            "must not imply independent production readiness",
            "benchmark performance",
            "reproduced scalability",
            "operational validation",
        ),
    )

    for bounded_line in (controlled_line, manual_line):
        _assert_not_contains_any(bounded_line, FORBIDDEN_OVERCLAIM_TERMS)
        assert "supported by the cited evidence" in bounded_line, (
            "Report wording should stay in traceability language"
        )
        assert "independently verified" not in bounded_line, (
            "Per-item report wording must not claim independent verification"
        )
