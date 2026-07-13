from fastapi import APIRouter
from services.wchtr.voice_service import VoiceService

router = APIRouter()
voice = VoiceService()

@router.post("/wchtr/voice/text")
def set_voice_text(text: str):
    voice.set_text(text)
    return {"ok": True, "text": text}

@router.post("/wchtr/voice/emotion")
def set_voice_emotion(emotion: str):
    voice.set_emotion(emotion)
    return {"ok": True, "emotion": emotion}

@router.post("/wchtr/voice/pitch")
def set_voice_pitch(pitch: float):
    voice.set_pitch(pitch)
    return {"ok": True, "pitch": pitch}

@router.post("/wchtr/voice/pace")
def set_voice_pace(pace: float):
    voice.set_pace(pace)
    return {"ok": True, "pace": pace}

@router.post("/wchtr/voice/character")
def set_voice_character(character: str):
    voice.set_character(character)
    return {"ok": True, "character": character}

@router.get("/wchtr/voice/snapshot")
def get_voice_snapshot():
    return voice.snapshot()
