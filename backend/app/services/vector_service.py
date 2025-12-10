from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import chromadb
from app.core.config import settings

class VectorService:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Connect to the remote container
        self.client = chromadb.HttpClient(host=settings.VECTOR_DB, port=8000)
        
        self.vector_db = Chroma(
            client=self.client,
            collection_name="quicklook_knowledge",
            embedding_function=self.embeddings,
        )

    def search_similar(self, query: str, k: int = 3):
        print(f"Searching for top {k} similar documents to the query: '{query}'")
        try:
            docs = self.vector_db.similarity_search(query, k=k)
            return docs
        except Exception as e:
            print(f"Error searching vector DB: {e}")
            return []
    