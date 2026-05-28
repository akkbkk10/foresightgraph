"""Tests for the Signal Store module."""
import pytest
from datetime import datetime
from foresightgraph.relationship_signals import RelationshipSignalRecord
from foresightgraph.signal_store import SignalStore


class TestSignalStore:
    @pytest.fixture
    def store(self):
        return SignalStore()

    @pytest.fixture
    def sample_record(self):
        return RelationshipSignalRecord(
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

    def test_add_and_get(self, store, sample_record):
        store.add(sample_record)
        assert store.get("signal-123") == sample_record

    def test_list_all_empty(self, store):
        assert store.list_all() == []

    def test_list_all_multiple(self, store):
        r1 = RelationshipSignalRecord(
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
            review_due_at=datetime.now()
        )
        r2 = RelationshipSignalRecord(
            signal_id="signal-456",
            source_company="Company C",
            target_company="Company D",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence2"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )
        store.add(r1)
        store.add(r2)
        allr = store.list_all()
        assert len(allr) == 2
        assert r1 in allr and r2 in allr

    def test_list_by_source(self, store):
        r1 = RelationshipSignalRecord(
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
            review_due_at=datetime.now()
        )
        r2 = RelationshipSignalRecord(
            signal_id="signal-456",
            source_company="Company A",
            target_company="Company C",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence2"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )
        store.add(r1)
        store.add(r2)
        results = store.list_by_source("Company A")
        assert len(results) == 2
        assert r1 in results and r2 in results

    def test_list_by_target(self, store):
        r1 = RelationshipSignalRecord(
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
            review_due_at=datetime.now()
        )
        r2 = RelationshipSignalRecord(
            signal_id="signal-456",
            source_company="Company C",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence2"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )
        store.add(r1)
        store.add(r2)
        results = store.list_by_target("Company B")
        assert len(results) == 2
        assert r1 in results and r2 in results

    def test_list_by_category(self, store):
        r1 = RelationshipSignalRecord(
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
            review_due_at=datetime.now()
        )
        r2 = RelationshipSignalRecord(
            signal_id="signal-456",
            source_company="Company C",
            target_company="Company D",
            relationship_type="strategic_partnership",
            signal_category="acquisition_interest_signal",  # Changed to valid category
            orientation="partnership_likely",
            evidence_ids=["evidence2"],
            confidence="high",
            signal_strength=8,
            status="watch",
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )
        store.add(r1)
        store.add(r2)
        results = store.list_by_category("ecosystem_signal")
        assert len(results) == 1
        assert r1 in results

    def test_list_by_status(self, store):
        r1 = RelationshipSignalRecord(
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
            review_due_at=datetime.now()
        )
        r2 = RelationshipSignalRecord(
            signal_id="signal-456",
            source_company="Company C",
            target_company="Company D",
            relationship_type="strategic_partnership",
            signal_category="ecosystem_signal",
            orientation="partnership_likely",
            evidence_ids=["evidence2"],
            confidence="high",
            signal_strength=8,
            status="confirmed_partnership",  # Changed to valid status
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )
        store.add(r1)
        store.add(r2)
        results = store.list_by_status("watch")
        assert len(results) == 1
        assert r1 in results

    def test_duplicate_signal_id_raises(self, store, sample_record):
        store.add(sample_record)
        dup = RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company C",
            target_company="Company D",
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
        with pytest.raises(ValueError, match="Signal with id 'signal-123' already exists"):
            store.add(dup)

    def test_update(self, store, sample_record):
        store.add(sample_record)
        
        # Update the record
        updated_record = RelationshipSignalRecord(
            signal_id="signal-123",
            source_company="Company A",
            target_company="Company B",
            relationship_type="strategic_partnership",
            signal_category="acquisition_interest_signal",  # Changed to valid category
            orientation="partnership_likely",
            evidence_ids=["evidence1", "evidence2"],
            confidence="high",
            signal_strength=8,
            status="confirmed_partnership",  # Changed to valid status
            observed_at=datetime.now(),
            last_verified_at=None,
            review_due_at=datetime.now()
        )
        
        store.update(updated_record)
        retrieved = store.get("signal-123")
        assert retrieved.signal_category == "acquisition_interest_signal"
        assert retrieved.status == "confirmed_partnership"

    def test_update_nonexistent_raises(self, store, sample_record):
        with pytest.raises(ValueError, match="Signal with id 'signal-123' does not exist"):
            store.update(sample_record)

    def test_delete(self, store, sample_record):
        store.add(sample_record)
        deleted = store.delete("signal-123")
        assert deleted is True
        assert store.get("signal-123") is None
        assert len(store.list_all()) == 0

    def test_delete_nonexistent(self, store):
        deleted = store.delete("nonexistent")
        assert deleted is False

    def test_delete_and_readd(self, store, sample_record):
        store.add(sample_record)
        store.delete("signal-123")
        store.add(sample_record)  # Should work fine
        assert store.get("signal-123") == sample_record