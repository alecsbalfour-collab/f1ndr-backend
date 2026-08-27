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
    # Replace this with your real scraper logic later
    return {
        "count": 1,
        "results": [
            {
                "title": "",
                "price": 0,
                "platform": "",
                "url": "",
                "posted": "",
                "location": "",
                "condition": "unknown",
                "distance_km": None,
                "deal_score": 75
            }
        ]
    }
