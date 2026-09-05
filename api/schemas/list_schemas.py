from pydantic import BaseModel
from typing import Optional

class Listing(BaseModel):
    id: str
    title: str
    price: float
    description: Optional[str] = None
    dealer_id: Optional[str] = None

class ListingSearchRequest(BaseModel):
    query: str

class ListingSearchResponse(BaseModel):
    results: list[Listing]
