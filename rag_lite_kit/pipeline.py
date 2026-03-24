from __future__ import annotations

from .config import settings
from .embeddings import EmbeddingBackend, get_embedding_backend
from .llm import MockLLM
from .models import DocumentIn, IngestResponse, QueryResponse, Reference
from .prompts import build_rag_prompt
from .retriever import Retriever
from .splitter import split_text
from .store import VectorRecord, get_vector_store


class RAGPipeline:
    def __init__(
        self,
        embedding_backend: EmbeddingBackend | None = None,
        vector_store=None,
        chunk_size: int | None = None,
        overlap: int | None = None,
    ):
        self.embedding_backend = embedding_backend or get_embedding_backend()
        self.store = vector_store or get_vector_store()
        self.chunk_size = chunk_size or settings.chunk_size
        self.overlap = overlap or settings.chunk_overlap
        self.retriever = Retriever(self.embedding_backend, self.store)
        self.llm = MockLLM()

    def ingest(self, documents: list[DocumentIn]) -> IngestResponse:
        records: list[VectorRecord] = []
        texts: list[str] = []
        identifiers: list[tuple[str, str, dict]] = []

        for doc in documents:
            chunks = split_text(doc.text, chunk_size=self.chunk_size, overlap=self.overlap)
            for index, chunk in enumerate(chunks):
                chunk_id = f"{doc.doc_id}:{index}"
                texts.append(chunk)
                identifiers.append((chunk_id, doc.doc_id, doc.metadata))

        if not texts:
            return IngestResponse(status="no documents ingested", count=0)

        embeddings = self.embedding_backend.embed_texts(texts)
        for (chunk_id, doc_id, metadata), chunk_text, embedding in zip(identifiers, texts, embeddings):
            records.append(
                VectorRecord(
                    chunk_id=chunk_id,
                    doc_id=doc_id,
                    text=chunk_text,
                    embedding=embedding,
                    metadata=metadata,
                )
            )

        self.store.add(records)
        return IngestResponse(status="ok", count=len(records))

    def ask(self, question: str, top_k: int | None = None) -> QueryResponse:
        top_k = top_k or settings.default_top_k
        records = self.retriever.retrieve(question, top_k=top_k)
        references = [
            Reference(
                doc_id=record.doc_id,
                chunk_id=record.chunk_id,
                text=record.text,
                score=float(index + 1),
                metadata=record.metadata,
            )
            for index, record in enumerate(records)
        ]
        prompt = build_rag_prompt(question, references)
        answer = self.llm.generate(question, references, prompt)
        return QueryResponse(answer=answer, references=references)

    def reset(self) -> None:
        reset = getattr(self.store, "reset", None)
        if callable(reset):
            reset()
