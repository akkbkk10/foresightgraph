"""Tests for the Claim Store module."""
import pytest
from datetime import datetime
from foresightgraph.claim_store import ClaimRecord, ClaimStore


class TestClaimRecord:
    def test_create_claim_record(self):
        now = datetime.now()
        record = ClaimRecord(
            claim_id="cl_001",
            evidence_id="ev_001",
            text="This is a claim.",
            confidence=0.75,
            review_status="pending",
            created_at=now,
        )
        assert record.claim_id == "cl_001"
        assert record.evidence_id == "ev_001"
        assert record.text == "This is a claim."
        assert record.confidence == 0.75
        assert record.review_status == "pending"
        assert record.created_at == now


class TestClaimStore:
    @pytest.fixture
    def store(self):
        return ClaimStore()

    @pytest.fixture
    def sample_record(self):
        return ClaimRecord(
            claim_id="cl_001",
            evidence_id="ev_001",
            text="A sample claim",
            confidence=0.5,
            review_status="pending",
            created_at=datetime.now(),
        )

    def test_add_and_get(self, store, sample_record):
        store.add(sample_record)
        retrieved = store.get("cl_001")
        assert retrieved == sample_record

    def test_list_all_empty(self, store):
        assert store.list_all() == []

    def test_list_all_multiple(self, store):
        r1 = ClaimRecord("cl_001", "ev_001", "c1", 0.2, "pending", datetime.now())
        r2 = ClaimRecord("cl_002", "ev_002", "c2", 0.8, "accepted", datetime.now())
        store.add(r1)
        store.add(r2)
        all_records = store.list_all()
        assert len(all_records) == 2
        assert r1 in all_records and r2 in all_records

    def test_list_by_evidence(self, store):
        r1 = ClaimRecord("cl_001", "ev_001", "c1", 0.2, "pending", datetime.now())
        r2 = ClaimRecord("cl_002", "ev_001", "c2", 0.9, "rejected", datetime.now())
        r3 = ClaimRecord("cl_003", "ev_002", "c3", 0.6, "pending", datetime.now())
        store.add(r1)
        store.add(r2)
        store.add(r3)
        ev1 = store.list_by_evidence("ev_001")
        assert len(ev1) == 2
        assert r1 in ev1 and r2 in ev1
        ev2 = store.list_by_evidence("ev_002")
        assert ev2 == [r3]

    def test_list_by_review_status(self, store):
        r1 = ClaimRecord("cl_001", "ev_001", "c1", 0.2, "pending", datetime.now())
        r2 = ClaimRecord("cl_002", "ev_002", "c2", 0.9, "accepted", datetime.now())
        r3 = ClaimRecord("cl_003", "ev_001", "c3", 0.6, "pending", datetime.now())
        store.add(r1)
        store.add(r2)
        store.add(r3)
        pending = store.list_by_review_status("pending")
        assert len(pending) == 2
        assert r1 in pending and r3 in pending
        accepted = store.list_by_review_status("accepted")
        assert accepted == [r2]

    def test_duplicate_claim_id_raises(self, store, sample_record):
        store.add(sample_record)
        dup = ClaimRecord("cl_001", "ev_999", "dup", 0.1, "pending", datetime.now())
        with pytest.raises(ValueError, match="Claim with id 'cl_001' already exists"):
            store.add(dup)

    def test_empty_text_raises(self, store):
        rec = ClaimRecord("cl_001", "ev_001", "", 0.5, "pending", datetime.now())
        with pytest.raises(ValueError, match="text cannot be empty"):
            store.add(rec)

    def test_invalid_confidence_raises(self, store):
        rec_low = ClaimRecord("cl_low", "ev_001", "c", -0.1, "pending", datetime.now())
        rec_high = ClaimRecord("cl_high", "ev_001", "c", 1.5, "pending", datetime.now())
        with pytest.raises(ValueError, match="confidence must be between 0.0 and 1.0"):
            store.add(rec_low)
        with pytest.raises(ValueError, match="confidence must be between 0.0 and 1.0"):
            store.add(rec_high)
