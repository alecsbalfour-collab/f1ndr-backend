from fastapi import APIRouter, HTTPException
from services.search.search_service import SearchService
from models.search.search_model import SearchRequest

router = APIRouter()
service = SearchService()

@router.post("/search")
def search(payload: SearchRequest):
    try:
        return service.process(payload.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
