from fastapi import APIRouter
from utils.response_builder import success_response
from schemas.list_schemas import Listing

# Router for listings
router = APIRouter(prefix="/listings", tags=["listings"])

# 1) Unified listings endpoint
@router.get("/unified")
async def get_unified_listings():
    return success_response({
        "source": "unified",
        "items": []
    })

# 2) Raw platform listings endpoints
@router.get("/raw/facebook")
async def get_raw_facebook_listings():
    return success_response({
        "platform": "facebook",
        "items": []
    })

@router.get("/raw/kijiji")
async def get_raw_kijiji_listings():
    return success_response({
        "platform": "kijiji",
        "items": []
    })

@router.get("/raw/craigslist")
async def get_raw_craigslist_listings():
    return success_response({
        "platform": "craigslist",
        "items": []
    })

class ListController:
    def search(self, query: str):
        results = []
        return success_response({"results": results})

list_controller = ListController()
