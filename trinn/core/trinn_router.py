# trinn/trinn_router.py

from fastapi import APIRouter
from trinn.trinn_brain import TrinnBrain

router = APIRouter()
brain = TrinnBrain()

@router.post("/trinn")
def trinn_endpoint(payload: dict):
    text = payload.get("text", "")
    return brain.think(text)
