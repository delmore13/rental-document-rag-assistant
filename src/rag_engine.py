from __future__ import annotations

from typing import List

from src.vector_store import SearchResult, VectorStore


def format_context(results: List[SearchResult]) -> str:
    """
    Format retrieved search results into readable context for an answer engine.
    """
    if not results:
        return "No relevant context found."

    context_blocks = []

    for i, result in enumerate(results, start=1):
        context_blocks.append(
            f"[Source {i} | Score: {result.score:.4f}]\n{result.text}"
        )

    return "\n\n".join(context_blocks)


class RAGEngine:
    """
    Retrieval-Augmented Generation engine.

    For now, this engine retrieves the most relevant document chunks and returns
    a grounded answer template. Later, we can connect this to an LLM.
    """

    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def answer_question(self, question: str, top_k: int = 3) -> dict:
        if not question.strip():
            raise ValueError("Question cannot be empty.")

        results = self.vector_store.search(question, top_k=top_k)
        context = format_context(results)

        answer = (
            "Based on the retrieved document context, here are the most relevant "
            "sections found for your question. Review the source context below "
            "before making a decision."
        )

        return {
            "question": question,
            "answer": answer,
            "context": context,
            "sources": results,
        }