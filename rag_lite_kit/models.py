from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class DocumentIn(BaseModel):
    doc_id: str = Field(..., description="Unique document identifier")
    text: str = Field(..., min_length=1, description="Raw document text")
    metadata: dict[str, Any] = Field(default_factory=dict)


class IngestRequest(BaseModel):
    documents: list[DocumentIn]


class IngestResponse(BaseModel):
    status: str
    count: int


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1)
    top_k: int | None = Field(default=None, ge=1, le=20)


class Reference(BaseModel):
    doc_id: str
    chunk_id: str
    text: str
    score: float
    metadata: dict[str, Any] = Field(default_factory=dict)


class QueryResponse(BaseModel):
    answer: str
    references: list[Reference]


class HealthResponse(BaseModel):
    status: str
    vector_store: str
    embedding_provider: str
