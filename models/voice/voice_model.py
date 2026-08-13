from pydantic import BaseModel
from typing import Optional, Dict, Any

class VoiceRequest(BaseModel):
    text: Optional[str] = None
    settings: Optional[Dict[str, Any]] = None
