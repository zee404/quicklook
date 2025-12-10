# QuickLook

QuickLook is a small RAG-style internal assistant prototype built with a FastAPI backend, a simple nginx-served frontend, and a Chroma vector database.

The project is intentionally structured to be modular and extensible, allowing different LLMs, embedding providers, and vector stores to be plugged in with minimal changes.

---

## Quick Overview

- **Backend**: FastAPI application exposing a chat endpoint backed by a RAG pipeline
  - Main app: [`backend/app/main.py`](backend/app/main.py)
  - API router: [`backend/app/api/v1/api`](backend/app/api/v1/api)
  - Chat proxy: [`backend/app/api/v1/proxy/chat.py`](backend/app/api/v1/proxy/chat.py)

- **Services (Abstracted)**:
  - **Vector store**: Factory-based vector store service (Chroma by default)
  - **Embeddings**: Pluggable embedding providers (HuggingFace local by default)
  - **LLM / Agent**: Pluggable LLM service (Google Gemini by default)
  - **RAG Orchestration**: Central service coordinating retrieval + generation

- **Schemas**:
  - [`ChatQuery`](backend/app/schemas/rag_Schemas.py)
  - [`ChatResponse`](backend/app/schemas/rag_Schemas.py)

- **Configuration**:
  - [`Settings`](backend/app/core/config.py) (loaded from `.env`)

---

## Files of Interest

- [docker-compose.yaml](docker-compose.yaml) — orchestrates backend, frontend, and vector DB
- Backend:
  - [backend/Dockerfile](backend/Dockerfile)
  - [backend/app/main.py](backend/app/main.py)
  - [backend/app/api/v1/api](backend/app/api/v1/api)
  - [backend/app/api/v1/proxy/chat.py](backend/app/api/v1/proxy/chat.py)
  - [backend/app/services/llm](backend/app/services/llm)
  - [backend/app/services/embeddings](backend/app/services/embeddings)
  - [backend/app/services/vector](backend/app/services/vector)
  - [backend/app/services/rag_service.py](backend/app/services/rag_service.py)
- Frontend:
  - [frontend/Dockerfile](frontend/Dockerfile)
  - [frontend/nginx.conf](frontend/nginx.conf)

---

## Environment

Create a `.env` file in `backend/`.

Minimum required variables:

```env
LLM_API_KEY=your_google_api_key

EMBEDDING_PROVIDER=huggingface
VECTOR_COLLECTION=quicklook_knowledge
VECTOR_DB=vector_db
