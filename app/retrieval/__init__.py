"""Retrieval layer for CMU student-support knowledge sources."""

from app.retrieval.retriever import retrieve_context
from app.retrieval.schemas import RetrievedDocument, RetrievalResult

__all__ = ["RetrievedDocument", "RetrievalResult", "retrieve_context"]
