from fastapi import APIRouter, HTTPException
from services.wtchr.wtchr_service import WtchrService
from models.wtchr.wtchr_model import WtchrRequest

router = APIRouter()
service = WtchrService()


@router.post("/wtchr")
def wtchr_core(payload: WtchrRequest):
    """
    WTCHR core engine.
    Handles watch timeline, frame processing, events, and state updates.
    """

    try:
        result = service.process(payload)

        return {
            "status": "success",
            "engine": "wtchr",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
