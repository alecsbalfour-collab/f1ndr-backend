from pydantic import BaseModel
from typing import Optional

class Dealer(BaseModel):
    id: str
    name: str
    city: Optional[str] = None
    province: Optional[str] = None
    phone: Optional[str] = None

class DealerSearchRequest(BaseModel):
    query: str

class DealerSearchResponse(BaseModel):
    results: list[Dealer]
