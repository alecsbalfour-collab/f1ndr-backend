from fastapi import APIRouter
from engines.search_engine import SearchEngine

router = APIRouter(
    prefix="/search",
    tags=["search"]
)

engine = SearchEngine()


@router.post("/query")
async def set_query(payload: dict):
    engine.set_query(payload.get("query", ""))
    return engine.snapshot()


@router.post("/filters")
async def apply_filters(payload: dict):
    engine.apply_filters(payload)
    return engine.snapshot()


@router.get("/run")
async def run_search():
    engine.run_search()
    return engine.snapshot()
