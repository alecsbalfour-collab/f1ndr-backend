from fastapi import APIRouter, HTTPException
from services.platforms.platforms_service import PlatformsService
from models.platforms.platforms_model import PlatformsRequest

router = APIRouter()
service = PlatformsService()

@router.post("/platforms")
def platforms(payload: PlatformsRequest):
    try:
        return service.process(payload.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
