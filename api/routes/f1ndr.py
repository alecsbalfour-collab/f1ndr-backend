from fastapi import APIRouter
from api.models.search_request import SearchRequest
from api.models.search_response import SearchResponse
from services.f1ndr.f1ndr_service import F1ndrService

router = APIRouter()

@router.post("/search", response_model=SearchResponse)
async def search(request: SearchRequest):
    data = F1ndrService().search(request.query, request.platforms)
    return SearchResponse(results=data["results"], total=data["total"])

@router.get("/test")
async def test():
    return {"message": "f1ndr route working"}
