from app.services.vector.chroma_servie import ChromaVectorService
from app.core.config import settings

def get_vector_store():
    provider = settings.VECTOR_STORE_PROVIDER

    if provider == "chroma":
        return ChromaVectorService()

    raise ValueError(f"Unsupported vector store: {provider}")