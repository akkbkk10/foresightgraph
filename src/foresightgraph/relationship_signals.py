"""Relationship Signal Validation module for ForesightGraph."""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

# Allowed values for signal categories
SIGNAL_CATEGORIES = {
    "ecosystem_signal",
    "technical_integration_signal",
    "commercial_deal_signal",
    "capital_investment_signal",
    "acquisition_interest_signal",
    "acquisition_process_signal"
}

# Allowed values for orientation
ORIENTATIONS = {
    "partnership_likely",
    "acquisition_possible",
    "acquisition_likely",
    "confirmed_transaction"
}

# Allowed values for confidence
CONFIDENCE_LEVELS = {
    "low",
    "medium",
    "high"
}

# Allowed values for status
STATUSES = {
    "unverified",
    "watch",
    "confirmed_partnership",
    "acquisition_watch",
    "acquisition_process",
    "confirmed_transaction",
    "stale",
    "superseded"
}


@dataclass
class RelationshipSignalRecord:
    """Minimal validation for relationship signals based on methodology requirements."""
    signal_id: str
    source_company: str
    target_company: str
    relationship_type: str
    signal_category: str
    orientation: str
    evidence_ids: List[str]
    confidence: str
    signal_strength: int
    status: str
    observed_at: datetime
    last_verified_at: Optional[datetime]
    review_due_at: datetime
    
    def __post_init__(self):
        """Validate required fields and constraints."""
        # Validate signal_id is not empty
        if not self.signal_id or not self.signal_id.strip():
            raise ValueError("signal_id cannot be empty")
        
        # Validate required fields are not empty
        if not self.source_company or not self.source_company.strip():
            raise ValueError("source_company cannot be empty")
        if not self.target_company or not self.target_company.strip():
            raise ValueError("target_company cannot be empty")
        if not self.relationship_type or not self.relationship_type.strip():
            raise ValueError("relationship_type cannot be empty")
        
        # Validate signal_category is allowed
        if self.signal_category not in SIGNAL_CATEGORIES:
            raise ValueError(f"signal_category '{self.signal_category}' is not allowed. Must be one of: {SIGNAL_CATEGORIES}")
        
        # Validate orientation is allowed
        if self.orientation not in ORIENTATIONS:
            raise ValueError(f"orientation '{self.orientation}' is not allowed. Must be one of: {ORIENTATIONS}")
        
        # Validate confidence is allowed
        if self.confidence not in CONFIDENCE_LEVELS:
            raise ValueError(f"confidence '{self.confidence}' is not allowed. Must be one of: {CONFIDENCE_LEVELS}")
        
        # Validate status is allowed
        if self.status not in STATUSES:
            raise ValueError(f"status '{self.status}' is not allowed. Must be one of: {STATUSES}")
        
        # Validate evidence_ids is not empty
        if not self.evidence_ids:
            raise ValueError("evidence_ids cannot be empty")
        
        # Validate each evidence_id is a non-empty string
        for i, evidence_id in enumerate(self.evidence_ids):
            if not evidence_id or not evidence_id.strip():
                raise ValueError(f"evidence_ids[{i}] cannot be empty")
        
        # Validate signal_strength is between 1 and 10
        if self.signal_strength < 1 or self.signal_strength > 10:
            raise ValueError(f"signal_strength must be between 1 and 10, got {self.signal_strength}")
        
        # Validate datetime fields
        if not isinstance(self.observed_at, datetime):
            raise ValueError("observed_at must be a datetime object")
        
        if not isinstance(self.review_due_at, datetime):
            raise ValueError("review_due_at must be a datetime object")
        
        # last_verified_at can be None or datetime
        if self.last_verified_at is not None and not isinstance(self.last_verified_at, datetime):
            raise ValueError("last_verified_at must be None or a datetime object")