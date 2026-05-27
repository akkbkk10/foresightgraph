"""Claim Store module for ForesightGraph."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ClaimRecord:
    """Represents a claim linked to a piece of evidence."""
    claim_id: str
    evidence_id: str
    text: str
    confidence: float
    review_status: str
    created_at: datetime


class ClaimStore:
    """In-memory store for managing claim records."""

    def __init__(self):
        self._records: dict[str, ClaimRecord] = {}
        self._evidence_index: dict[str, list[str]] = {}
        self._review_index: dict[str, list[str]] = {}

    def add(self, record: ClaimRecord) -> None:
        """
        Add a claim record to the store.

        Raises:
            ValueError: If claim_id already exists, text is empty, or confidence out of range.
        """
        if record.claim_id in self._records:
            raise ValueError(f"Claim with id '{record.claim_id}' already exists")

        if not record.text or not record.text.strip():
            raise ValueError("text cannot be empty")

        if not isinstance(record.confidence, (int, float)) or not (0.0 <= record.confidence <= 1.0):
            raise ValueError("confidence must be between 0.0 and 1.0")

        self._records[record.claim_id] = record

        # index by evidence
        self._evidence_index.setdefault(record.evidence_id, []).append(record.claim_id)
        # index by review_status
        self._review_index.setdefault(record.review_status, []).append(record.claim_id)

    def get(self, claim_id: str) -> Optional[ClaimRecord]:
        return self._records.get(claim_id)

    def list_all(self) -> list[ClaimRecord]:
        return list(self._records.values())

    def list_by_evidence(self, evidence_id: str) -> list[ClaimRecord]:
        ids = self._evidence_index.get(evidence_id, [])
        return [self._records[cid] for cid in ids]

    def list_by_review_status(self, review_status: str) -> list[ClaimRecord]:
        ids = self._review_index.get(review_status, [])
        return [self._records[cid] for cid in ids]
