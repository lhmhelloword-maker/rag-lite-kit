from rag_lite_kit.splitter import split_text


def test_split_text_basic():
    text = "a" * 1000
    chunks = split_text(text, chunk_size=200, overlap=50)
    assert len(chunks) > 1
    assert all(len(c) <= 200 for c in chunks)


def test_split_text_empty():
    assert split_text("   ") == []
