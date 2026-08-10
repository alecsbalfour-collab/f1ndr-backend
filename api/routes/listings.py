from fastapi import APIRouter
from services.f1ndr_service import F1ndrService

router = APIRouter()
service = F1ndrService()

@router.post("/listings")
def listings(payload: dict):
    """
    Listings route for Findr.
    Accepts JSON payload:
    {
        "targets": ["url1", "url2", "url3"]
    }
    """
    targets = payload.get("targets")
    if not targets or not isinstance(targets, list):
        return {"error": "Missing 'targets' list"}

    results = []

    for target in targets:
        result = service.scrape({"target": target})
        results.append(result)

    return {
        "action": "listings",
        "count": len(results),
        "results": results
    }
