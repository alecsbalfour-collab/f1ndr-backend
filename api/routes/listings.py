from fastapi import APIRouter
from models.listings.listings_model import ListingsRequest
from services.listings.listings_service import ListingsService

router = APIRouter(
    prefix="/listings",
    tags=["listings"]
)

service = ListingsService()

@router.post("/process")
async def process_listings(payload: ListingsRequest):
    """
    Enterprise listings endpoint.
    Accepts a ListingsRequest model,
    passes it to the ListingsService,
    which delegates to ListingsEngine.
    """
    return service.process(payload)
