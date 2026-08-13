from fastapi import APIRouter, HTTPException
from services.wtchr.wchtr_renderer_service import WchtrRendererService
from models.wtchr.wchtr_renderer_model import WchtrRenderRequest

router = APIRouter()
service = WchtrRendererService()


@router.post("/wchtr/renderer")
def wchtr_render(payload: WchtrRenderRequest):
    """
    WTCHR renderer.
    Handles frame rendering, timeline rendering, and watch-specific visuals.
    """

    try:
        result = service.render(payload)

        return {
            "status": "success",
            "engine": "wchtr_renderer",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
