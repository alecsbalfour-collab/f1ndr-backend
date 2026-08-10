from fastapi import APIRouter
from typing import Optional
from services.f1ndr.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.get("/search")
def search(
    keywords: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    lat: Optional[float] = None,
    lng: Optional[float] = None,
    radius_km: Optional[float] = None,
    sort: Optional[str] = None
):
    payload = {
        "query": {
            "keywords": keywords,
            "category": category,
            "min_price": min_price,
            "max_price": max_price,
            "lat": lat,
            "lng": lng,
            "radius_km": radius_km,
            "sort": sort
        }
    }

    return service.search(payload)
