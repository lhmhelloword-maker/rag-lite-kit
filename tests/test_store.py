from rag_lite_kit.store import InMemoryVectorStore, VectorRecord


def test_in_memory_store_returns_best_match_first():
    store = InMemoryVectorStore()
    store.add(
        [
            VectorRecord("a:0", "a", "retrieval pipelines", [1.0, 0.0], {}),
            VectorRecord("b:0", "b", "frontend ui", [0.0, 1.0], {}),
        ]
    )
    results = store.query([1.0, 0.0], top_k=1)
    assert results[0].doc_id == "a"
