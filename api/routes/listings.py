from fastapi import APIRouter
from api.models.listing_create import ListingCreate
from api.models.listing_create_response import ListingCreateResponse
from api.models.listing_push_response import ListingPushResponse
from services.f1ndr.f1ndr_service import F1ndrService

router = APIRouter()

@router.post("/create", response_model=ListingCreateResponse)
async def create_listing(data: ListingCreate):
    result = F1ndrService().create_listing(data)
    return ListingCreateResponse(status=result["status"], listing_id=result.get("id"))

@router.post("/push", response_model=ListingPushResponse)
async def push_listing(data: ListingCreate):
    result = F1ndrService().push_listing(data)
    return ListingPushResponse(status=result["status"], platforms=result["platforms"])
