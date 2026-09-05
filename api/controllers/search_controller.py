from utils.response_builder import success_response
from core.rules_core import rule_engine

class SearchController:
    """
    Example search controller.
    Replace logic later when integrating real search modules.
    """

    def search(self, query: str):
        processed = rule_engine.apply_rules({"query": query})

        # Placeholder search result
        result = {
            "query": processed["query"],
            "results": [],
        }

        return success_response(result, "Search completed")


search_controller = SearchController()
