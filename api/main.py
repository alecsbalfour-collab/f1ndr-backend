from fastapi import FastAPI

# Config imports
from f1ndr_backend.api.config.cors_config import apply_cors
from f1ndr_backend.api.config.logging_config import setup_logging
from f1ndr_backend.api.config.settings_config import get_settings

# Lifecycle events
from f1ndr_backend.api.app_lifecycles import register_lifecycle_events

# Router imports (add yours here)
# from f1ndr_backend.api.routes.example_routes import router as example_router


def create_app() -> FastAPI:
    """
    Core application factory for the f1ndr backend.
    This replaces the original api/main.py file exactly as it was intended:
    - Load settings
    - Configure logging
    - Apply CORS
    - Register lifecycle events
    - Mount routers
    """
    settings = get_settings()
    setup_logging(settings)

    app = FastAPI(title="f1ndr Backend API")

    # Apply CORS
    apply_cors(app, settings)

    # Register startup/shutdown events
    register_lifecycle_events(app)

    # Include routers
    # app.include_router(example_router)

    return app


# Uvicorn entrypoint (only used if someone runs this file directly)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "f1ndr_backend.api.main:create_app",
        host="0.0.0.0",
        port=8000,
        factory=True
    )
