from datetime import datetime
import pytest

from foresightgraph import (
    SourceRecord,
    EvidenceRecord,
    ClaimRecord,
    EntityRecord,
    EdgeRecord,
    ReviewRecord,
)
from foresightgraph.serialization import record_to_dict, record_from_dict


def roundtrip(record_type, record):
    d = record_to_dict(record)
    r2 = record_from_dict(record_type, d)
    assert r2 == record


def test_source_record_serialization():
    now = datetime.now()
    s = SourceRecord("s1", "Title", "article", "/p", now)
    d = record_to_dict(s)
    assert isinstance(d["created_at"], str)
    assert d["created_at"] == now.isoformat()
    roundtrip(SourceRecord, s)


def test_evidence_record_serialization():
    now = datetime.now()
    e = EvidenceRecord("e1", "s1", "loc", "excerpt", now)
    d = record_to_dict(e)
    assert isinstance(d["created_at"], str)
    roundtrip(EvidenceRecord, e)


def test_claim_record_serialization():
    now = datetime.now()
    c = ClaimRecord("c1", "e1", "A claim", 0.9, "pending", now)
    d = record_to_dict(c)
    assert isinstance(d["created_at"], str)
    roundtrip(ClaimRecord, c)


def test_entity_record_serialization():
    now = datetime.now()
    ent = EntityRecord("en1", "Name", "type", ["a1", "a2"], now)
    d = record_to_dict(ent)
    assert isinstance(d["aliases"], list)
    assert d["aliases"] == ["a1", "a2"]
    roundtrip(EntityRecord, ent)


def test_edge_record_serialization():
    now = datetime.now()
    ed = EdgeRecord("ed1", "en1", "en2", "rel", "e1", now)
    d = record_to_dict(ed)
    assert isinstance(d["created_at"], str)
    roundtrip(EdgeRecord, ed)


def test_review_record_serialization():
    now = datetime.now()
    rv = ReviewRecord("r1", "c1", "claim", "pending", "rev", "ok", now)
    d = record_to_dict(rv)
    assert isinstance(d["created_at"], str)
    roundtrip(ReviewRecord, rv)


def test_record_from_dict_unsupported_type_raises():
    with pytest.raises(TypeError):
        record_from_dict(int, {})
