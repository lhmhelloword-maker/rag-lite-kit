from __future__ import annotations

from dataclasses import dataclass
from typing import Any
import math

from .config import settings


@dataclass(slots=True)
class VectorRecord:
    chunk_id: str
    doc_id: str
    text: str
    embedding: list[float]
    metadata: dict[str, Any]


class InMemoryVectorStore:
    def __init__(self):
        self.records: list[VectorRecord] = []

    def add(self, records: list[VectorRecord]) -> None:
        self.records.extend(records)

    def reset(self) -> None:
        self.records = []

    def query(self, embedding: list[float], top_k: int = 4) -> list[VectorRecord]:
        scored = [(self._cosine_similarity(embedding, record.embedding), record) for record in self.records]
        scored.sort(key=lambda item: item[0], reverse=True)
        return [record for _, record in scored[:top_k]]

    @staticmethod
    def _cosine_similarity(left: list[float], right: list[float]) -> float:
        dot = sum(a * b for a, b in zip(left, right))
        left_norm = math.sqrt(sum(a * a for a in left)) or 1.0
        right_norm = math.sqrt(sum(b * b for b in right)) or 1.0
        return dot / (left_norm * right_norm)


class ChromaVectorStore:
    def __init__(self):
        try:
            import chromadb
        except ImportError as exc:
            raise RuntimeError(
                "chromadb is not installed. Use `pip install -e .[local]` or set VECTOR_STORE=memory."
            ) from exc
        self.client = chromadb.PersistentClient(path=settings.chroma_path)
        self.collection = self.client.get_or_create_collection(name=settings.collection_name)

    def add(self, records: list[VectorRecord]) -> None:
        self.collection.add(
            ids=[record.chunk_id for record in records],
            documents=[record.text for record in records],
            embeddings=[record.embedding for record in records],
            metadatas=[{"doc_id": record.doc_id, **record.metadata} for record in records],
        )

    def reset(self) -> None:
        self.client.delete_collection(settings.collection_name)
        self.collection = self.client.get_or_create_collection(name=settings.collection_name)

    def query(self, embedding: list[float], top_k: int = 4) -> list[VectorRecord]:
        raw = self.collection.query(query_embeddings=[embedding], n_results=top_k)
        documents = raw.get("documents", [[]])[0]
        metadatas = raw.get("metadatas", [[]])[0]
        ids = raw.get("ids", [[]])[0]
        results: list[VectorRecord] = []
        for text, metadata, chunk_id in zip(documents, metadatas, ids):
            metadata = metadata or {}
            results.append(
                VectorRecord(
                    chunk_id=chunk_id,
                    doc_id=metadata.get("doc_id", chunk_id.split(":", 1)[0]),
                    text=text,
                    embedding=[],
                    metadata=metadata,
                )
            )
        return results


def get_vector_store(store_name: str | None = None):
    store_name = (store_name or settings.vector_store).lower()
    if store_name == "memory":
        return InMemoryVectorStore()
    if store_name == "chroma":
        return ChromaVectorStore()
    raise ValueError(f"Unsupported vector store: {store_name}")
