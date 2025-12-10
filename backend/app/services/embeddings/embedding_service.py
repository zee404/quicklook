from abc import ABC, abstractmethod
from langchain_core.embeddings import Embeddings

class EmbeddingService(ABC):
    @abstractmethod
    def get_embedding(self) -> Embeddings:
        pass