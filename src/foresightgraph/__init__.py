"""ForesightGraph package."""
from .claim_store import ClaimRecord, ClaimStore
from .edge_store import EdgeRecord, EdgeStore
from .entity_store import EntityRecord, EntityStore
from .evidence_store import EvidenceRecord, EvidenceStore
from .repository import ForesightGraphRepository
from .review_store import ReviewRecord, ReviewStore
from .source_registry import SourceRecord, SourceRegistry
from .persistence import repository_to_dict, repository_from_dict, save_repository, load_repository
from .eval_questions import load_jsonl_questions, validate_question_record

__all__ = [
    "__version__",
    "hello",
    "ForesightGraphRepository",
    "SourceRecord",
    "SourceRegistry",
    "EvidenceRecord",
    "EvidenceStore",
    "ClaimRecord",
    "ClaimStore",
    "EntityRecord",
    "EntityStore",
    "EdgeRecord",
    "EdgeStore",
    "ReviewRecord",
    "ReviewStore",
    "repository_to_dict",
    "repository_from_dict",
    "save_repository",
    "load_repository",
]

__version__ = "0.0.0"

def hello() -> str:
    return "hello from foresightgraph"
