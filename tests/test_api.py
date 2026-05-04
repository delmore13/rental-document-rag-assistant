from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    data = response.json()

    assert data["message"] == "Rental Document RAG Assistant API is running."
    assert data["docs_url"] == "/docs"


def test_ask_endpoint_answers_question():
    pdf_path = Path("data/sample_lease.pdf")

    if not pdf_path.exists():
        # Keep the test useful even if the sample PDF has not been generated yet.
        from scripts.create_sample_pdf import create_sample_lease_pdf

        create_sample_lease_pdf()

    response = client.post(
        "/ask",
        json={"question": "What does this document say about pets?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["question"] == "What does this document say about pets?"
    assert "answer" in data
    assert "context" in data
    assert "sources" in data
    assert len(data["sources"]) > 0
    assert "Pets" in data["context"] or "pets" in data["context"]