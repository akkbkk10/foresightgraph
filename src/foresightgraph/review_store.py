"""Review Store module for ForesightGraph."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class ReviewRecord:
    """Represents a review of a target (claim, evidence, etc.)."""
    review_id: str
    target_id: str
    target_type: str
    status: str
    reviewer: str
    comment: str
    created_at: datetime


class ReviewStore:
    """In-memory store for managing review records."""

    ALLOWED_STATUS = {"pending", "approved", "rejected", "needs_changes"}

    def __init__(self):
        self._records: dict[str, ReviewRecord] = {}
        self._target_index: dict[str, list[str]] = {}
        self._status_index: dict[str, list[str]] = {}

    def add(self, record: ReviewRecord) -> None:
        """
        Add a review record to the store.

        Raises:
            ValueError: If review_id already exists or required fields are invalid.
        """
        if record.review_id in self._records:
            raise ValueError(f"Review with id '{record.review_id}' already exists")

        if not record.target_id or not record.target_id.strip():
            raise ValueError("target_id cannot be empty")

        if not record.target_type or not record.target_type.strip():
            raise ValueError("target_type cannot be empty")

        if not record.status or not record.status.strip():
            raise ValueError("status cannot be empty")

        if record.status not in self.ALLOWED_STATUS:
            raise ValueError(f"status must be one of: {', '.join(sorted(self.ALLOWED_STATUS))}")

        if not record.reviewer or not record.reviewer.strip():
            raise ValueError("reviewer cannot be empty")

        self._records[record.review_id] = record

        self._target_index.setdefault(record.target_id, []).append(record.review_id)
        self._status_index.setdefault(record.status, []).append(record.review_id)

    def get(self, review_id: str) -> Optional[ReviewRecord]:
        return self._records.get(review_id)

    def list_all(self) -> list[ReviewRecord]:
        return list(self._records.values())

    def list_by_target(self, target_id: str) -> list[ReviewRecord]:
        ids = self._target_index.get(target_id, [])
        return [self._records[rid] for rid in ids]

    def list_by_status(self, status: str) -> list[ReviewRecord]:
        ids = self._status_index.get(status, [])
        return [self._records[rid] for rid in ids]
