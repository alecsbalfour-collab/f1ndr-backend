from pydantic import BaseModel
from typing import Optional

class SellItem(BaseModel):
    id: str
    title: str
    price: float
    condition: Optional[str] = None
    description: Optional[str] = None

class SellRequest(BaseModel):
    title: str
    price: float
    condition: Optional[str] = None
    description: Optional[str] = None

class SellResponse(BaseModel):
    item: SellItem
