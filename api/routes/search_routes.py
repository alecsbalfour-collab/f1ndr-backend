from fastapi import APIRouter
from api.schemas.search_schema import SearchRequest
from api.controllers.search_controller import SearchController

router = APIRouter()
controller = SearchController()

@router.post("/")
async def search(payload: SearchRequest):
    return controller.search(payload)
