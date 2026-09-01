from pydantic import BaseModel
from typing import List, Optional

class SearchRequest(BaseModel):
    query: str
    platforms: Optional[List[str]] = None
