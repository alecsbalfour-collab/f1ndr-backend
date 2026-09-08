from fastapi import APIRouter
from utils.response_builder import success_response

router = APIRouter(prefix="/sell", tags=["Sell"])

class SellController:
    """
    Enterprise Sell Controller.
    Manages sales pipelines, transactional workflows, and market data listing layers.
    """
    def get_listings(self):
        data = {
            "listings": [],
            "total_count": 0
        }
        return success_response(data, "Sales listings retrieved successfully")

sell_controller = SellController()

@router.get("")
async def list_sales():
    return sell_controller.get_listings()
