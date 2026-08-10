from fastapi import APIRouter
from services.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/dialogue")
def dialogue(payload: dict):
    """
    Dialogue route for Findr.
    Accepts JSON payload: { "data": ... }
    """
    return {
        "action": "dialogue",
        "input": payload.get("data"),
        "response": "generated-dialogue"
    }
