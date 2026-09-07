# f1ndr_backend/api/app_lifecycles.py

from fastapi import FastAPI
from f1ndr_backend.api.startup import on_startup
from f1ndr_backend.api.shutdown import on_shutdown

def register_lifecycle_events(app: FastAPI):
    """
    Registers startup and shutdown lifecycle events for the FastAPI app.
    """

    @app.on_event("startup")
    async def startup_event():
        await on_startup()

    @app.on_event("shutdown")
    async def shutdown_event():
        await on_shutdown()
