from fastapi import APIRouter
from models.search_request import SearchRequest
from services.f1ndr.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/search")
def search(request: SearchRequest):
    return service.search(request.query, request.platforms)

@router.post("/listings")
def create_listing(data: dict):
    return service.create_listing(data)

@router.get("/listings")
def get_listings():
    return service.get_listings()

@router.delete("/listings")
def clear_listings():
    return service.clear_listings()
