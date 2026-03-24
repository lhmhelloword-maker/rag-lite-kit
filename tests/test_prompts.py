from rag_lite_kit.models import Reference
from rag_lite_kit.prompts import build_rag_prompt


def test_build_rag_prompt():
    prompt = build_rag_prompt(
        "What is RAG?",
        [Reference(doc_id="rag", chunk_id="rag:0", text="RAG combines retrieval and generation.", score=1.0)],
    )
    assert "Question: What is RAG?" in prompt
    assert "[rag:0] RAG combines retrieval and generation." in prompt
