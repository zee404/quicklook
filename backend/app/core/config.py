from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # 1. Define the fields matching your .env file
    APP_NAME: str = "QuickLook"
    LLM_API_KEY: str
    VECTOR_DB_HOST: str = "vector_db"
    VECTOR_DB_HOST_PORT: int = 8000
    VECTOR_COLLECTION: str = "quicklook_knowledge"
    LLM_PROVIDER: str
    EMBEDDING_PROVIDER:str = "huggingface"
    VECTOR_STORE_PROVIDER: str = "chroma"
    class Config:
        env_file = ".env"
        # Allows extra fields in .env (like comments or unused vars) without crashing
        extra = "ignore" 

settings = Settings()