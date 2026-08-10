from fastapi import APIRouter
from services.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/search")
def search(payload: dict):
    """
    Search route for Findr.
    Accepts JSON payload: { "query": "text" }
    """
    return service.search(payload)
