from fastapi import APIRouter, HTTPException
from services.renderer.renderer_service import RendererService
from models.renderer.renderer_model import RendererRequest

router = APIRouter()
service = RendererService()

@router.post("/renderer")
def renderer(payload: RendererRequest):
    try:
        result = service.process(payload.dict())
        return {
            "status": "success",
            "engine": "renderer",
            "input": payload.dict(),
            "output": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
