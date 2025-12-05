from fastapi import APIRouter
from app.schemas.rag_schemas import ChatQuery, ChatResponse
from app.services.rag_service import RagService

router = APIRouter()

@router.post("/query", response_model=ChatResponse)
async def query_knowledge_base(chat_query: ChatQuery):
    service = RagService()
    
    answer = service.process_query(
        user_question=chat_query.user_question
    )
    
    return ChatResponse(answer=answer, sources=[])