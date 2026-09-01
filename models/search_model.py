from pydantic import BaseModel
from typing import Optional, List, Dict

class SearchRequest(BaseModel):
    query: str
    platforms: Optional[List[str]] = None
    filters: Optional[Dict] = None
