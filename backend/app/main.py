from fastapi import FastAPI
from app.core.config import settings 
from app.api.v1.api import api_router
from app.core.logger import logger

app = FastAPI(title=settings.APP_NAME)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting QuickLook Backend...")

@app.get("/")
def health_check():
    logger.debug("Health check endpoint called")
    return {"status": "ok", "app": "QuickLook Backend"}