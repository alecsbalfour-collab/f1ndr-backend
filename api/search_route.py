from fastapi import APIRouter
from models.search_model import SearchRequest

from engines.f1ndr.f1ndr_engine import F1ndrEngine
from mongo.search_history_repo import SearchHistoryRepo

router = APIRouter()
engine = F1ndrEngine()
history = SearchHistoryRepo()

@router.post("/")
def search(req: SearchRequest):
    history.log(req.query, req.platforms or [])
    results = engine.run(req.query, req.platforms)
    return {"results": results}
