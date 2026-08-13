from pydantic import BaseModel
from typing import List, Dict, Any

class ListingsRequest(BaseModel):
    items: List[Dict[str, Any]]
