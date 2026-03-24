from __future__ import annotations

from fastapi import FastAPI

from .config import settings
from .models import HealthResponse, IngestRequest, IngestResponse, QueryRequest, QueryResponse
from .pipeline import RAGPipeline

app = FastAPI(title="rag-lite-kit", version="0.2.0")
pipeline = RAGPipeline()


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        vector_store=settings.vector_store,
        embedding_provider=settings.embedding_provider,
    )


@app.post("/ingest", response_model=IngestResponse)
def ingest(req: IngestRequest) -> IngestResponse:
    return pipeline.ingest(req.documents)


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest) -> QueryResponse:
    return pipeline.ask(req.question, top_k=req.top_k)


@app.post("/reset")
def reset() -> dict[str, str]:
    pipeline.reset()
    return {"status": "ok"}
