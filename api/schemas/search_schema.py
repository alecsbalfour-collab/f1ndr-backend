from pydantic import BaseModel
from typing import List, Dict

class SearchRequest(BaseModel):
    query: str
    sources: List[str] = ["kijiji"]
    filters: Dict = {}
