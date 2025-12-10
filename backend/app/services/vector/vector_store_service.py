from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class VectorStoreService(ABC):
    @abstractmethod
    def add_documents(self, docs:List[Document])-> None:
        pass

    @abstractmethod
    def search_similar(self, query: str, k: int = 3):
        pass