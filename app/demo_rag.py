from __future__ import annotations

from pathlib import Path

from src.chunking import chunk_text
from src.document_loader import load_pdf_text
from src.rag_engine import RAGEngine
from src.vector_store import VectorStore


def run_demo(pdf_path: str, question: str) -> dict:
    """
    Run the full RAG pipeline on a PDF document.

    Steps:
    1. Load text from PDF
    2. Split text into chunks
    3. Build vector search index
    4. Retrieve context and answer the question
    """
    text = load_pdf_text(pdf_path)
    chunks = chunk_text(text)

    store = VectorStore()
    store.build_index(chunks)

    engine = RAGEngine(store)
    return engine.answer_question(question)


if __name__ == "__main__":
    sample_pdf = Path("data/sample_lease.pdf")

    if not sample_pdf.exists():
        raise FileNotFoundError(
            "Missing data/sample_lease.pdf. Add a sample PDF lease or rental document first."
        )

    question = "What does this document say about pets?"
    response = run_demo(str(sample_pdf), question)

    print("\nQUESTION:")
    print(response["question"])

    print("\nANSWER:")
    print(response["answer"])

    print("\nRETRIEVED CONTEXT:")
    print(response["context"])