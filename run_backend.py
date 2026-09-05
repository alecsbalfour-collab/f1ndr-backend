
import os
import sys

# Forces Python to recognize the current directory as the base module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import os
import uvicorn
from fastapi import FastAPI

# Import your backend modules
from f1ndr_backend.api.config.cors_config import apply_cors
from f1ndr_backend.api.config.logging_config import setup_logging
from f1ndr_backend.api.config.settings_config import get_settings
from f1ndr_backend.api.app_lifecycles import register_lifecycle_events

def create_app() -> FastAPI:
    settings = get_settings()
    setup_logging(settings)

    app = FastAPI(title="F1NDR Backend API")

    apply_cors(app, settings)
    register_lifecycle_events(app)

    return app

if __name__ == "__main__":
    app = create_app()

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        log_level="info"
    )
