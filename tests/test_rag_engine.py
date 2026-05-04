import pytest

from src.rag_engine import RAGEngine, format_context
from src.vector_store import SearchResult, VectorStore


def test_format_context_with_results():
    results = [
        SearchResult(text="Rent is due on the first day of each month.", score=0.91, index=0),
        SearchResult(text="Late fees apply after the fifth day.", score=0.87, index=1),
    ]

    context = format_context(results)

    assert "Source 1" in context
    assert "0.9100" in context
    assert "Rent is due" in context
    assert "Source 2" in context
    assert "Late fees apply" in context


def test_format_context_with_no_results():
    context = format_context([])

    assert context == "No relevant context found."


def test_rag_engine_answers_question_with_context():
    chunks = [
        "Rent is due on the first day of each month.",
        "Pets are not allowed unless approved in writing by the landlord.",
        "The security deposit is returned within 45 days after move-out.",
    ]

    store = VectorStore()
    store.build_index(chunks)

    engine = RAGEngine(store)
    response = engine.answer_question("When is rent due?", top_k=2)

    assert response["question"] == "When is rent due?"
    assert "answer" in response
    assert "context" in response
    assert "sources" in response
    assert len(response["sources"]) == 2
    assert "Source 1" in response["context"]


def test_rag_engine_rejects_empty_question():
    chunks = ["Rent is due on the first day of each month."]

    store = VectorStore()
    store.build_index(chunks)

    engine = RAGEngine(store)

    with pytest.raises(ValueError):
        engine.answer_question("")