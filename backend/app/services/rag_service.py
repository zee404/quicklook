from app.services.vector_service import VectorService
from app.services.agents.factory import get_agent
from app.core.config import settings

class RagService:
    def __init__(self):
        # Initialize the helper services
        self.vector_service = VectorService()
        self.agent = get_agent(settings.LLM_PROVIDER)

    def process_query(self, user_question: str) -> str:
        # Step 1: Search the Memory (Vector DB)
        # We ask for the top 3 relevant chunks
        print(f"Processing user question: {user_question}")
        relevant_docs = self.vector_service.search_similar(user_question, k=10)
        
        if not relevant_docs:
            return "I couldn't find any relevant documents to answer your question."

        # Step 2: Combine the found text into one big string
        # Each 'doc' has page_content
        context_text = "\n\n".join([doc.page_content for doc in relevant_docs])

        # Step 3: Send to the Brain (Gemini)
        answer = self.agent.generate_response(context_text, user_question)

        return answer