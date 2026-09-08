from fastapi import APIRouter, Depends
from utils.response_builder import success_response
from core.rules_core import rule_engine

# Initialize the router instance that api/main.py is looking for
router = APIRouter(prefix="/search", tags=["Search"])

class SearchController:
    """
    Enterprise Search Controller.
    Handles business rules execution and response delivery.
    """
    def search(self, query: str):
        # Using evaluate method matching our rebuilt rules engine
        processed = rule_engine.evaluate({"query": query}, criteria={})
        
        result = {
            "query": processed.get("query", query),
            "results": [],
        }
        return success_response(result, "Search completed")

search_controller = SearchController()

# Expose an HTTP GET endpoint mapped to the controller method
@router.get("")
async def execute_search(query: str):
    return search_controller.search(query=query)
