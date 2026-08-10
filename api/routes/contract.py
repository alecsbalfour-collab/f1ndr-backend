from fastapi import APIRouter
from services.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/contract")
def contract(payload: dict):
    """
    Contract route for Findr.
    Accepts JSON payload: { "text": "..." }
    """
    return service.contract(payload)
