from fastapi import APIRouter
from api.models.search_request import SearchRequest
from services.f1ndr.f1ndr_service import F1ndrService

router = APIRouter()

@router.post("/search")
async def search(request: SearchRequest):
    return F1ndrService().search(request.query, request.platforms)

@router.get("/test")
async def test():
    return {"message": "f1ndr route working"}
