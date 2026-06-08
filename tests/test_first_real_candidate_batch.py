from __future__ import annotations

import json
from pathlib import Path


CANDIDATE_PATH = Path("evals/golden_sets/candidates/first_real_candidate_batch_v0.1.jsonl")
BASELINE_PATH = Path("evals/golden_sets/real_nvidia_ai_micro_v0.1.jsonl")
REQUIRED_FIELDS = (
    "item_id",
    "item_type",
    "question",
    "expected_answer",
    "source_ids",
    "evidence_ids",
    "required_citations",
    "source",
    "locator",
    "review_status",
    "reviewer_notes",
    "uncertainty_notes",
    "contradiction_notes",
    "conservative_wording",
    "candidate_decision",
    "decision_reason",
)
FORBIDDEN_OUTPUT_STRINGS = (
    "buy",
    "sell",
    "hold",
    "price target",
    "broker integration",
    "autonomous trading",
    "investment recommendation",
    "benchmark proven",
    "production ready",
    "guaranteed",
)


def _load_records() -> list[dict]:
    assert CANDIDATE_PATH.exists(), f"Candidate batch file is missing: {CANDIDATE_PATH}"
    lines = CANDIDATE_PATH.read_text(encoding="utf-8").splitlines()
    assert lines, f"Candidate batch file is empty: {CANDIDATE_PATH}"
    records: list[dict] = []
    for line_number, line in enumerate(lines, start=1):
        assert line.strip(), f"Candidate batch contains blank line at {line_number}"
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise AssertionError(
                f"Invalid JSON on line {line_number} of {CANDIDATE_PATH}: {exc}"
            ) from exc
        assert isinstance(record, dict), f"Line {line_number} must decode to an object"
        records.append(record)
    return records


def _assert_non_empty_string(record: dict, field_name: str) -> None:
    value = record.get(field_name)
    assert isinstance(value, str) and value.strip(), (
        f"Record {record.get('item_id', '<missing item_id>')} needs non-empty string field {field_name!r}"
    )


def test_first_real_candidate_batch_exists_and_count_is_bounded() -> None:
    records = _load_records()
    assert 1 <= len(records) <= 3, "Candidate batch must contain between 1 and 3 records"


def test_first_real_candidate_batch_records_match_required_contract() -> None:
    records = _load_records()
    item_ids: list[str] = []
    for record in records:
        for field_name in REQUIRED_FIELDS:
            assert field_name in record, f"Missing required field {field_name!r} in {record}"

        _assert_non_empty_string(record, "item_id")
        _assert_non_empty_string(record, "item_type")
        _assert_non_empty_string(record, "question")
        _assert_non_empty_string(record, "expected_answer")
        _assert_non_empty_string(record, "source")
        _assert_non_empty_string(record, "locator")
        _assert_non_empty_string(record, "reviewer_notes")
        _assert_non_empty_string(record, "uncertainty_notes")
        _assert_non_empty_string(record, "contradiction_notes")
        _assert_non_empty_string(record, "decision_reason")

        assert isinstance(record["source_ids"], list) and record["source_ids"], "source_ids must be a non-empty list"
        assert isinstance(record["evidence_ids"], list) and record["evidence_ids"], "evidence_ids must be a non-empty list"
        assert isinstance(record["required_citations"], list) and record["required_citations"], (
            "required_citations must be a non-empty list"
        )
        assert record["review_status"] == "candidate", "review_status must be 'candidate'"
        assert record["candidate_decision"] == "needs_review", (
            "candidate_decision must be 'needs_review'"
        )
        assert record["conservative_wording"] is True, "conservative_wording must be true"

        item_ids.append(record["item_id"])

    assert len(item_ids) == len(set(item_ids)), "Candidate item_id values must be unique"


def test_first_real_candidate_batch_avoids_forbidden_outputs_and_keeps_baseline() -> None:
    records = _load_records()
    text = CANDIDATE_PATH.read_text(encoding="utf-8").lower()
    present = [marker for marker in FORBIDDEN_OUTPUT_STRINGS if marker in text]
    assert not present, f"Forbidden output strings present: {present}"
    assert BASELINE_PATH.exists(), f"Approved baseline file is missing: {BASELINE_PATH}"
