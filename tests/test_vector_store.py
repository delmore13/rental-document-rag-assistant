import pytest

from src.vector_store import SearchResult, VectorStore


def test_vector_store_builds_index_and_searches():
    chunks = [
        "The tenant is responsible for paying rent on the first day of each month.",
        "Pets are not allowed unless approved in writing by the landlord.",
        "The security deposit will be returned within 45 days after move-out.",
    ]

    store = VectorStore()
    store.build_index(chunks)

    results = store.search("Are pets allowed?", top_k=2)

    assert len(results) == 2
    assert all(isinstance(result, SearchResult) for result in results)
    assert any("Pets" in result.text or "pets" in result.text for result in results)


def test_vector_store_rejects_empty_chunks():
    store = VectorStore()

    with pytest.raises(ValueError):
        store.build_index([])


def test_vector_store_rejects_search_before_index():
    store = VectorStore()

    with pytest.raises(ValueError):
        store.search("What does the lease say about rent?")


def test_vector_store_rejects_empty_query():
    chunks = ["Rent is due on the first day of each month."]

    store = VectorStore()
    store.build_index(chunks)

    with pytest.raises(ValueError):
        store.search("")