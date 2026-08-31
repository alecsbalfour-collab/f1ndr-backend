from fastapi import APIRouter
from engines.scrapers_engine import ScrapersEngine

router = APIRouter(
    prefix="/scrapers",
    tags=["scrapers"]
)

engine = ScrapersEngine()


@router.post("/platform")
async def set_platform(payload: dict):
    engine.set_platform(payload.get("platform", ""))
    return engine.snapshot()


@router.post("/query")
async def set_query(payload: dict):
    engine.set_query(payload.get("query", ""))
    return engine.snapshot()


@router.get("/run")
async def run_scraper():
    engine.run()
    return engine.snapshot()
