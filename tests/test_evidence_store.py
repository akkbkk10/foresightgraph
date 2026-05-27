"""Tests for the Evidence Store module."""
import pytest
from datetime import datetime
from foresightgraph.evidence_store import EvidenceRecord, EvidenceStore


class TestEvidenceRecord:
    """Tests for the EvidenceRecord dataclass."""
    
    def test_create_evidence_record(self):
        """Test creating an EvidenceRecord."""
        now = datetime.now()
        record = EvidenceRecord(
            evidence_id="ev_001",
            source_id="src_001",
            locator="page 42",
            text_excerpt="Important finding here",
            created_at=now
        )
        assert record.evidence_id == "ev_001"
        assert record.source_id == "src_001"
        assert record.locator == "page 42"
        assert record.text_excerpt == "Important finding here"
        assert record.created_at == now


class TestEvidenceStore:
    """Tests for the EvidenceStore class."""
    
    @pytest.fixture
    def store(self):
        """Create a fresh store for each test."""
        return EvidenceStore()
    
    @pytest.fixture
    def sample_record(self):
        """Create a sample EvidenceRecord for testing."""
        return EvidenceRecord(
            evidence_id="ev_001",
            source_id="src_001",
            locator="section 1.2",
            text_excerpt="This is evidence text",
            created_at=datetime.now()
        )
    
    def test_add_record(self, store, sample_record):
        """Test adding a record to the store."""
        store.add(sample_record)
        assert store.get("ev_001") == sample_record
    
    def test_get_existing_record(self, store, sample_record):
        """Test retrieving an existing record."""
        store.add(sample_record)
        retrieved = store.get("ev_001")
        assert retrieved is not None
        assert retrieved.evidence_id == "ev_001"
        assert retrieved.source_id == "src_001"
    
    def test_get_nonexistent_record(self, store):
        """Test retrieving a non-existent record returns None."""
        result = store.get("nonexistent")
        assert result is None
    
    def test_duplicate_evidence_id_raises_error(self, store, sample_record):
        """Test that adding a record with duplicate evidence_id raises ValueError."""
        store.add(sample_record)
        
        duplicate = EvidenceRecord(
            evidence_id="ev_001",
            source_id="src_002",
            locator="page 10",
            text_excerpt="Different evidence",
            created_at=datetime.now()
        )
        
        with pytest.raises(ValueError, match="Evidence with id 'ev_001' already exists"):
            store.add(duplicate)
    
    def test_empty_text_excerpt_raises_error(self, store):
        """Test that empty text_excerpt raises ValueError."""
        record = EvidenceRecord(
            evidence_id="ev_001",
            source_id="src_001",
            locator="page 1",
            text_excerpt="",
            created_at=datetime.now()
        )
        
        with pytest.raises(ValueError, match="text_excerpt cannot be empty"):
            store.add(record)
    
    def test_whitespace_only_text_excerpt_raises_error(self, store):
        """Test that whitespace-only text_excerpt raises ValueError."""
        record = EvidenceRecord(
            evidence_id="ev_001",
            source_id="src_001",
            locator="page 1",
            text_excerpt="   \n\t  ",
            created_at=datetime.now()
        )
        
        with pytest.raises(ValueError, match="text_excerpt cannot be empty"):
            store.add(record)
    
    def test_list_all_empty(self, store):
        """Test listing records from an empty store."""
        records = store.list_all()
        assert records == []
    
    def test_list_all_multiple_records(self, store):
        """Test listing all records in the store."""
        record1 = EvidenceRecord(
            evidence_id="ev_001",
            source_id="src_001",
            locator="page 1",
            text_excerpt="Evidence 1",
            created_at=datetime.now()
        )
        record2 = EvidenceRecord(
            evidence_id="ev_002",
            source_id="src_001",
            locator="page 2",
            text_excerpt="Evidence 2",
            created_at=datetime.now()
        )
        record3 = EvidenceRecord(
            evidence_id="ev_003",
            source_id="src_002",
            locator="chapter 3",
            text_excerpt="Evidence 3",
            created_at=datetime.now()
        )
        
        store.add(record1)
        store.add(record2)
        store.add(record3)
        
        records = store.list_all()
        assert len(records) == 3
        assert record1 in records
        assert record2 in records
        assert record3 in records
    
    def test_list_by_source_single_source(self, store):
        """Test listing evidence for a specific source."""
        record1 = EvidenceRecord(
            evidence_id="ev_001",
            source_id="src_001",
            locator="page 1",
            text_excerpt="Evidence 1",
            created_at=datetime.now()
        )
        record2 = EvidenceRecord(
            evidence_id="ev_002",
            source_id="src_001",
            locator="page 2",
            text_excerpt="Evidence 2",
            created_at=datetime.now()
        )
        
        store.add(record1)
        store.add(record2)
        
        results = store.list_by_source("src_001")
        assert len(results) == 2
        assert record1 in results
        assert record2 in results
    
    def test_list_by_source_multiple_sources(self, store):
        """Test listing evidence with multiple sources in store."""
        record1 = EvidenceRecord(
            evidence_id="ev_001",
            source_id="src_001",
            locator="page 1",
            text_excerpt="Evidence 1",
            created_at=datetime.now()
        )
        record2 = EvidenceRecord(
            evidence_id="ev_002",
            source_id="src_002",
            locator="chapter 2",
            text_excerpt="Evidence 2",
            created_at=datetime.now()
        )
        record3 = EvidenceRecord(
            evidence_id="ev_003",
            source_id="src_001",
            locator="page 5",
            text_excerpt="Evidence 3",
            created_at=datetime.now()
        )
        
        store.add(record1)
        store.add(record2)
        store.add(record3)
        
        src_001_results = store.list_by_source("src_001")
        assert len(src_001_results) == 2
        assert record1 in src_001_results
        assert record3 in src_001_results
        
        src_002_results = store.list_by_source("src_002")
        assert len(src_002_results) == 1
        assert record2 in src_002_results
    
    def test_list_by_source_nonexistent_source(self, store):
        """Test listing evidence for a non-existent source returns empty list."""
        record = EvidenceRecord(
            evidence_id="ev_001",
            source_id="src_001",
            locator="page 1",
            text_excerpt="Evidence 1",
            created_at=datetime.now()
        )
        store.add(record)
        
        results = store.list_by_source("nonexistent")
        assert results == []
