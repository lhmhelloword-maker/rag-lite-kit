from __future__ import annotations

from .embeddings import EmbeddingBackend
from .store import VectorRecord


class Retriever:
    def __init__(self, embedding_backend: EmbeddingBackend, store):
        self.embedding_backend = embedding_backend
        self.store = store

    def retrieve(self, question: str, top_k: int = 4) -> list[VectorRecord]:
        query_vector = self.embedding_backend.embed_query(question)
        return self.store.query(query_vector, top_k=top_k)
