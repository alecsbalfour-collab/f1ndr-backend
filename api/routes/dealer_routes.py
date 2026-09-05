from fastapi import APIRouter
from routes.controllers.dealer_controller import dealer_controller
from schemas.dealer_schemas import DealerSearchRequest, DealerSearchResponse

router = APIRouter(prefix="/dealer", tags=["dealer"])

@router.post("/search", response_model=DealerSearchResponse)
def search_dealers(payload: DealerSearchRequest):
    return dealer_controller.search(payload.query)
