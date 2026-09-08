from fastapi import APIRouter
from utils.response_builder import success_response

router = APIRouter(prefix="/version", tags=["version"])

@router.get("/")
async def version_info():
    return success_response({
        "version": "1.0.0",
        "description": "F1NDR Backend API",
        "status": "stable"
    })
