from fastapi import APIRouter
from utils.response_builder import success_response

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/")
async def health_check():
    # No DB calls, no external services — just a heartbeat.
    return success_response({"status": "ok"})
