from __future__ import annotations

from .models import Reference


class MockLLM:
    def generate(self, question: str, references: list[Reference], prompt: str) -> str:
        if not references:
            return "I am not sure based on the retrieved context."
        top = references[0]
        return f"Based on the retrieved context, the best matching evidence is: {top.text} [{top.doc_id}:{top.chunk_id}]"
