from fastapi import APIRouter

router = APIRouter()

@router.post("/trinn")
def trinn(payload: dict):
    """
    Trinn route.
    Accepts JSON payload: { "input": ... }
    """
    text = payload.get("input")
    if not text:
        return {"error": "Missing 'input' field"}

    return {
        "action": "trinn",
        "input": text,
        "output": f"trinn-processed: {text}"
    }
