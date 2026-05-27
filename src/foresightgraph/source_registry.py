"""Source Registry module for ForesightGraph."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class SourceRecord:
    """Represents a single source with metadata."""
    source_id: str
    title: str
    source_type: str
    path: str
    created_at: datetime


class SourceRegistry:
    """In-memory registry for storing and managing source records."""
    
    def __init__(self):
        """Initialize an empty source registry."""
        self._records: dict[str, SourceRecord] = {}
    
    def add(self, record: SourceRecord) -> None:
        """
        Add a source record to the registry.
        
        Args:
            record: The SourceRecord to add.
            
        Raises:
            ValueError: If a record with the same source_id already exists.
        """
        if record.source_id in self._records:
            raise ValueError(f"Source with id '{record.source_id}' already exists")
        self._records[record.source_id] = record
    
    def get(self, source_id: str) -> Optional[SourceRecord]:
        """
        Retrieve a source record by source_id.
        
        Args:
            source_id: The ID of the source to retrieve.
            
        Returns:
            The SourceRecord if found, None otherwise.
        """
        return self._records.get(source_id)
    
    def list_all(self) -> list[SourceRecord]:
        """
        List all source records in the registry.
        
        Returns:
            A list of all SourceRecord objects.
        """
        return list(self._records.values())
