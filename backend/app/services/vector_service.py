from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.config import settings

class VectorService:
    def __init__(self):
        # We initialize the connection to ChromaDB here
        # This setup assumes Chroma is running in a Docker container
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001", 
            google_api_key=settings.GOOGLE_API_KEY
        )
        
        self.vector_db = Chroma(
            collection_name="quicklook_knowledge",
            embedding_function=self.embeddings,
            client_settings=None, # In production, you'd set host/port here
            persist_directory="./chroma_data" # Or connect to http server
        )

    def search_similar(self, query: str, k: int = 3):
        """
        Searches the database for the top 'k' chunks relevant to the query.
        """
        try:
            # Returns a list of Document objects
            docs = self.vector_db.similarity_search(query, k=k)
            return docs
        except Exception as e:
            print(f"Error searching vector DB: {e}")
            return []

    def add_documents(self, documents):
        """
        Adds processed text chunks to the database.
        """
        self.vector_db.add_documents(documents)