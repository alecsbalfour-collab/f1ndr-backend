from pydantic import BaseModel
from typing import List

class ScraperRequest(BaseModel):
    query: str
    platforms: List[str]
