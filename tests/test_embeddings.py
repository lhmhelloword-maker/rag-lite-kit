from rag_lite_kit.embeddings import HashEmbeddingBackend


def test_hash_embeddings_are_deterministic():
    backend = HashEmbeddingBackend(dimensions=16)
    left = backend.embed_query("retrieval augmented generation")
    right = backend.embed_query("retrieval augmented generation")
    assert left == right
    assert len(left) == 16
