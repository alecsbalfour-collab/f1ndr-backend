from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# -----------------------------
# MODELS
# -----------------------------
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

# -----------------------------
# ENDPOINTS
# -----------------------------
@app.post("/listings", response_model=ListingsResponse)
async def listings():
    return ListingsResponse(
        count=1,
        results=[
            Listing(
                title="Test Item",
                price=100,
                platform="Kijiji",
                url="https://example.com",
                posted="today",
                location="Calgary",
                condition="good",
                deal_score=90
            )
        ]
    )
