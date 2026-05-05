\# Real Estate / Rental Document RAG Assistant



A production-style Retrieval-Augmented Generation (RAG) assistant that allows users to ask questions about real estate and rental documents, such as leases, inspection notes, rental agreements, and property paperwork.



The system loads PDF documents, extracts text, splits the content into searchable chunks, stores those chunks in a FAISS vector database, retrieves the most relevant sections, and returns document-grounded answers with supporting context.



\---



\## Project Purpose



Real estate and rental documents are often long, dense, and difficult to quickly understand. This project demonstrates how machine learning, semantic search, and backend API design can be combined to help users ask natural-language questions and receive answers based on the actual document content.



Example questions:



```text

What does the lease say about pets?

Who is responsible for repairs?

When is rent due?

What are the tenant responsibilities?

```



\---



\## Features



\- PDF document loading and text extraction

\- Text chunking for long document processing

\- Semantic search using FAISS vector storage

\- Sentence-transformer embeddings for document retrieval

\- RAG answer engine with supporting context

\- Runnable demo pipeline

\- FastAPI `/ask` endpoint for backend question answering

\- Streamlit dashboard for interactive document Q\&A

\- Automated Pytest test suite

\- Clean project structure suitable for portfolio and production-style expansion



\---



\## Tech Stack



\- Python

\- FastAPI

\- Streamlit

\- FAISS

\- Sentence Transformers

\- Pydantic

\- Pytest



\---



\## Project Structure



```text

rental-document-rag-assistant/

├── app/

│   ├── \_\_init\_\_.py

│   └── main.py

├── dashboard/

│   └── streamlit\_app.py

├── data/

├── scripts/

│   └── \_\_init\_\_.py

├── tests/

├── README.md

└── requirements.txt

```



\---



\## Run the Streamlit Dashboard



Start the interactive dashboard:



```bash

python -m streamlit run dashboard/streamlit\_app.py --server.fileWatcherType none

```



Then open:



```text

http://localhost:8501

```



The dashboard allows users to type a document question and receive an answer with supporting context.



\---



\## Run the FastAPI App



Start the FastAPI backend:



```bash

python -m uvicorn app.main:app --reload

```



Then open the interactive API docs:



```text

http://127.0.0.1:8000/docs

```



Example request body:



```json

{

&#x20; "question": "What does the lease say about pets?"

}

```



\---



\## Run Tests



Run the full test suite:



```bash

python -m pytest

```



Current test result:



```text

16 passed

```



\---



\## Example Use Case



A user uploads or processes a rental/real estate document and asks:



```text

What does the lease say about pets?

```



The system retrieves the most relevant document chunks and returns an answer grounded in the document text.



\---



\## Portfolio Highlights



This project demonstrates:



\- End-to-end machine learning application design

\- Semantic search and vector database usage

\- RAG pipeline architecture

\- API development with FastAPI

\- Interactive dashboard development with Streamlit

\- Automated testing with Pytest

\- Clean Git/GitHub workflow

\- Production-style project organization



\---



\## Future Improvements



Potential future upgrades include:



\- Multi-document upload support

\- User authentication

\- Better source citations by page number

\- Docker deployment

\- Cloud deployment

\- UI file uploader

\- Chat history

\- Model evaluation metrics for answer quality

