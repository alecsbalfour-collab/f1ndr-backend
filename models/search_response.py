# models/search_response.py

from pydantic import BaseModel
from typing import Any, Dict, List

class SearchResponse(BaseModel):
    results: List[Dict[str, Any]]
    best_deal: Dict[str, Any] | None = None
