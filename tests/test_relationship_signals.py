"""Tests for RelationshipSignalRecord validation."""
import pytest
from datetime import datetime
from foresightgraph.relationship_signals import RelationshipSignalRecord

def test_valid_relationship_signal_record():
    """Test that a valid relationship signal record can be created."""
    record = RelationshipSignalRecord(
        signal_id="signal-123",
        source_company="Company A",
        target_company="Company B",
        relationship_type="strategic_partnership",
        signal_category="ecosystem_signal",
        orientation="partnership_likely",
        evidence_ids=["evidence1", "evidence2"],
        confidence="high",
        signal_strength=8,
        status="watch",
        observed_at=datetime.now(),
        last_verified_at=None,
        review_due_at=datetime.now()
    )
    
    assert record.signal_id == "signal-123"
    assert record.source_company == "Company A"
    assert record.target_company == "Company B"
    assert record.relationship_type == "strategic_partnership"
    assert record.signal_category == "ecosystem_signal"
    assert record.orientation == "partnership_likely"
    assert record.evidence_ids == ["evidence1", "evidence2"]
    assert record.confidence == "high"
    assert record.signal_strength == 8
    assert record.status == "watch"
    assert record.observed_at is not None
    assert record.last_verified_at is None
    assert record.review_due_at is not None

def test_empty_source_company_raises_value_error():
    """Test that empty source_company raises ValueError."""
    with pytest.raises(ValueError, match="source_company cannot be empty"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_empty_target_company_raises_value_error():
    """Test that empty target_company raises ValueError."""
    with pytest.raises(ValueError, match="target_company cannot be empty"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_empty_relationship_type_raises_value_error():
    """Test that empty relationship_type raises ValueError."""
    with pytest.raises(ValueError, match="relationship_type cannot be empty"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_invalid_signal_category_raises_value_error():
    """Test that invalid signal_category raises ValueError."""
    with pytest.raises(ValueError, match="signal_category 'invalid_signal' is not allowed"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="invalid_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_invalid_orientation_raises_value_error():
    """Test that invalid orientation raises ValueError."""
    with pytest.raises(ValueError, match="orientation 'invalid_orientation' is not allowed"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="invalid_orientation",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_invalid_confidence_raises_value_error():
    """Test that invalid confidence raises ValueError."""
    with pytest.raises(ValueError, match="confidence 'invalid_confidence' is not allowed"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="invalid_confidence",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_invalid_status_raises_value_error():
    """Test that invalid status raises ValueError."""
    with pytest.raises(ValueError, match="status 'invalid_status' is not allowed"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="invalid_status",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_empty_evidence_ids_raises_value_error():
    """Test that empty evidence_ids raises ValueError."""
    with pytest.raises(ValueError, match="evidence_ids cannot be empty"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=[],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_empty_evidence_id_raises_value_error():
    """Test that empty evidence_id in list raises ValueError."""
    with pytest.raises(ValueError, match="evidence_ids\\[0\\] cannot be empty"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=[""],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_invalid_signal_strength_low_raises_value_error():
    """Test that signal_strength below 1 raises ValueError."""
    with pytest.raises(ValueError, match="signal_strength must be between 1 and 10"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=0,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_invalid_signal_strength_high_raises_value_error():
    """Test that signal_strength above 10 raises ValueError."""
    with pytest.raises(ValueError, match="signal_strength must be between 1 and 10"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=11,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_invalid_observed_at_raises_value_error():
    """Test that non-datetime observed_at raises ValueError."""
    with pytest.raises(ValueError, match="observed_at must be a datetime object"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at="not_a_datetime",
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_invalid_review_due_at_raises_value_error():
    """Test that non-datetime review_due_at raises ValueError."""
    with pytest.raises(ValueError, match="review_due_at must be a datetime object"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at="not_a_datetime"
        )

def test_invalid_last_verified_at_raises_value_error():
    """Test that non-datetime last_verified_at raises ValueError."""
    with pytest.raises(ValueError, match="last_verified_at must be None or a datetime object"):
        RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at="not_a_datetime",
            review_due_at=datetime.now()
        )

def test_empty_signal_id_raises_value_error():
    """Test that empty signal_id raises ValueError."""
    with pytest.raises(ValueError, match="signal_id cannot be empty"):
        RelationshipSignalRecord(
            signal_id="",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )

def test_whitespace_only_signal_id_raises_value_error():
    """Test that whitespace-only signal_id raises ValueError."""
    with pytest.raises(ValueError, match="signal_id cannot be empty"):
        RelationshipSignalRecord(
            signal_id="   ",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence1"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )
