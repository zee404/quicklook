from app.services.embeddings.huggingface_embedding import HuggingFaceEmbeddingService

def get_embedding_service(provider: str):
    if provider == "huggingface":
        return HuggingFaceEmbeddingService()
    else:
        raise ValueError(f"Unsupported embedding provider: {provider}")