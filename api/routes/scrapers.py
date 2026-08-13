from fastapi import APIRouter, HTTPException
from services.scrapers.scrapers_service import ScrapersService
from models.scrapers.scrapers_model import ScraperRequest

router = APIRouter()
service = ScrapersService()

@router.post("/scrapers")
def scrapers(payload: ScraperRequest):
    try:
        return service.process(payload.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
