from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.services.vector.factory import get_vector_store

class VectorService:
    def __init__(self):
        self.vector_store = get_vector_store()

    def search_similar(self, query: str, k: int = 3):
        print(f"Searching for top {k} similar documents to the query: '{query}'")
        try:
            docs = self.vector_store.search_similar(query, k=k)
            return docs
        except Exception as e:
            print(f"Error searching vector DB: {e}")
            return []
    