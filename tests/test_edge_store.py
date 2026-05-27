"""Tests for the Edge Store module."""
import pytest
from datetime import datetime
from foresightgraph.edge_store import EdgeRecord, EdgeStore


class TestEdgeRecord:
    def test_create_edge_record(self):
        now = datetime.now()
        rec = EdgeRecord(
            edge_id="e_001",
            from_id="n1",
            to_id="n2",
            edge_type="related_to",
            evidence_id="ev_001",
            created_at=now,
        )
        assert rec.edge_id == "e_001"
        assert rec.from_id == "n1"
        assert rec.to_id == "n2"
        assert rec.edge_type == "related_to"
        assert rec.evidence_id == "ev_001"
        assert rec.created_at == now


class TestEdgeStore:
    @pytest.fixture
    def store(self):
        return EdgeStore()

    @pytest.fixture
    def sample_record(self):
        return EdgeRecord("e_001", "n1", "n2", "rel", "ev_1", datetime.now())

    def test_add_and_get(self, store, sample_record):
        store.add(sample_record)
        assert store.get("e_001") == sample_record

    def test_list_all_empty(self, store):
        assert store.list_all() == []

    def test_list_all_multiple(self, store):
        r1 = EdgeRecord("e_001", "n1", "n2", "rel", "ev_1", datetime.now())
        r2 = EdgeRecord("e_002", "n2", "n3", "rel", "ev_2", datetime.now())
        store.add(r1)
        store.add(r2)
        allr = store.list_all()
        assert len(allr) == 2
        assert r1 in allr and r2 in allr

    def test_list_by_from(self, store):
        r1 = EdgeRecord("e_001", "A", "B", "t1", "ev1", datetime.now())
        r2 = EdgeRecord("e_002", "A", "C", "t2", "ev2", datetime.now())
        r3 = EdgeRecord("e_003", "X", "A", "t1", "ev3", datetime.now())
        store.add(r1)
        store.add(r2)
        store.add(r3)
        results = store.list_by_from("A")
        assert len(results) == 2
        assert r1 in results and r2 in results

    def test_list_by_to(self, store):
        r1 = EdgeRecord("e_001", "A", "B", "t1", "ev1", datetime.now())
        r2 = EdgeRecord("e_002", "C", "B", "t2", "ev2", datetime.now())
        r3 = EdgeRecord("e_003", "B", "D", "t1", "ev3", datetime.now())
        store.add(r1)
        store.add(r2)
        store.add(r3)
        results = store.list_by_to("B")
        assert len(results) == 2
        assert r1 in results and r2 in results

    def test_list_by_type(self, store):
        r1 = EdgeRecord("e_001", "A", "B", "type1", "ev1", datetime.now())
        r2 = EdgeRecord("e_002", "C", "D", "type1", "ev2", datetime.now())
        r3 = EdgeRecord("e_003", "E", "F", "type2", "ev3", datetime.now())
        store.add(r1)
        store.add(r2)
        store.add(r3)
        results = store.list_by_type("type1")
        assert len(results) == 2
        assert r1 in results and r2 in results

    def test_duplicate_edge_id_raises(self, store, sample_record):
        store.add(sample_record)
        dup = EdgeRecord("e_001", "X", "Y", "t", "ev", datetime.now())
        with pytest.raises(ValueError, match="Edge with id 'e_001' already exists"):
            store.add(dup)

    def test_empty_from_to_type_raises(self, store):
        rec1 = EdgeRecord("e_001", "", "B", "t", "ev", datetime.now())
        rec2 = EdgeRecord("e_002", "A", " ", "t", "ev", datetime.now())
        rec3 = EdgeRecord("e_003", "A", "B", "", "ev", datetime.now())
        with pytest.raises(ValueError, match="from_id cannot be empty"):
            store.add(rec1)
        with pytest.raises(ValueError, match="to_id cannot be empty"):
            store.add(rec2)
        with pytest.raises(ValueError, match="edge_type cannot be empty"):
            store.add(rec3)

    def test_list_filters_nonexistent(self, store):
        assert store.list_by_from("nope") == []
        assert store.list_by_to("nope") == []
        assert store.list_by_type("nope") == []
