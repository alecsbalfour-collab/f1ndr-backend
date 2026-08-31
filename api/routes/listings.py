from fastapi import APIRouter
from engines.listings_engine import ListingsEngine

router = APIRouter(
    prefix="/listings",
    tags=["listings"]
)

engine = ListingsEngine()


@router.post("/add")
async def add_listing(listing: dict):
    engine.add_listing(listing)
    return engine.snapshot()


@router.post("/filter")
async def filter_listings(filters: dict):
    engine.apply_filters(filters)
    engine.score_listings()
    return engine.snapshot()
