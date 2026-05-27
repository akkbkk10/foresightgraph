"""Entity Store module for ForesightGraph."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class EntityRecord:
    """Represents an entity in the system."""
    entity_id: str
    name: str
    entity_type: str
    aliases: List[str]
    created_at: datetime


class EntityStore:
    """In-memory store for managing entity records."""

    def __init__(self):
        self._records: dict[str, EntityRecord] = {}
        self._name_index: dict[str, list[str]] = {}
        self._alias_index: dict[str, list[str]] = {}

    def add(self, record: EntityRecord) -> None:
        """
        Add an entity record to the store.

        Raises:
            ValueError: If entity_id already exists, name is empty, or aliases invalid.
        """
        if record.entity_id in self._records:
            raise ValueError(f"Entity with id '{record.entity_id}' already exists")

        if not record.name or not record.name.strip():
            raise ValueError("name cannot be empty")

        if not isinstance(record.aliases, list) or not all(isinstance(a, str) for a in record.aliases):
            raise ValueError("aliases must be a list of strings")

        self._records[record.entity_id] = record

        # index by name (case-insensitive)
        key = record.name.lower()
        self._name_index.setdefault(key, []).append(record.entity_id)

        # index by aliases (case-insensitive)
        for alias in record.aliases:
            akey = alias.lower()
            self._alias_index.setdefault(akey, []).append(record.entity_id)

    def get(self, entity_id: str) -> Optional[EntityRecord]:
        return self._records.get(entity_id)

    def list_all(self) -> list[EntityRecord]:
        return list(self._records.values())

    def find_by_name(self, name: str) -> list[EntityRecord]:
        ids = self._name_index.get(name.lower(), []) if name else []
        return [self._records[eid] for eid in ids]

    def find_by_alias(self, alias: str) -> list[EntityRecord]:
        ids = self._alias_index.get(alias.lower(), []) if alias else []
        return [self._records[eid] for eid in ids]
