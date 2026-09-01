from pydantic import BaseModel
from typing import Optional, List

class SearchRequest(BaseModel):
    query: str
    platforms: Optional[List[str]] = None
    filters: Optional[dict] = None
