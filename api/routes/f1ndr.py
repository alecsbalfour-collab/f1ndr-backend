from fastapi import APIRouter, HTTPException
from services.f1ndr.f1ndr_service import F1ndrService

router = APIRouter(prefix="/f1ndr", tags=["f1ndr"])
f1ndr = F1ndrService()

@router.get("/status")
def status():
    return {"status": "ok", "module": "f1ndr"}

@router.post("/search")
def search(payload: dict):
    try:
        return f1ndr.search(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/scrape")
def scrape(payload: dict):
    try:
        return f1ndr.scrape(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/render")
def render(payload: dict):
    try:
        return f1ndr.render(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/contract")
def contract(payload: dict):
    try:
        return f1ndr.contract(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
