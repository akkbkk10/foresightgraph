"""Tests for the Source Registry module."""
import pytest
from datetime import datetime
from foresightgraph.source_registry import SourceRecord, SourceRegistry


class TestSourceRecord:
    """Tests for the SourceRecord dataclass."""
    
    def test_create_source_record(self):
        """Test creating a SourceRecord."""
        now = datetime.now()
        record = SourceRecord(
            source_id="src_001",
            title="Test Source",
            source_type="article",
            path="/path/to/source",
            created_at=now
        )
        assert record.source_id == "src_001"
        assert record.title == "Test Source"
        assert record.source_type == "article"
        assert record.path == "/path/to/source"
        assert record.created_at == now


class TestSourceRegistry:
    """Tests for the SourceRegistry class."""
    
    @pytest.fixture
    def registry(self):
        """Create a fresh registry for each test."""
        return SourceRegistry()
    
    @pytest.fixture
    def sample_record(self):
        """Create a sample SourceRecord for testing."""
        return SourceRecord(
            source_id="src_001",
            title="Sample Source",
            source_type="article",
            path="/path/to/source",
            created_at=datetime.now()
        )
    
    def test_add_record(self, registry, sample_record):
        """Test adding a record to the registry."""
        registry.add(sample_record)
        assert registry.get("src_001") == sample_record
    
    def test_get_existing_record(self, registry, sample_record):
        """Test retrieving an existing record."""
        registry.add(sample_record)
        retrieved = registry.get("src_001")
        assert retrieved is not None
        assert retrieved.source_id == "src_001"
        assert retrieved.title == "Sample Source"
    
    def test_get_nonexistent_record(self, registry):
        """Test retrieving a non-existent record returns None."""
        result = registry.get("nonexistent")
        assert result is None
    
    def test_duplicate_source_id_raises_error(self, registry, sample_record):
        """Test that adding a record with duplicate source_id raises ValueError."""
        registry.add(sample_record)
        
        duplicate = SourceRecord(
            source_id="src_001",
            title="Duplicate Source",
            source_type="book",
            path="/different/path",
            created_at=datetime.now()
        )
        
        with pytest.raises(ValueError, match="Source with id 'src_001' already exists"):
            registry.add(duplicate)
    
    def test_list_all_empty(self, registry):
        """Test listing records from an empty registry."""
        records = registry.list_all()
        assert records == []
    
    def test_list_all_multiple_records(self, registry):
        """Test listing all records in the registry."""
        record1 = SourceRecord(
            source_id="src_001",
            title="Source 1",
            source_type="article",
            path="/path/1",
            created_at=datetime.now()
        )
        record2 = SourceRecord(
            source_id="src_002",
            title="Source 2",
            source_type="book",
            path="/path/2",
            created_at=datetime.now()
        )
        
        registry.add(record1)
        registry.add(record2)
        
        records = registry.list_all()
        assert len(records) == 2
        assert record1 in records
        assert record2 in records
