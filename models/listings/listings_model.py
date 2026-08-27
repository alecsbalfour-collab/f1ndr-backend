from pydantic import BaseModel
from typing import List, Optional

class Listing(BaseModel):
    title: str
    price: float
    platform: str
    url: str
    posted: str
    location: str
    condition: str
    distance_km: Optional[float] = None
    deal_score: int

class ListingsResponse(BaseModel):
    count: int
    results: List[Listing]
