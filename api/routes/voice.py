from fastapi import APIRouter, HTTPException
from services.voice.voice_service import VoiceService
from models.voice.voice_model import VoiceRequest

router = APIRouter()
service = VoiceService()

@router.post("/voice")
def voice(payload: VoiceRequest):
    try:
        result = service.process(payload.dict())
        return {
            "status": "success",
            "engine": "voice",
            "input": payload.dict(),
            "output": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
