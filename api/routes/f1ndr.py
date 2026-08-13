from fastapi import APIRouter, HTTPException
from services.f1ndr.f1ndr_service import F1ndrService
from models.f1ndr.f1ndr_model import F1ndrRequest

router = APIRouter()
service = F1ndrService()

@router.post("/f1ndr")
def f1ndr(payload: F1ndrRequest):
    try:
        return service.process(payload.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
