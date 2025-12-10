# QuickLook

QuickLook is a lightweight Retrieval-Augmented Generation (RAG) internal assistant prototype built with a FastAPI backend, an nginx-served frontend, and a Chroma vector database.

The project is intentionally designed to be modular and extensible so that LLM providers, embedding providers, and vector stores can be swapped with minimal changes.

## Architecture

Frontend (Browser)
→ nginx (serves UI + proxies /api)
→ FastAPI backend (RAG logic)
→ Vector store (Chroma)
→ LLM provider (Gemini by default)

## Backend

- Framework: FastAPI
- Entry point: backend/app/main.py
- API routing: backend/app/api/v1/api
- Chat endpoint: backend/app/api/v1/proxy/chat.py
- Core RAG flow handled by a dedicated RAG service

## Services Design

All external dependencies are abstracted:

- LLM Service  
  Interface-based design allowing different LLMs.  
  Default implementation uses Google Gemini.

- Embedding Services  
  Factory-based selection.  
  Default: local HuggingFace embeddings.

- Vector Store  
  Factory-based vector store abstraction.  
  Default: Chroma via HTTP client.

- RAG Service  
  Coordinates vector search + LLM response generation.

## Frontend

- Served using nginx
- Static HTML/JS stored in frontend/src
- nginx proxies all `/api/*` requests to the backend container
- Frontend communicates with backend using relative paths

Frontend URL:
http://localhost:3000

## Environment Configuration

Create a `.env` file inside the `backend/` directory.

Minimum required variables:
see .env.example

## Running Locally with Docker

Build and start everything:

docker compose up --build

This starts:
- Backend (FastAPI)
- Frontend (nginx)
- Vector database (Chroma)

## Access Points

Frontend:
http://localhost:3000

Backend:
http://localhost:8000

API Endpoint:
POST /api/v1/chat/query

This starts:
- Backend (FastAPI)
- Frontend (nginx)
- Vector database (Chroma)

## Access Points

Frontend:
http://localhost:3000

Backend:
http://localhost:8000

API Endpoint:
POST /api/v1/chat/query


## Data Ingestion

Documents are:
- Loaded
- Split into chunks
- Embedded using the configured embedding provider
- Stored in the vector database

The ingestion pipeline is decoupled from querying and generation, making future changes easy.

## Development Notes

- All providers (LLM, embeddings, vector DB) are accessed through interfaces and factories.
- Swapping implementations does not require changing business logic.
- Chroma data is persisted via Docker volumes.
- Backend code is mounted as a volume for fast iteration in development.

## Troubleshooting

- If frontend loads but API fails, check nginx proxy configuration.
- If vector search fails, verify the Chroma container is running.
- If LLM calls fail, ensure `LLM_API_KEY` is set correctly.


