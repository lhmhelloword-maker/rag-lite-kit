from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(slots=True)
class Settings:
    embedding_provider: str = os.getenv("EMBEDDING_PROVIDER", "hash")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    vector_store: str = os.getenv("VECTOR_STORE", "memory")
    chroma_path: str = os.getenv("CHROMA_PATH", ".chromadb")
    collection_name: str = os.getenv("COLLECTION_NAME", "rag-lite-kit")
    llm_backend: str = os.getenv("LLM_BACKEND", "mock")
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "400"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "80"))
    default_top_k: int = int(os.getenv("DEFAULT_TOP_K", "4"))


settings = Settings()
