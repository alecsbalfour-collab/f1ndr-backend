from pydantic import BaseModel
from typing import Optional

class WatchItem(BaseModel):
    id: str
    title: str
    price: float
    dealer_id: Optional[str] = None

class WatchRequest(BaseModel):
    query: str

class WatchResponse(BaseModel):
    results: list[WatchItem]
