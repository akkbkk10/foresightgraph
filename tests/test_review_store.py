"""Tests for the Review Store module."""
import pytest
from datetime import datetime
from foresightgraph.review_store import ReviewRecord, ReviewStore


class TestReviewRecord:
    def test_create_review_record(self):
        now = datetime.now()
        rec = ReviewRecord(
            review_id="r_001",
            target_id="cl_001",
            target_type="claim",
            status="pending",
            reviewer="alice",
            comment="Looks ok",
            created_at=now,
        )
        assert rec.review_id == "r_001"
        assert rec.target_id == "cl_001"
        assert rec.target_type == "claim"
        assert rec.status == "pending"
        assert rec.reviewer == "alice"
        assert rec.comment == "Looks ok"
        assert rec.created_at == now


class TestReviewStore:
    @pytest.fixture
    def store(self):
        return ReviewStore()

    @pytest.fixture
    def sample_record(self):
        return ReviewRecord(
            review_id="r_001",
            target_id="cl_001",
            target_type="claim",
            status="pending",
            reviewer="alice",
            comment="Initial review",
            created_at=datetime.now(),
        )

    def test_add_and_get(self, store, sample_record):
        store.add(sample_record)
        assert store.get("r_001") == sample_record

    def test_list_all_empty(self, store):
        assert store.list_all() == []

    def test_list_all_multiple(self, store):
        r1 = ReviewRecord("r_001", "t1", "claim", "pending", "a", "c", datetime.now())
        r2 = ReviewRecord("r_002", "t2", "evidence", "approved", "b", "c2", datetime.now())
        store.add(r1)
        store.add(r2)
        allr = store.list_all()
        assert len(allr) == 2
        assert r1 in allr and r2 in allr

    def test_list_by_target(self, store):
        r1 = ReviewRecord("r_001", "t1", "claim", "pending", "a", "c", datetime.now())
        r2 = ReviewRecord("r_002", "t1", "claim", "approved", "b", "c2", datetime.now())
        r3 = ReviewRecord("r_003", "t2", "claim", "rejected", "c", "c3", datetime.now())
        store.add(r1)
        store.add(r2)
        store.add(r3)
        results = store.list_by_target("t1")
        assert len(results) == 2
        assert r1 in results and r2 in results
        assert store.list_by_target("nope") == []

    def test_list_by_status(self, store):
        r1 = ReviewRecord("r_001", "t1", "claim", "pending", "a", "c", datetime.now())
        r2 = ReviewRecord("r_002", "t2", "claim", "pending", "b", "c2", datetime.now())
        r3 = ReviewRecord("r_003", "t3", "claim", "approved", "c", "c3", datetime.now())
        store.add(r1)
        store.add(r2)
        store.add(r3)
        pending = store.list_by_status("pending")
        assert len(pending) == 2
        assert r1 in pending and r2 in pending
        assert store.list_by_status("nope") == []

    def test_duplicate_review_id_raises(self, store, sample_record):
        store.add(sample_record)
        dup = ReviewRecord("r_001", "tX", "claim", "pending", "d", "dup", datetime.now())
        with pytest.raises(ValueError, match="Review with id 'r_001' already exists"):
            store.add(dup)

    def test_empty_fields_raise(self, store):
        rec1 = ReviewRecord("r_001", "", "claim", "pending", "a", "c", datetime.now())
        rec2 = ReviewRecord("r_002", "t", "", "pending", "a", "c", datetime.now())
        rec3 = ReviewRecord("r_003", "t", "claim", "", "a", "c", datetime.now())
        rec4 = ReviewRecord("r_004", "t", "claim", "pending", "", "c", datetime.now())
        with pytest.raises(ValueError, match="target_id cannot be empty"):
            store.add(rec1)
        with pytest.raises(ValueError, match="target_type cannot be empty"):
            store.add(rec2)
        with pytest.raises(ValueError, match="status cannot be empty"):
            store.add(rec3)
        with pytest.raises(ValueError, match="reviewer cannot be empty"):
            store.add(rec4)

    def test_invalid_status_raises(self, store):
        rec = ReviewRecord("r_bad", "t", "claim", "unknown", "a", "c", datetime.now())
        with pytest.raises(ValueError, match="status must be one of:"):
            store.add(rec)
