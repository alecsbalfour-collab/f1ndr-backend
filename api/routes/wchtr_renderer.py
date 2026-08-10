from fastapi import APIRouter

router = APIRouter()

@router.post("/wchtr/renderer")
def wchtr_renderer(payload: dict):
    """
    WTCHR Renderer route.
    Accepts JSON payload: { "frame": ... }
    """
    frame = payload.get("frame")
    if not frame:
        return {"error": "Missing 'frame' field"}

    return {
        "action": "wchtr_renderer",
        "input": frame,
        "rendered": "rendered-frame"
    }
