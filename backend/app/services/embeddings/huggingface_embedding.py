from app.services.embeddings.embedding_service import EmbeddingService
from langchain_huggingface import HuggingFaceEmbeddings

class HuggingFaceEmbeddingService(EmbeddingService):
    def get_embedding(self):
        return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")