from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.demo_rag import run_demo


app = FastAPI(
    title="Rental Document RAG Assistant",
    description="A RAG API for asking questions about rental and real estate documents.",
    version="1.0.0",
)


class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        example="What does this document say about pets?",
    )


class SourceResponse(BaseModel):
    text: str
    score: float
    index: int


class QuestionResponse(BaseModel):
    question: str
    answer: str
    context: str
    sources: list[SourceResponse]


@app.get("/")
def root() -> dict:
    return {
        "message": "Rental Document RAG Assistant API is running.",
        "docs_url": "/docs",
    }


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest) -> dict:
    pdf_path = Path("data/sample_lease.pdf")

    if not pdf_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Sample PDF not found. Run scripts/create_sample_pdf.py first.",
        )

    try:
        response = run_demo(str(pdf_path), request.question)
        return response
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc