from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI()

# Include your routes
app.include_router(api_router)
