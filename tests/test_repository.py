"""Tests for the ForesightGraphRepository facade."""
from datetime import datetime
from foresightgraph.repository import ForesightGraphRepository
from foresightgraph.source_registry import SourceRecord
from foresightgraph.evidence_store import EvidenceRecord
from foresightgraph.claim_store import ClaimRecord
from foresightgraph.entity_store import EntityRecord
from foresightgraph.edge_store import EdgeRecord
from foresightgraph.review_store import ReviewRecord
from foresightgraph.signal_store import SignalStore, RelationshipSignalRecord


def test_repository_initializes():
    repo = ForesightGraphRepository()
    assert repo.sources is not None
    assert repo.evidence is not None
    assert repo.claims is not None
    assert repo.entities is not None
    assert repo.edges is not None
    assert repo.reviews is not None


def test_stores_work_together():
    repo = ForesightGraphRepository()
    now = datetime.now()

    s = SourceRecord("src1", "Title", "article", "/path", now)
    repo.sources.add(s)

    e = EvidenceRecord("ev1", "src1", "loc", "excerpt", now)
    repo.evidence.add(e)

    cl = ClaimRecord("cl1", "ev1", "A claim", 0.5, "pending", now)
    repo.claims.add(cl)

    ent = EntityRecord("en1", "Name", "type", ["alias"], now)
    repo.entities.add(ent)

    ed = EdgeRecord("ed1", "en1", "en1", "rel", "ev1", now)
    repo.edges.add(ed)

    rv = ReviewRecord("r1", "cl1", "claim", "pending", "rev", "ok", now)
    repo.reviews.add(rv)

    assert repo.sources.get("src1") == s
    assert repo.evidence.get("ev1") == e
    assert repo.claims.get("cl1") == cl
    assert repo.entities.get("en1") == ent
    assert repo.edges.get("ed1") == ed
    assert repo.reviews.get("r1") == rv


def test_repository_add_wrappers_return_record():
    repo = ForesightGraphRepository()
    now = datetime.now()

    s = SourceRecord("src1", "Title", "article", "/path", now)
    e = EvidenceRecord("ev1", "src1", "loc", "excerpt", now)
    cl = ClaimRecord("cl1", "ev1", "A claim", 0.5, "pending", now)
    ent = EntityRecord("en1", "Name", "type", ["alias"], now)
    ed = EdgeRecord("ed1", "en1", "en1", "rel", "ev1", now)
    rv = ReviewRecord("r1", "cl1", "claim", "pending", "rev", "ok", now)

    assert repo.add_source(s) == s
    assert repo.add_evidence(e) == e
    assert repo.add_claim(cl) == cl
    assert repo.add_entity(ent) == ent
    assert repo.add_edge(ed) == ed
    assert repo.add_review(rv) == rv

    assert repo.sources.get("src1") == s
    assert repo.evidence.get("ev1") == e
    assert repo.claims.get("cl1") == cl
    assert repo.entities.get("en1") == ent
    assert repo.edges.get("ed1") == ed
    assert repo.reviews.get("r1") == rv


def test_repository_add_source_duplicate_raises():
    repo = ForesightGraphRepository()
    now = datetime.now()

    s = SourceRecord("src1", "Title", "article", "/path", now)
    repo.add_source(s)

    duplicate = SourceRecord("src1", "Title", "article", "/path", now)

    try:
        repo.add_source(duplicate)
        assert False, "Expected ValueError for duplicate source id"
    except ValueError as exc:
        assert "already exists" in str(exc)


def test_repository_signals_attribute():
    repo = ForesightGraphRepository()
    assert hasattr(repo, 'signals')
    assert isinstance(repo.signals, SignalStore)


def test_repository_add_signal_works():
    repo = ForesightGraphRepository()
    now = datetime.now()
    
    # Test that add_signal method exists and works
    record = RelationshipSignalRecord(
        signal_id="sig1",
        source_company="Company A",
        target_company="Company B",
        relationship_type="partnership",
        signal_category="commercial_deal_signal",
        orientation="partnership_likely",
        evidence_ids=["e1"],
        confidence="high",
        signal_strength=7,
        status="confirmed_partnership",
        observed_at=now,
        last_verified_at=None,
        review_due_at=now
    )
    
    result = repo.add_signal(record)
    assert result == record
    assert repo.signals.get("sig1") == record


def test_package_imports_work():
    import foresightgraph
    assert hasattr(foresightgraph, "SignalStore")
    assert hasattr(foresightgraph, "RelationshipSignalRecord")
    
    # Test from imports work
    from foresightgraph import SignalStore, RelationshipSignalRecord
    assert SignalStore is not None
    assert RelationshipSignalRecord is not None
