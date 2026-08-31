from fastapi import APIRouter
from api.models.listing_create import ListingCreate
from services.f1ndr.f1ndr_service import F1ndrService

router = APIRouter()

@router.post("/create")
async def create_listing(data: ListingCreate):
    return F1ndrService().create_listing(data)

@router.post("/push")
async def push_listing(data: ListingCreate):
    return F1ndrService().push_listing(data)
