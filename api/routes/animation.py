from fastapi import APIRouter, HTTPException
from services.animation.animation_timeline_service import AnimationTimelineService
from models.animation.animation_timeline_model import build_animation_timeline_contract

router = APIRouter()
timeline = AnimationTimelineService()

@router.post("/event")
def add_event(payload: dict):
    anim = payload.get("animation")
    dur = payload.get("duration")
    easing = payload.get("easing", "linear")

    if not anim or dur is None:
        raise HTTPException(status_code=400, detail="animation and duration required")

    timeline.add_event(anim, float(dur), easing)
    return {"added": anim}

@router.post("/clear")
def clear():
    timeline.clear()
    return {"cleared": True}

@router.post("/play")
def play():
    timeline.play()
    return {"playing": True}

@router.post("/stop")
def stop():
    timeline.stop()
    return {"playing": False}

@router.get("/contract")
def get_contract():
    return build_animation_timeline_contract(timeline.snapshot())
