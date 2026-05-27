"""Evidence Store module for ForesightGraph."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class EvidenceRecord:
    """Represents a single piece of evidence linked to a source."""
    evidence_id: str
    source_id: str
    locator: str
    text_excerpt: str
    created_at: datetime


class EvidenceStore:
    """In-memory store for managing evidence records."""
    
    def __init__(self):
        """Initialize an empty evidence store."""
        self._records: dict[str, EvidenceRecord] = {}
        self._source_index: dict[str, list[str]] = {}
    
    def add(self, record: EvidenceRecord) -> None:
        """
        Add an evidence record to the store.
        
        Args:
            record: The EvidenceRecord to add.
            
        Raises:
            ValueError: If evidence_id already exists or text_excerpt is empty.
        """
        if record.evidence_id in self._records:
            raise ValueError(f"Evidence with id '{record.evidence_id}' already exists")
        
        if not record.text_excerpt or not record.text_excerpt.strip():
            raise ValueError("text_excerpt cannot be empty")
        
        self._records[record.evidence_id] = record
        
        # Update source index
        if record.source_id not in self._source_index:
            self._source_index[record.source_id] = []
        self._source_index[record.source_id].append(record.evidence_id)
    
    def get(self, evidence_id: str) -> Optional[EvidenceRecord]:
        """
        Retrieve an evidence record by evidence_id.
        
        Args:
            evidence_id: The ID of the evidence to retrieve.
            
        Returns:
            The EvidenceRecord if found, None otherwise.
        """
        return self._records.get(evidence_id)
    
    def list_all(self) -> list[EvidenceRecord]:
        """
        List all evidence records in the store.
        
        Returns:
            A list of all EvidenceRecord objects.
        """
        return list(self._records.values())
    
    def list_by_source(self, source_id: str) -> list[EvidenceRecord]:
        """
        List all evidence records for a specific source.
        
        Args:
            source_id: The source ID to filter by.
            
        Returns:
            A list of EvidenceRecord objects for the source, or empty list if none found.
        """
        evidence_ids = self._source_index.get(source_id, [])
        return [self._records[eid] for eid in evidence_ids]
