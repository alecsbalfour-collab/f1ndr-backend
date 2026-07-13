from fastapi import APIRouter
from db.mongo import get_listings_collection

router = APIRouter()


@router.get("/")
def get_listings(limit: int = 50):
    col = get_listings_collection()
    docs = list(col.find().sort("created_at", -1).limit(limit))
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs


@router.get("/{listing_id}")
def get_listing(listing_id: str):
    col = get_listings_collection()
    doc = col.find_one({"_id": listing_id})
    if not doc:
        return {"error": "Listing not found"}
    doc["_id"] = str(doc["_id"])
    return doc
