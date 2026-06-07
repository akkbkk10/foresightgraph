from __future__ import annotations

import json
from pathlib import Path


DATASET_PATH = Path("evals/golden_sets/real_nvidia_ai_micro_v0.1.jsonl")
CHECKLIST_PATH = Path(
    "reports/methodology/citation_accuracy_checklist_nvidia_ai_micro_v0.1.md"
)
EXPECTED_IDS = {
    "nvidia_ai_001",
    "nvidia_ai_002",
    "nvidia_ai_003",
    "nvidia_ai_004",
    "nvidia_ai_005",
}
ALLOWED_ITEM_TYPES = {"question", "claim"}
TRACEABILITY_FIELDS = ("source_ids", "evidence_ids", "required_citations")
REVIEW_MARKERS = (
    "manufacturer_claim",
    "not_reproduced",
    "reviewed_vendor_claim_only",
)


def _read_dataset_lines() -> list[str]:
    assert DATASET_PATH.exists(), f"Golden-set file is missing: {DATASET_PATH}"
    text = DATASET_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    assert lines, f"Golden-set file is empty: {DATASET_PATH}"
    blank_lines = [index for index, line in enumerate(lines, start=1) if not line.strip()]
    assert not blank_lines, f"Golden-set file contains blank-only lines at: {blank_lines}"
    return lines


def _load_records() -> list[dict]:
    records = []
    for line_number, line in enumerate(_read_dataset_lines(), start=1):
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise AssertionError(
                f"Invalid JSON on line {line_number} of {DATASET_PATH}: {exc}"
            ) from exc
        assert isinstance(record, dict), f"Record {line_number} must decode to an object"
        records.append(record)
    return records


def _assert_non_empty_string(record: dict, field_name: str) -> None:
    value = record.get(field_name)
    assert isinstance(value, str) and value.strip(), (
        f"Record {record.get('item_id', '<missing item_id>')} needs non-empty "
        f"string field '{field_name}'"
    )


def _assert_non_empty_list(record: dict, field_name: str) -> None:
    value = record.get(field_name)
    assert isinstance(value, list), (
        f"Record {record.get('item_id', '<missing item_id>')} field '{field_name}' "
        "must be a list"
    )
    assert value, (
        f"Record {record.get('item_id', '<missing item_id>')} field '{field_name}' "
        "must not be empty"
    )
    for index, item in enumerate(value, start=1):
        assert isinstance(item, str) and item.strip(), (
            f"Record {record.get('item_id', '<missing item_id>')} field '{field_name}' "
            f"contains blank or non-string value at position {index}"
        )


def test_real_nvidia_micro_golden_set_file_level_contract():
    records = _load_records()
    assert len(records) == 5, "real_nvidia_ai_micro_v0.1.jsonl must contain exactly 5 records"

    item_ids = [record.get("item_id") for record in records]
    assert all(item_ids), "Every golden-set record must include item_id"
    assert len(item_ids) == len(set(item_ids)), "Golden-set item_id values must be unique"
    assert set(item_ids) == EXPECTED_IDS, (
        "Golden-set item_id set changed. "
        f"Expected {sorted(EXPECTED_IDS)}, got {sorted(item_ids)}"
    )


def test_real_nvidia_micro_golden_set_structure_and_traceability():
    for record in _load_records():
        _assert_non_empty_string(record, "item_id")
        _assert_non_empty_string(record, "item_type")
        assert record["item_type"] in ALLOWED_ITEM_TYPES, (
            f"Record {record['item_id']} has unsupported item_type {record['item_type']!r}"
        )

        _assert_non_empty_string(record, "question_or_claim")
        _assert_non_empty_string(record, "expected_answer_or_label")

        for field_name in TRACEABILITY_FIELDS:
            _assert_non_empty_list(record, field_name)

        _assert_non_empty_string(record, "review_status")
        _assert_non_empty_string(record, "reviewer_notes")


def test_real_nvidia_micro_golden_set_review_semantics_are_preserved():
    for record in _load_records():
        assert record["review_status"] == "draft", (
            f"Record {record['item_id']} review_status changed from the expected draft state"
        )
        notes = record["reviewer_notes"]
        assert "traceability" in notes, (
            f"Record {record['item_id']} reviewer_notes should preserve traceability wording"
        )
        for marker in REVIEW_MARKERS:
            assert marker in notes, (
                f"Record {record['item_id']} reviewer_notes must preserve '{marker}'"
            )


def test_nvidia_ai_004_has_traceability_metadata_and_conservative_checklist_guard():
    records_by_id = {record["item_id"]: record for record in _load_records()}
    assert "nvidia_ai_004" in records_by_id, "Expected record nvidia_ai_004 is missing"

    record = records_by_id["nvidia_ai_004"]
    assert record["item_type"] == "claim", "nvidia_ai_004 should remain a claim item"
    for field_name in TRACEABILITY_FIELDS:
        _assert_non_empty_list(record, field_name)
    _assert_non_empty_string(record, "review_status")
    _assert_non_empty_string(record, "reviewer_notes")

    assert CHECKLIST_PATH.exists(), f"Checklist file is missing: {CHECKLIST_PATH}"
    checklist_text = CHECKLIST_PATH.read_text(encoding="utf-8")
    assert "nvidia_ai_004" in checklist_text, "Checklist must still discuss nvidia_ai_004"
    for phrase in (
        "independent production readiness",
        "benchmark performance",
        "reproduced scalability",
        "operational validation",
    ):
        assert phrase in checklist_text, (
            "Checklist must preserve the conservative overclaim guard for nvidia_ai_004: "
            f"missing phrase {phrase!r}"
        )
