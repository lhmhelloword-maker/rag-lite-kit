# Architecture

## 1. Objective

`rag-lite-kit` is intentionally designed as a **portfolio-grade RAG starter**, not a research-heavy framework.
Its north star is: **clean structure, runnable demo, easy extension**.

## 2. Main flow

1. Load documents
2. Normalize and split text
3. Embed chunks
4. Store vectors
5. Retrieve top-k chunks
6. Build prompt
7. Generate answer
8. Return answer + references

## 3. Module responsibilities

- `loaders.py`: file and JSON ingestion helpers
- `splitter.py`: chunking and normalization
- `embeddings.py`: pluggable embedding providers
- `store.py`: pluggable vector store backends
- `retriever.py`: retrieval orchestration
- `prompts.py`: RAG prompt assembly
- `llm.py`: answer generation adapter
- `pipeline.py`: end-to-end orchestration
- `api.py`: FastAPI service layer
- `cli.py`: local developer entrypoint

## 4. Design decisions

### 4.1 Hash embeddings by default
The default path must be runnable in CI and on low-spec machines.
A deterministic hash-based embedding backend is enough to validate the engineering flow.

### 4.2 Memory store by default
This keeps tests fast and installation friction low.
Chroma remains optional for local persistence.

### 4.3 Provider abstraction
Real projects often swap models and vector stores many times.
Keeping these behind simple interfaces makes the project easier to evolve.

## 5. Suggested next extensions

- PDF / DOCX loaders
- metadata filtering
- reranker layer
- answer citation formatter
- OpenAI / Ollama adapters
- benchmark dataset and regression tests
