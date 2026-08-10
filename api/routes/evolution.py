from fastapi import APIRouter
from services.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/evolution")
def evolution(payload: dict):
    """
    Evolution route for Findr.
    Accepts JSON payload: { "data": ... }
    """
    data = payload.get("data")
    if not data:
        return {"error": "Missing 'data' field"}

    return {
        "action": "evolution",
        "input": data,
        "status": "evolved"
    }
