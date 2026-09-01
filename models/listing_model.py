from pydantic import BaseModel
from typing import Optional

class Listing(BaseModel):
    id: str
    title: str
    price: float
    platform: str
    url: str
    location: Optional[str] = None
