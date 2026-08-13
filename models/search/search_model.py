from pydantic import BaseModel
from typing import Optional

class SearchRequest(BaseModel):
    query: Optional[str] = None
