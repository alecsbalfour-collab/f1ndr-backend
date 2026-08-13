from fastapi import APIRouter, HTTPException
from services.animation.animation_timeline_service import AnimationTimelineService
from models.animation.animation_timeline_model import AnimationTimelineRequest

router = APIRouter()
service = AnimationTimelineService()


@router.post("/animation/timeline")
def generate_animation_timeline(payload: AnimationTimelineRequest):
    """
    Generate an animation timeline using the existing AnimationTimelineService.
    This wires the route → service → engine → model exactly as your architecture intends.
    """

    try:
        result = service.generate_timeline(payload)
        return {
            "status": "success",
            "engine": "animation_timeline",
            "input": payload.dict(),
            "output": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
