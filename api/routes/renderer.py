from fastapi import APIRouter
from services.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/render")
def render(payload: dict):
    """
    Render route for Findr.
    Accepts JSON payload: { "data": ... }
    """
    return service.render(payload)
