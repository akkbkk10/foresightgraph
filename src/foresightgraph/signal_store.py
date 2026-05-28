"""Signal Store module for ForesightGraph."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from .relationship_signals import RelationshipSignalRecord


class SignalStore:
    """In-memory store for managing relationship signal records."""

    def __init__(self):
        self._records: dict[str, RelationshipSignalRecord] = {}
        self._source_index: dict[str, list[str]] = {}
        self._target_index: dict[str, list[str]] = {}
        self._category_index: dict[str, list[str]] = {}
        self._status_index: dict[str, list[str]] = {}

    def add(self, record: RelationshipSignalRecord) -> None:
        """
        Add a relationship signal record to the store.

        Raises:
            ValueError: If signal_id already exists.
        """
        if record.signal_id in self._records:
            raise ValueError(f"Signal with id '{record.signal_id}' already exists")

        self._records[record.signal_id] = record

        # index by source_company
        self._source_index.setdefault(record.source_company, []).append(record.signal_id)
        
        # index by target_company
        self._target_index.setdefault(record.target_company, []).append(record.signal_id)
        
        # index by signal_category
        self._category_index.setdefault(record.signal_category, []).append(record.signal_id)
        
        # index by status
        self._status_index.setdefault(record.status, []).append(record.signal_id)

    def get(self, signal_id: str) -> Optional[RelationshipSignalRecord]:
        return self._records.get(signal_id)

    def list_all(self) -> list[RelationshipSignalRecord]:
        return list(self._records.values())

    def list_by_source(self, source_company: str) -> list[RelationshipSignalRecord]:
        ids = self._source_index.get(source_company, [])
        return [self._records[eid] for eid in ids]

    def list_by_target(self, target_company: str) -> list[RelationshipSignalRecord]:
        ids = self._target_index.get(target_company, [])
        return [self._records[eid] for eid in ids]

    def list_by_category(self, signal_category: str) -> list[RelationshipSignalRecord]:
        ids = self._category_index.get(signal_category, [])
        return [self._records[eid] for eid in ids]

    def list_by_status(self, status: str) -> list[RelationshipSignalRecord]:
        ids = self._status_index.get(status, [])
        return [self._records[eid] for eid in ids]

    def update(self, record: RelationshipSignalRecord) -> None:
        """
        Update an existing relationship signal record.
        
        Raises:
            ValueError: If signal_id does not exist.
        """
        if record.signal_id not in self._records:
            raise ValueError(f"Signal with id '{record.signal_id}' does not exist")

        # Remove old indexed entries
        old_record = self._records[record.signal_id]
        self._source_index[old_record.source_company].remove(record.signal_id)
        self._target_index[old_record.target_company].remove(record.signal_id)
        self._category_index[old_record.signal_category].remove(record.signal_id)
        self._status_index[old_record.status].remove(record.signal_id)

        # Add new indexed entries
        self._source_index.setdefault(record.source_company, []).append(record.signal_id)
        self._target_index.setdefault(record.target_company, []).append(record.signal_id)
        self._category_index.setdefault(record.signal_category, []).append(record.signal_id)
        self._status_index.setdefault(record.status, []).append(record.signal_id)

        # Update the record
        self._records[record.signal_id] = record

    def delete(self, signal_id: str) -> bool:
        """
        Delete a relationship signal record.
        
        Returns:
            bool: True if record was deleted, False if it didn't exist.
        """
        if signal_id not in self._records:
            return False

        record = self._records[signal_id]
        
        # Remove from indexes
        self._source_index[record.source_company].remove(signal_id)
        self._target_index[record.target_company].remove(signal_id)
        self._category_index[record.signal_category].remove(signal_id)
        self._status_index[record.status].remove(signal_id)
        
        # Remove the record
        del self._records[signal_id]
        return True