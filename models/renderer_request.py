# models/renderer_request.py

from pydantic import BaseModel

class RendererRequest(BaseModel):
    scene: str
    detail: str | None = None
