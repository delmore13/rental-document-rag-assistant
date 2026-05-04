from __future__ import annotations

from dataclasses import dataclass
from typing import List

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


@dataclass
class SearchResult:
    text: str
    score: float
    index: int


class VectorStore:
    """
    FAISS-based vector store for document chunks.

    Converts text chunks into embeddings, stores them in FAISS,
    and retrieves the most relevant chunks for a user question.
    """

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.chunks: List[str] = []

    def _embed_texts(self, texts: List[str]) -> np.ndarray:
        if not texts:
            raise ValueError("Cannot embed an empty list of texts.")

        embeddings = self.model.encode(texts, convert_to_numpy=True)
        embeddings = np.array(embeddings).astype("float32")

        # Normalize so inner product behaves like cosine similarity.
        faiss.normalize_L2(embeddings)

        return embeddings

    def build_index(self, chunks: List[str]) -> None:
        if not chunks:
            raise ValueError("Cannot build index with no chunks.")

        self.chunks = chunks
        embeddings = self._embed_texts(chunks)

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)

    def search(self, query: str, top_k: int = 3) -> List[SearchResult]:
        if self.index is None:
            raise ValueError("Index has not been built yet. Call build_index() first.")

        if not query.strip():
            raise ValueError("Query cannot be empty.")

        query_embedding = self._embed_texts([query])
        scores, indices = self.index.search(query_embedding, top_k)

        results: List[SearchResult] = []

        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue

            results.append(
                SearchResult(
                    text=self.chunks[idx],
                    score=float(score),
                    index=int(idx),
                )
            )

        return results