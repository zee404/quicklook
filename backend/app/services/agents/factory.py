from app.services.agents.gemini_service import GeminiService
def get_agent(Provider: str):
    if Provider == "gemini":
        return GeminiService()
    else:
        raise ValueError(f"Unsupported provider: {Provider}")