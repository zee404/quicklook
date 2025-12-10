from fastapi import FastAPI
from app.core.config import settings 
from app.api.v1.api import api_router

# 2. Use lowercase 'settings' (the object)
app = FastAPI(title=settings.APP_NAME)

# 3. FIX TYPO: It is include_router (with an 'r'), not include_route
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def health_check():
    test="zze"
    return {"status": "ok", "app": "QuickLook Backend"}