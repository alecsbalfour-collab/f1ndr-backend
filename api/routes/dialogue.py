from fastapi import APIRouter, HTTPException
from services.dialogue.dialogue_service import DialogueService
from models.dialogue.dialogue_model import build_dialogue_contract

router = APIRouter()
dialogue = DialogueService()

@router.post("/personality")
def set_personality(payload: dict):
    p = payload.get("personality")
    if not p:
        raise HTTPException(status_code=400, detail="personality required")
    dialogue.set_personality(p)
    return {"personality": p}

@router.post("/send")
def send_message(payload: dict):
    msg = payload.get("message")
    if not msg:
        raise HTTPException(status_code=400, detail="message required")
    reply = dialogue.send_message(msg)
    return {"reply": reply}

@router.get("/history")
def get_history():
    return build_dialogue_contract(dialogue.history())
