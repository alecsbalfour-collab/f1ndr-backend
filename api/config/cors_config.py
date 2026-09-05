from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def apply_cors(app: FastAPI) -> None:
    """
    Apply CORS configuration to the FastAPI app.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Adjust later if needed
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
