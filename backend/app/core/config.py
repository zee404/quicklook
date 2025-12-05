import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # 1. Define the fields matching your .env file
    APP_NAME: str = "QuickLook"
    GOOGLE_API_KEY: str
    CHROMA_HOST: str = "vector_db"

    class Config:
        env_file = ".env"
        # Allows extra fields in .env (like comments or unused vars) without crashing
        extra = "ignore" 

# CRITICAL FIX: Instantiate the class so other files can import 'settings'
settings = Settings()