# models/listing_document.py

from pydantic import BaseModel
from typing import Any, Dict

class ListingDocument(BaseModel):
    id: str
    title: str
    price: float
    url: str
    source: str
    metadata: Dict[str, Any] = {}
