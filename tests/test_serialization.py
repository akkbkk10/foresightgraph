from datetime import datetime
import pytest

from foresightgraph import (
    SourceRecord,
    EvidenceRecord,
    ClaimRecord,
    EntityRecord,
    EdgeRecord,
    ReviewRecord,
    RelationshipSignalRecord,
)
from foresightgraph.serialization import record_to_dict, record_from_dict


def roundtrip(record_type, record):
    d = record_to_dict(record)
    r2 = record_from_dict(record_type, d)
    assert r2 == record


def test_source_record_serialization():
    now = datetime.now()
    s = SourceRecord("s1", "Title", "article", "/p", now)
    d = record_to_dict(s)
    assert isinstance(d["created_at"], str)
    assert d["created_at"] == now.isoformat()
    roundtrip(SourceRecord, s)


def test_evidence_record_serialization():
    now = datetime.now()
    e = EvidenceRecord("e1", "s1", "loc", "excerpt", now)
    d = record_to_dict(e)
    assert isinstance(d["created_at"], str)
    roundtrip(EvidenceRecord, e)


def test_claim_record_serialization():
    now = datetime.now()
    c = ClaimRecord("c1", "e1", "A claim", 0.9, "pending", now)
    d = record_to_dict(c)
    assert isinstance(d["created_at"], str)
    roundtrip(ClaimRecord, c)


def test_entity_record_serialization():
    now = datetime.now()
    ent = EntityRecord("en1", "Name", "type", ["a1", "a2"], now)
    d = record_to_dict(ent)
    assert isinstance(d["aliases"], list)
    assert d["aliases"] == ["a1", "a2"]
    roundtrip(EntityRecord, ent)


def test_edge_record_serialization():
    now = datetime.now()
    ed = EdgeRecord("ed1", "en1", "en2", "rel", "e1", now)
    d = record_to_dict(ed)
    assert isinstance(d["created_at"], str)
    roundtrip(EdgeRecord, ed)


def test_review_record_serialization():
    now = datetime.now()
    rv = ReviewRecord("r1", "c1", "claim", "pending", "rev", "ok", now)
    d = record_to_dict(rv)
    assert isinstance(d["created_at"], str)
    roundtrip(ReviewRecord, rv)


def test_record_from_dict_unsupported_type_raises():
    with pytest.raises(TypeError):
        record_from_dict(int, {})


def test_relationship_signal_record_serialization():
    """Test that RelationshipSignalRecord works with existing serialization helpers."""
    now = datetime.now()
    last_verified = datetime(2023, 1, 15, 10, 30, 0)
    review_due = datetime(2023, 2, 1, 14, 0, 0)

    # Create a valid RelationshipSignalRecord
    record = RelationshipSignalRecord(
        signal_id="signal-123",
        source_company="Company A",
        target_company="Company B",
        relationship_type="partnership",
        signal_category="ecosystem_signal",
        orientation="partnership_likely",
        evidence_ids=["e1", "e2", "e3"],
        confidence="high",
        signal_strength=8,
        status="watch",
        observed_at=now,
        last_verified_at=last_verified,
        review_due_at=review_due
    )
    
    # Test record_to_dict
    data = record_to_dict(record)
    
    # Verify datetime fields are serialized as ISO strings
    assert isinstance(data["observed_at"], str)
    assert data["observed_at"] == now.isoformat()
    assert isinstance(data["last_verified_at"], str)
    assert data["last_verified_at"] == last_verified.isoformat()
    assert isinstance(data["review_due_at"], str)
    assert data["review_due_at"] == review_due.isoformat()
    
    # Verify evidence_ids is preserved
    assert data["evidence_ids"] == ["e1", "e2", "e3"]
    
    # Verify signal fields are preserved
    assert data["source_company"] == "Company A"
    assert data["target_company"] == "Company B"
    assert data["relationship_type"] == "partnership"
    assert data["signal_category"] == "ecosystem_signal"
    assert data["orientation"] == "partnership_likely"
    assert data["confidence"] == "high"
    assert data["signal_strength"] == 8
    assert data["status"] == "watch"
    
    # Test record_from_dict
    restored_record = record_from_dict(RelationshipSignalRecord, data)
    
    # Verify the restored record has matching important fields
    assert restored_record.source_company == "Company A"
    assert restored_record.target_company == "Company B"
    assert restored_record.relationship_type == "partnership"
    assert restored_record.signal_category == "ecosystem_signal"
    assert restored_record.orientation == "partnership_likely"
    assert restored_record.evidence_ids == ["e1", "e2", "e3"]
    assert restored_record.confidence == "high"
    assert restored_record.signal_strength == 8
    assert restored_record.status == "watch"
    assert restored_record.observed_at == now
    assert restored_record.last_verified_at == last_verified
    assert restored_record.review_due_at == review_due


def test_relationship_signal_record_serialization_with_none_last_verified():
    """Test that RelationshipSignalRecord works with last_verified_at=None."""
    now = datetime.now()
    review_due = datetime(2023, 2, 1, 14, 0, 0)
    
    # Create a RelationshipSignalRecord with last_verified_at=None
    record = RelationshipSignalRecord(
        signal_id="signal-123",
        source_company="Company A",
        target_company="Company B",
        relationship_type="partnership",
        signal_category="ecosystem_signal",
        orientation="partnership_likely",
        evidence_ids=["e1", "e2"],
        confidence="medium",
        signal_strength=5,
        status="unverified",
        observed_at=now,
        last_verified_at=None,
        review_due_at=review_due
    )
    
    # Test record_to_dict
    data = record_to_dict(record)
    
    # Verify datetime fields are serialized as ISO strings
    assert isinstance(data["observed_at"], str)
    assert data["observed_at"] == now.isoformat()
    assert isinstance(data["review_due_at"], str)
    assert data["review_due_at"] == review_due.isoformat()
    
    # Verify last_verified_at is None in serialized data
    assert data["last_verified_at"] is None
    
    # Verify evidence_ids is preserved
    assert data["evidence_ids"] == ["e1", "e2"]
    
    # Verify signal fields are preserved
    assert data["source_company"] == "Company A"
    assert data["target_company"] == "Company B"
    assert data["relationship_type"] == "partnership"
    assert data["signal_category"] == "ecosystem_signal"
    assert data["orientation"] == "partnership_likely"
    assert data["confidence"] == "medium"
    assert data["signal_strength"] == 5
    assert data["status"] == "unverified"
    
    # Test record_from_dict
    restored_record = record_from_dict(RelationshipSignalRecord, data)
    
    # Verify the restored record has matching important fields
    assert restored_record.source_company == "Company A"
    assert restored_record.target_company == "Company B"
    assert restored_record.relationship_type == "partnership"
    assert restored_record.signal_category == "ecosystem_signal"
    assert restored_record.orientation == "partnership_likely"
    assert restored_record.evidence_ids == ["e1", "e2"]
    assert restored_record.confidence == "medium"
    assert restored_record.signal_strength == 5
    assert restored_record.status == "unverified"
    assert restored_record.observed_at == now
    assert restored_record.last_verified_at is None
    assert restored_record.review_due_at == review_due
