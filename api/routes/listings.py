from fastapi import APIRouter, HTTPException
from services.listings.listings_service import ListingsService
from models.listings.listings_model import ListingsRequest

router = APIRouter()
service = ListingsService()

@router.post("/listings")
def listings(payload: ListingsRequest):
    try:
        return service.process(payload.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
