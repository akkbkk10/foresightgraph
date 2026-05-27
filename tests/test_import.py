def test_import_package():
    import foresightgraph

    assert hasattr(foresightgraph, "__version__")
    assert foresightgraph.hello() == "hello from foresightgraph"
    assert hasattr(foresightgraph, "ForesightGraphRepository")
    assert hasattr(foresightgraph, "SourceRecord")
    assert hasattr(foresightgraph, "SourceRegistry")
    assert hasattr(foresightgraph, "EvidenceRecord")
    assert hasattr(foresightgraph, "EvidenceStore")
    assert hasattr(foresightgraph, "ClaimRecord")
    assert hasattr(foresightgraph, "ClaimStore")
    assert hasattr(foresightgraph, "EntityRecord")
    assert hasattr(foresightgraph, "EntityStore")
    assert hasattr(foresightgraph, "EdgeRecord")
    assert hasattr(foresightgraph, "EdgeStore")
    assert hasattr(foresightgraph, "ReviewRecord")
    assert hasattr(foresightgraph, "ReviewStore")


def test_from_imports_package_exports():
    from foresightgraph import (
        ForesightGraphRepository,
        SourceRecord,
        SourceRegistry,
        EvidenceRecord,
        EvidenceStore,
        ClaimRecord,
        ClaimStore,
        EntityRecord,
        EntityStore,
        EdgeRecord,
        EdgeStore,
        ReviewRecord,
        ReviewStore,
    )

    assert ForesightGraphRepository is not None
    assert SourceRecord is not None
    assert SourceRegistry is not None
    assert EvidenceRecord is not None
    assert EvidenceStore is not None
    assert ClaimRecord is not None
    assert ClaimStore is not None
    assert EntityRecord is not None
    assert EntityStore is not None
    assert EdgeRecord is not None
    assert EdgeStore is not None
    assert ReviewRecord is not None
    assert ReviewStore is not None
