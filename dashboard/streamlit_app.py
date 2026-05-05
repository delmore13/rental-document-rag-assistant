from __future__ import annotations

from pathlib import Path

import streamlit as st

from app.demo_rag import run_demo
from scripts.create_sample_pdf import create_sample_lease_pdf


st.set_page_config(
    page_title="Rental Document RAG Assistant",
    page_icon="🏠",
    layout="wide",
)

st.title("🏠 Rental Document RAG Assistant")
st.write(
    "Ask questions about a sample lease document and retrieve grounded context "
    "from the PDF using semantic search."
)

sample_pdf = Path("data/sample_lease.pdf")

if not sample_pdf.exists():
    create_sample_lease_pdf()

question = st.text_input(
    "Ask a question about the lease:",
    value="What does this document say about pets?",
)

if st.button("Ask Document"):
    if not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Searching the document..."):
            response = run_demo(str(sample_pdf), question)

        st.subheader("Answer")
        st.write(response["answer"])

        st.subheader("Retrieved Context")
        st.text_area(
            "Most relevant document sections:",
            value=response["context"],
            height=300,
        )

        st.subheader("Source Scores")
        for i, source in enumerate(response["sources"], start=1):
            st.write(f"Source {i}: score `{source.score:.4f}`")