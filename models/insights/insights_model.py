from pydantic import BaseModel
from typing import Optional, Dict, Any

class InsightsRequest(BaseModel):
    query: Optional[str] = None
    params: Optional[Dict[str, Any]] = None
