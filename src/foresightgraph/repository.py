"""ForesightGraph repository facade grouping all in-memory stores."""
from .source_registry import SourceRegistry
from .evidence_store import EvidenceStore
from .claim_store import ClaimStore
from .entity_store import EntityStore
from .edge_store import EdgeStore
from .review_store import ReviewStore


class ForesightGraphRepository:
    """Facade that provides access to all in-memory stores."""

    def __init__(self):
        self.sources = SourceRegistry()
        self.evidence = EvidenceStore()
        self.claims = ClaimStore()
        self.entities = EntityStore()
        self.edges = EdgeStore()
        self.reviews = ReviewStore()
