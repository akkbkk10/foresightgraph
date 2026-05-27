import json
from pathlib import Path
from typing import Any, Dict

from .repository import ForesightGraphRepository
from .serialization import record_to_dict, record_from_dict
from .source_registry import SourceRecord
from .evidence_store import EvidenceRecord
from .claim_store import ClaimRecord
from .entity_store import EntityRecord
from .edge_store import EdgeRecord
from .review_store import ReviewRecord


SECTIONS = [
    "sources",
    "evidence",
    "claims",
    "entities",
    "edges",
    "reviews",
]


def repository_to_dict(repository: ForesightGraphRepository) -> Dict[str, Any]:
    result: Dict[str, Any] = {}

    result["sources"] = [record_to_dict(r) for r in repository.sources.list_all()]
    result["evidence"] = [record_to_dict(r) for r in repository.evidence.list_all()]
    result["claims"] = [record_to_dict(r) for r in repository.claims.list_all()]
    result["entities"] = [record_to_dict(r) for r in repository.entities.list_all()]
    result["edges"] = [record_to_dict(r) for r in repository.edges.list_all()]
    result["reviews"] = [record_to_dict(r) for r in repository.reviews.list_all()]

    return result


def repository_from_dict(data: Dict[str, Any]) -> ForesightGraphRepository:
    if not isinstance(data, dict):
        raise TypeError("snapshot data must be a dict")

    for sec in SECTIONS:
        if sec not in data or not isinstance(data[sec], list):
            raise TypeError(f"snapshot missing or invalid section: {sec}")

    repo = ForesightGraphRepository()

    # helper to reconstruct and add
    for item in data["sources"]:
        r = record_from_dict(SourceRecord, item)
        repo.add_source(r)

    for item in data["evidence"]:
        r = record_from_dict(EvidenceRecord, item)
        repo.add_evidence(r)

    for item in data["claims"]:
        r = record_from_dict(ClaimRecord, item)
        repo.add_claim(r)

    for item in data["entities"]:
        r = record_from_dict(EntityRecord, item)
        repo.add_entity(r)

    for item in data["edges"]:
        r = record_from_dict(EdgeRecord, item)
        repo.add_edge(r)

    for item in data["reviews"]:
        r = record_from_dict(ReviewRecord, item)
        repo.add_review(r)

    return repo


def save_repository(repository: ForesightGraphRepository, path: Path) -> None:
    data = repository_to_dict(repository)
    text = json.dumps(data, indent=2, ensure_ascii=False)
    Path(path).write_text(text, encoding="utf-8")


def load_repository(path: Path) -> ForesightGraphRepository:
    text = Path(path).read_text(encoding="utf-8")
    data = json.loads(text)
    return repository_from_dict(data)
