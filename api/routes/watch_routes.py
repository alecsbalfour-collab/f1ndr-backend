from fastapi import APIRouter
from routes.controllers.watch_controller import watch_controller
from schemas.watch_schemas import WatchRequest, WatchResponse

router = APIRouter(prefix="/watch", tags=["watch"])

@router.post("/search", response_model=WatchResponse)
def watch_search(payload: WatchRequest):
    return watch_controller.search(payload.query)
