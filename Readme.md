# QuickLook

QuickLook is a small RAG-style internal assistant prototype with a FastAPI backend, a simple frontend served by nginx, and a Chroma vector DB for embeddings.

## Quick overview
- Backend: FastAPI application serving a single RAG-related endpoint.
  - Main app: [`app`](backend/app/main.py)
  - API router: [backend/app/api/v1/api](backend/app/api/v1/api) which mounts the chat proxy [backend/app/api/v1/proxy/chat.py](/backend/app/api/v1/proxy/chat.py)
- Services:
  - Embeddings & vector store: [`VectorService`](backend/app/services/vector_service.py)
  - LLM proxy (Google Gemini): [`GeminiService`](backend/app/services/gemini_service.py)
  - RAG orchestration (stub): [`RagService.ask_question`](backend/app/services/rag_service.py)
- Schemas: [`ChatQuery`](backend/app/schemas/rag_Schemas.py), [`ChatResponse`](backend/app/schemas/rag_Schemas.py)
- Configuration: [`Settings`](backend/app/core/config.py) (reads values from `.env`)

## Files of interest
- [docker-compose.yaml](docker-compose.yaml) — orchestrates backend, frontend, and chroma DB
- [backend/Dockerfile](backend/Dockerfile) — backend image
- [frontend/Dockerfile](frontend/Dockerfile) — frontend image
- [frontend/nginx.conf](frontend/nginx.conf) — nginx config used in the frontend container
- Backend code:
  - [backend/app/main.py](backend/app/main.py) (`app`)
  - [backend/app/api/v1/api](backend/app/api/v1/api)
  - [backend/app/api/v1/proxy/chat.py](backend/app/api/v1/proxy/chat.py)
  - [backend/app/services/vector_service.py](backend/app/services/vector_service.py) (`VectorService`)
  - [backend/app/services/gemini_service.py](backend/app/services/gemini_service.py) (`GeminiService`)
  - [backend/app/services/rag_service.py](backend/app/services/rag_service.py) (`RagService.ask_question`)
  - [backend/app/schemas/rag_Schemas.py](backend/app/schemas/rag_Schemas.py) (`ChatQuery`, `ChatResponse`)
  - [backend/app/core/config.py](backend/app/core/config.py) (`Settings`, `setting`)

## Environment
Create a `.env` file in `backend/` (referenced by [`Settings`](backend/app/core/config.py)). Minimum required env var:
- `GOOGLE_API_KEY` — API key for Google generative models/embeddings.

The project uses Pipfile in `backend/` to manage Python dependencies.

## Running locally (recommended)
1. Start services with Docker Compose:
```sh
docker-compose up --build
```
This builds the backend and frontend images and starts a Chroma container (configured in [docker-compose.yaml](docker-compose.yaml)).

2. Backend API will be reachable at:
- http://localhost:8000/  — health check (`GET /`)
- Intended chat endpoint: `POST /api/v1/chat/query` (see [backend/app/api/v1/proxy/chat.py](backend/app/api/v1/proxy/chat.py))

3. Frontend will be served at:
- http://localhost:3000/ (nginx serves files from [`frontend/src`], configured via [frontend/nginx.conf](frontend/nginx.conf))

## API (example)
POST request to the chat endpoint (JSON body according to [`ChatQuery`](backend/app/schemas/rag_Schemas.py)):

Example curl:
```sh
curl -X POST "http://localhost:8000/api/v1/chat/query" \
  -H "Content-Type: application/json" \
  -d '{"user_question":"What is QuickLook?","chat_history": []}'
```
Response shape follows [`ChatResponse`](backend/app/schemas/rag_Schemas.py).

## Development notes
- Embeddings use [`VectorService`](backend/app/services/vector_service.py) backed by Chroma; configured to persist to `./data` via docker-compose.
- LLM access is implemented in [`GeminiService`](backend/app/services/gemini_service.py) using `langchain-google-genai`.
- RAG orchestration is currently a stub at [`RagService.ask_question`](backend/app/services/rag_service.py) — implement retrieval + generation there.
- Configuration is in [`Settings`](backend/app/core/config.py) and reads `.env`.

## Troubleshooting
- Ensure `GOOGLE_API_KEY` is set in `backend/.env`.
- Chroma runs in container `vector_db` (ports configured in [docker-compose.yaml](docker-compose.yaml)); if using an external Chroma, update [`VectorService`](backend/app/services/vector_service.py).
- Check container logs for failures:
```sh
docker-compose logs backend
docker-compose logs vector_db
```

## Next steps / TODO
- Implement retrieval and prompt orchestration in [`RagService.ask_question`](backend/app/services/rag_service.py).
- Add tests and CI.
- Harden production configuration (secrets, CORS, request validation).

License: Add a LICENSE file as needed.