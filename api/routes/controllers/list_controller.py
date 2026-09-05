from utils.response_builder import success_response
from schemas.list_schemas import Listing

class ListController:
    def search(self, query: str):
        results = []
        return success_response({"results": results})

list_controller = ListController()
