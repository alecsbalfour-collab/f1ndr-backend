from utils.response_builder import success_response

class SearchController:
    def search(self, query: str):
        return success_response({"query": query, "results": []})

search_controller = SearchController()
