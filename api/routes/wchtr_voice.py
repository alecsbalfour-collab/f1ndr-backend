from fastapi import APIRouter, HTTPException
from services.wtchr.wchtr_voice_service import WchtrVoiceService
from models.wtchr.wchtr_voice_model import WchtrVoiceRequest

router = APIRouter()
service = WchtrVoiceService()


@router.post("/wchtr/voice")
def wchtr_voice(payload: WchtrVoiceRequest):
    """
    WTCHR voice engine.
    Handles watch-specific voice synthesis, alerts, tones, and voice responses.
    """

    try:
        result = service.generate_voice(payload)

        return {
            "status": "success",
            "engine": "wchtr_voice",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
