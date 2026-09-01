from fastapi import FastAPI
from api.routes.f1ndr_routes import router as f1ndr_router

app = FastAPI()

app.include_router(f1ndr_router)
