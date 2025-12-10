from app.services.vector.vector_store_service import VectorStoreService
from app.core.config import settings
from app.services.embeddings.factory import get_embedding_service
from chromadb import HttpClient
from langchain_community.vectorstores import Chroma

class ChromaVectorService(VectorStoreService):
    
    def __init__(self):
        embeddings_service = get_embedding_service(settings.EMBEDDING_PROVIDER)
        embeddings = embeddings_service.get_embedding()

        self.client = HttpClient(host=settings.VECTOR_DB_HOST, port=settings.VECTOR_DB_HOST_PORT)
        
        self.vector_db = Chroma(
            client=self.client,
            collection_name=settings.VECTOR_COLLECTION,
            embedding_function=embeddings,
        )
    def add_documents(self, docs):
        self.vector_db.add_documents(docs)

    def search_similar(self, query: str, k: int = 3):
        print(f"Searching for top {k} similar documents to the query: '{query}'")
        try:
            docs = self.vector_db.similarity_search(query, k=k)
            return docs
        except Exception as e:
            print(f"Error searching vector DB: {e}")
            return []