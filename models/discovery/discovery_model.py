from pydantic import BaseModel
from typing import Optional, Dict, Any

class DiscoveryRequest(BaseModel):
    query: Optional[str] = None
    options: Optional[Dict[str, Any]] = None
