"""Edge Store module for ForesightGraph."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class EdgeRecord:
    """Represents a relationship (edge) between entities or nodes."""
    edge_id: str
    from_id: str
    to_id: str
    edge_type: str
    evidence_id: str
    created_at: datetime


class EdgeStore:
    """In-memory store for managing edge records."""

    def __init__(self):
        self._records: dict[str, EdgeRecord] = {}
        self._from_index: dict[str, list[str]] = {}
        self._to_index: dict[str, list[str]] = {}
        self._type_index: dict[str, list[str]] = {}

    def add(self, record: EdgeRecord) -> None:
        """
        Add an edge record to the store.

        Raises:
            ValueError: If edge_id already exists or required fields are empty.
        """
        if record.edge_id in self._records:
            raise ValueError(f"Edge with id '{record.edge_id}' already exists")

        if not record.from_id or not record.from_id.strip():
            raise ValueError("from_id cannot be empty")

        if not record.to_id or not record.to_id.strip():
            raise ValueError("to_id cannot be empty")

        if not record.edge_type or not record.edge_type.strip():
            raise ValueError("edge_type cannot be empty")

        self._records[record.edge_id] = record

        self._from_index.setdefault(record.from_id, []).append(record.edge_id)
        self._to_index.setdefault(record.to_id, []).append(record.edge_id)
        self._type_index.setdefault(record.edge_type, []).append(record.edge_id)

    def get(self, edge_id: str) -> Optional[EdgeRecord]:
        return self._records.get(edge_id)

    def list_all(self) -> list[EdgeRecord]:
        return list(self._records.values())

    def list_by_from(self, from_id: str) -> list[EdgeRecord]:
        ids = self._from_index.get(from_id, [])
        return [self._records[eid] for eid in ids]

    def list_by_to(self, to_id: str) -> list[EdgeRecord]:
        ids = self._to_index.get(to_id, [])
        return [self._records[eid] for eid in ids]

    def list_by_type(self, edge_type: str) -> list[EdgeRecord]:
        ids = self._type_index.get(edge_type, [])
        return [self._records[eid] for eid in ids]
