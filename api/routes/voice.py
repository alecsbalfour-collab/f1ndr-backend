from fastapi import APIRouter
from services.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/voice")
def voice(payload: dict):
    """
    Global Voice route.
    Accepts JSON payload: { "text": ... }
    """
    text = payload.get("text")
    if not text:
        return {"error": "Missing 'text' field"}

    return {
        "action": "voice",
        "input": text,
        "voice": "generated-global-voice"
    }
