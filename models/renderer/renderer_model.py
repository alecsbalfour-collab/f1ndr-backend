from pydantic import BaseModel
from typing import Optional, Dict, Any

class RendererRequest(BaseModel):
    content: Optional[str] = None
    options: Optional[Dict[str, Any]] = None
