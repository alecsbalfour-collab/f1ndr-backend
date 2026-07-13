from fastapi import APIRouter, HTTPException
from services.scene.scene_service import SceneService
from models.scene.scene_model import build_scene_contract

router = APIRouter()
scene = SceneService()

@router.post("/location")
def set_location(payload: dict):
    loc = payload.get("location")
    if not loc:
        raise HTTPException(status_code=400, detail="location required")
    scene.set_location(loc)
    return {"location": loc}

@router.post("/time")
def set_time(payload: dict):
    t = payload.get("time")
    if not t:
        raise HTTPException(status_code=400, detail="time required")
    scene.set_time_of_day(t)
    return {"time": t}

@router.post("/weather")
def set_weather(payload: dict):
    w = payload.get("weather")
    if not w:
        raise HTTPException(status_code=400, detail="weather required")
    scene.set_weather(w)
    return {"weather": w}

@router.post("/character/add")
def add_character(payload: dict):
    name = payload.get("name")
    if not name:
        raise HTTPException(status_code=400, detail="name required")
    scene.add_character(name)
    return {"added": name}

@router.post("/character/remove")
def remove_character(payload: dict):
    name = payload.get("name")
    if not name:
        raise HTTPException(status_code=400, detail="name required")
    scene.remove_character(name)
    return {"removed": name}

@router.post("/object/add")
def add_object(payload: dict):
    obj = payload.get("object")
    if not obj:
        raise HTTPException(status_code=400, detail="object required")
    scene.add_object(obj)
    return {"added": obj}

@router.post("/object/remove")
def remove_object(payload: dict):
    obj = payload.get("object")
    if not obj:
        raise HTTPException(status_code=400, detail="object required")
    scene.remove_object(obj)
    return {"removed": obj}

@router.post("/mood")
def set_mood(payload: dict):
    mood = payload.get("mood")
    if not mood:
        raise HTTPException(status_code=400, detail="mood required")
    scene.set_mood(mood)
    return {"mood": mood}

@router.get("/contract")
def get_scene_contract():
    return build_scene_contract(scene.snapshot())
