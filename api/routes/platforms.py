from fastapi import APIRouter
from engines.platforms_engine import PlatformsEngine

router = APIRouter(
    prefix="/platforms",
    tags=["platforms"]
)

engine = PlatformsEngine()


@router.post("/register")
async def register_platform(payload: dict):
    engine.register_platform(
        payload.get("name", ""),
        payload.get("metadata", {})
    )
    return engine.snapshot()


@router.post("/select")
async def select_platform(payload: dict):
    engine.select_platform(payload.get("name", ""))
    return engine.snapshot()


@router.post("/metadata")
async def update_metadata(payload: dict):
    engine.update_metadata(
        payload.get("name", ""),
        payload.get("metadata", {})
    )
    return engine.snapshot()
