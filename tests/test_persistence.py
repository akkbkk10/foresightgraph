from datetime import datetime
import json
import pytest

from foresightgraph import (
    SourceRecord,
    EvidenceRecord,
    ClaimRecord,
    EntityRecord,
    EdgeRecord,
    ReviewRecord,
    ForesightGraphRepository,
)
from foresightgraph.persistence import (
    repository_to_dict,
    repository_from_dict,
    save_repository,
    load_repository,
)


def make_repo_with_one_each():
    repo = ForesightGraphRepository()
    now = datetime.now()

    s = SourceRecord("s1", "Title", "article", "/p", now)
    e = EvidenceRecord("e1", "s1", "loc", "excerpt", now)
    c = ClaimRecord("c1", "e1", "A", 0.5, "pending", now)
    ent = EntityRecord("en1", "Name", "type", ["a"], now)
    ed = EdgeRecord("ed1", "en1", "en1", "rel", "e1", now)
    rv = ReviewRecord("r1", "c1", "claim", "pending", "rev", "ok", now)

    repo.add_source(s)
    repo.add_evidence(e)
    repo.add_claim(c)
    repo.add_entity(ent)
    repo.add_edge(ed)
    repo.add_review(rv)

    return repo


def test_repository_roundtrip(tmp_path):
    repo = make_repo_with_one_each()
    p = tmp_path / "snapshot.json"

    save_repository(repo, p)

    loaded = load_repository(p)

    assert loaded.sources.get("s1") == repo.sources.get("s1")
    assert loaded.evidence.get("e1") == repo.evidence.get("e1")
    assert loaded.claims.get("c1") == repo.claims.get("c1")
    assert loaded.entities.get("en1") == repo.entities.get("en1")
    assert loaded.edges.get("ed1") == repo.edges.get("ed1")
    assert loaded.reviews.get("r1") == repo.reviews.get("r1")


def test_repository_from_dict_invalid_raises():
    with pytest.raises(TypeError):
        repository_from_dict({})

    with pytest.raises(TypeError):
        repository_from_dict({"sources": "notalist"})
