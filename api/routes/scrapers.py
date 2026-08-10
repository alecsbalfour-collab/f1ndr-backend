from fastapi import APIRouter
from services.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/scrape")
def scrape(payload: dict):
    """
    Scrape route for Findr.
    Accepts JSON payload: { "target": "URL or text" }
    """
    return service.scrape(payload)
