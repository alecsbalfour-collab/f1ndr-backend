from utils.response_builder import created_response
from schemas.sell_schemas import SellItem, SellRequest

class SellController:
    def create(self, payload: SellRequest):
        item = SellItem(
            id="temp-id",
            title=payload.title,
            price=payload.price,
            condition=payload.condition,
            description=payload.description,
        )
        return created_response({"item": item})

sell_controller = SellController()
