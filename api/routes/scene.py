from fastapi import APIRouter, HTTPException
from services.scene.scene_service import SceneService
from models.scene_model import SceneRequest

router = APIRouter()
service = SceneService()


@router.post("/scene")
def generate_scene(payload: SceneRequest):
    """
    Generate a scene using the existing SceneService.
    This wires the route → service → engine → model exactly as your architecture intends.
    """

    try:
        result = service.generate_scene(payload)

        return {
            "status": "success",
            "engine": "scene",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
