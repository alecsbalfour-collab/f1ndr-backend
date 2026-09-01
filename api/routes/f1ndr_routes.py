from fastapi import APIRouter
from models.search_request import SearchRequest
from engines.f1ndr.listings_engine import F1ndrEngine

router = APIRouter()

@router.post("/search")
def search(request: SearchRequest):
    engine = F1ndrEngine()
    return engine.search(request.query, request.platforms)
