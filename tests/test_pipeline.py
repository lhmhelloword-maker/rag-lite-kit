from rag_lite_kit.embeddings import HashEmbeddingBackend
from rag_lite_kit.models import DocumentIn
from rag_lite_kit.pipeline import RAGPipeline
from rag_lite_kit.store import InMemoryVectorStore


def test_pipeline_ingest_and_ask():
    pipeline = RAGPipeline(
        embedding_backend=HashEmbeddingBackend(dimensions=32),
        vector_store=InMemoryVectorStore(),
        chunk_size=120,
        overlap=20,
    )
    pipeline.ingest(
        [
            DocumentIn(doc_id="rag", text="RAG combines retrieval and generation for grounded answering."),
            DocumentIn(doc_id="chunking", text="Chunking affects recall and answer quality in retrieval systems."),
        ]
    )
    response = pipeline.ask("What affects answer quality?", top_k=2)
    assert response.references
    assert "chunking" in response.answer.lower() or "retrieval" in response.answer.lower()
