from fastapi import APIRouter
from routes.controllers.list_controller import list_controller
from schemas.list_schemas import ListingSearchRequest, ListingSearchResponse

router = APIRouter(prefix="/list", tags=["listings"])

@router.post("/search", response_model=ListingSearchResponse)
def search_listings(payload: ListingSearchRequest):
    return list_controller.search(payload.query)
