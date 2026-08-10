from fastapi import APIRouter
from services.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/goals")
def goals(payload: dict):
    """
    Goals route for Findr.
    Accepts JSON payload: { "data": ... }
    """
    return {
        "action": "goals",
        "input": payload.get("data"),
        "status": "goal-processed"
    }
