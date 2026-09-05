from fastapi import APIRouter
from routes.controllers.sell_controller import sell_controller
from schemas.sell_schemas import SellRequest, SellResponse

router = APIRouter(prefix="/sell", tags=["sell"])

@router.post("/", response_model=SellResponse)
def sell_item(payload: SellRequest):
    return sell_controller.create(payload)
