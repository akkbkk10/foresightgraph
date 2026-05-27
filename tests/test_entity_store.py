"""Tests for the Entity Store module."""
import pytest
from datetime import datetime
from foresightgraph.entity_store import EntityRecord, EntityStore


class TestEntityRecord:
    def test_create_entity_record(self):
        now = datetime.now()
        rec = EntityRecord(
            entity_id="en_001",
            name="Test Entity",
            entity_type="person",
            aliases=["T. Entity", "Tester"],
            created_at=now,
        )
        assert rec.entity_id == "en_001"
        assert rec.name == "Test Entity"
        assert rec.entity_type == "person"
        assert rec.aliases == ["T. Entity", "Tester"]
        assert rec.created_at == now


class TestEntityStore:
    @pytest.fixture
    def store(self):
        return EntityStore()

    @pytest.fixture
    def sample_record(self):
        return EntityRecord(
            entity_id="en_001",
            name="Alpha",
            entity_type="organization",
            aliases=["A Corp", "AlphaCo"],
            created_at=datetime.now(),
        )

    def test_add_and_get(self, store, sample_record):
        store.add(sample_record)
        assert store.get("en_001") == sample_record

    def test_list_all_empty(self, store):
        assert store.list_all() == []

    def test_list_all_multiple(self, store):
        r1 = EntityRecord("en_001", "Alpha", "org", ["A"], datetime.now())
        r2 = EntityRecord("en_002", "Beta", "person", ["B"], datetime.now())
        store.add(r1)
        store.add(r2)
        allr = store.list_all()
        assert len(allr) == 2
        assert r1 in allr and r2 in allr

    def test_find_by_name(self, store):
        r1 = EntityRecord("en_001", "Alpha", "org", ["A"], datetime.now())
        r2 = EntityRecord("en_002", "alpha", "person", ["Al"], datetime.now())
        store.add(r1)
        store.add(r2)
        results = store.find_by_name("Alpha")
        assert len(results) == 2
        assert r1 in results and r2 in results

    def test_find_by_alias(self, store):
        r1 = EntityRecord("en_001", "Alpha", "org", ["A", "Common"], datetime.now())
        r2 = EntityRecord("en_002", "Beta", "person", ["Common", "B"], datetime.now())
        store.add(r1)
        store.add(r2)
        results = store.find_by_alias("common")
        assert len(results) == 2
        assert r1 in results and r2 in results

    def test_duplicate_entity_id_raises(self, store, sample_record):
        store.add(sample_record)
        dup = EntityRecord("en_001", "Different", "org", [], datetime.now())
        with pytest.raises(ValueError, match="Entity with id 'en_001' already exists"):
            store.add(dup)

    def test_empty_name_raises(self, store):
        rec = EntityRecord("en_001", "   ", "org", [], datetime.now())
        with pytest.raises(ValueError, match="name cannot be empty"):
            store.add(rec)

    def test_invalid_aliases_raises(self, store):
        rec1 = EntityRecord("en_001", "Name", "org", "not-a-list", datetime.now())
        rec2 = EntityRecord("en_002", "Name2", "org", ["ok", 123], datetime.now())
        with pytest.raises(ValueError, match="aliases must be a list of strings"):
            store.add(rec1)
        with pytest.raises(ValueError, match="aliases must be a list of strings"):
            store.add(rec2)

    def test_find_by_name_nonexistent(self, store):
        assert store.find_by_name("Nope") == []

    def test_find_by_alias_nonexistent(self, store):
        assert store.find_by_alias("Nope") == []
