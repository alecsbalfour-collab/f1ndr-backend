from fastapi import APIRouter

router = APIRouter()


from services.trinn_interaction_engine import TrinnInteractionEngine

interaction_engine = TrinnInteractionEngine()


@router.post("/trinn/personality/{profile}")
def set_trinn_personality(profile: str):
    interaction_engine.set_personality(profile)
    return {"personality": interaction_engine.get_personality()}


@router.post("/trinn/message")
def send_message_to_trinn(payload: dict):
    user_message = payload.get("message", "")
    if not user_message:
        raise HTTPException(status_code=400, detail="message is required")

    return interaction_engine.handle_message(user_message)

from services.trinn_interaction_engine import TrinnInteractionEngine

interaction_engine = TrinnInteractionEngine()

@router.post("/trinn/personality/{profile}")
def set_trinn_personality(profile: str):
    interaction_engine.set_personality(profile)
    return {"personality": interaction_engine.dialogue.get_personality()}

@router.post("/trinn/message")
def send_message_to_trinn(payload: dict):
    user_message = payload.get("message", "")
    if not user_message:
        raise HTTPException(status_code=400, detail="message is required")

    return interaction_engine.handle_message(user_message)
@router.get("/trinn/animation")
def get_trinn_animation():
    return interaction_engine.controller.animation.snapshot()
