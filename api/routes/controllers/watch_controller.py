from utils.response_builder import success_response
from schemas.watch_schemas import WatchItem

class WatchController:
    def search(self, query: str):
        results = []
        return success_response({"results": results})

watch_controller = WatchController()
