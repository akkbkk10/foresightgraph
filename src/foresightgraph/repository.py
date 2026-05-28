"""ForesightGraph repository facade grouping all in-memory stores."""
from .source_registry import SourceRegistry, SourceRecord
from .evidence_store import EvidenceStore, EvidenceRecord
from .claim_store import ClaimStore, ClaimRecord
from .entity_store import EntityStore, EntityRecord
from .edge_store import EdgeStore, EdgeRecord
from .review_store import ReviewStore, ReviewRecord
from .signal_store import SignalStore, RelationshipSignalRecord


class ForesightGraphRepository:
    """Facade that provides access to all in-memory stores."""

    def __init__(self):
        self.sources = SourceRegistry()
        self.evidence = EvidenceStore()
        self.claims = ClaimStore()
        self.entities = EntityStore()
        self.edges = EdgeStore()
        self.reviews = ReviewStore()
        self.signals = SignalStore()

    def add_source(self, record: SourceRecord) -> SourceRecord:
        self.sources.add(record)
        return record

    def add_evidence(self, record: EvidenceRecord) -> EvidenceRecord:
        self.evidence.add(record)
        return record

    def add_claim(self, record: ClaimRecord) -> ClaimRecord:
        self.claims.add(record)
        return record

    def add_entity(self, record: EntityRecord) -> EntityRecord:
        self.entities.add(record)
        return record

    def add_edge(self, record: EdgeRecord) -> EdgeRecord:
        self.edges.add(record)
        return record

    def add_review(self, record: ReviewRecord) -> ReviewRecord:
        self.reviews.add(record)
        return record

    def add_signal(self, record: RelationshipSignalRecord) -> RelationshipSignalRecord:
        self.signals.add(record)
        return record
