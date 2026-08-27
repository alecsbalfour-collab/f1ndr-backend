from fastapi import FastAPI
from models.listings_model import ListingsResponse

app = FastAPI()

@app.post("/listings", response_model=ListingsResponse)
async def listings():
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
