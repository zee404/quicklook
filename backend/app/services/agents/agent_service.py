from abc import ABC ,abstractmethod

class AgentService(ABC):
    @abstractmethod
    def generate_response(self,context_text, question: str) -> str:
        pass