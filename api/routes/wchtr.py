from fastapi import APIRouter
from services.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/wtchr")
def wtchr(payload: dict):
    """
    WTCHR route for Findr.
    Accepts JSON payload: { "target": "...", "mode": "..." }
    """
    target = payload.get("target")
    mode = payload.get("mode", "default")

    if not target:
        return {"error": "Missing 'target' field"}

    # WTCHR currently uses scrape() as its backend engine
    result = service.scrape({"target": target})

    return {
        "action": "wtchr",
        "mode": mode,
        "target": target,
        "result": result
    }
