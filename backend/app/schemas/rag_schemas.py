from pydantic import BaseModel

class ChatQuery(BaseModel):
    user_question: str
    chat_history: list[tuple[str, str]] = []

class ChatResponse(BaseModel):
    answer: str
    source_documents: list[dict] = []