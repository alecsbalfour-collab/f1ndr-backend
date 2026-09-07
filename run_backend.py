# run_backend.py

import os
from fastapi import FastAPI
import uvicorn

from f1ndr_backend.api.main import create_app

# IMPORTANT:
# Uvicorn needs a top-level variable named "app"
app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "run_backend:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        log_level="info"
    )
