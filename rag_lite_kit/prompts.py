from __future__ import annotations

from .models import Reference


SYSTEM_INSTRUCTION = (
    "You are a retrieval QA assistant. Answer only from the retrieved context. "
    "If the answer is not supported, explicitly say you are not sure."
)


def build_rag_prompt(question: str, references: list[Reference]) -> str:
    context_block = "\n\n".join(
        f"[{ref.chunk_id}] {ref.text}" for ref in references
    )
    return (
        f"{SYSTEM_INSTRUCTION}\n\n"
        f"Question: {question}\n\n"
        f"Context:\n{context_block}\n\n"
        "Answer with short citations if possible."
    )
