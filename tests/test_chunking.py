import pytest

from src.chunking import chunk_text


def test_chunk_text_returns_chunks():
    text = "A" * 2000

    chunks = chunk_text(text, chunk_size=500, overlap=100)

    assert len(chunks) > 1
    assert all(len(chunk) <= 500 for chunk in chunks)


def test_chunk_text_rejects_empty_text():
    with pytest.raises(ValueError, match="Text cannot be empty"):
        chunk_text("")


def test_chunk_text_rejects_invalid_overlap():
    with pytest.raises(ValueError, match="overlap must be smaller"):
        chunk_text("Some text", chunk_size=100, overlap=100)