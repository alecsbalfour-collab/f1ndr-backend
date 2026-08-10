from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="API Layer",
    version="1.0.0",
    description="Internal API layer for f1ndr + watchr + trinn engines"
)

app.include_router(router)
