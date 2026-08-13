from fastapi import APIRouter, HTTPException
from services.insights.insights_service import InsightsService
from models.insights.insights_model import InsightsRequest

router = APIRouter()
service = InsightsService()

@router.post("/insights")
def insights(payload: InsightsRequest):
    try:
        result = service.process(payload.dict())
        return {
            "status": "success",
            "engine": "insights",
            "input": payload.dict(),
            "output": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
