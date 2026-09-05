from fastapi import APIRouter
from api.schemas.search_schema import SearchRequest
from api.controllers.search_controller import SearchController

router = APIRouter()
controller = SearchController()

@router.post("/")
async def search(payload: SearchRequest):
    return controller.search(payload)
from fastapi import APIRouter
from routes.controllers.search_controller import search_controller
from schemas.search_schema import SearchRequest, SearchResult

router = APIRouter(prefix="/search", tags=["search"])

@router.post("/", response_model=SearchResult)
def search(payload: SearchRequest):
    return search_controller.search(payload.query)
