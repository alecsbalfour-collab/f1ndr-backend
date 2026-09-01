from fastapi import APIRouter
from mongo.listings_repo import ListingsRepo

router = APIRouter()
repo = ListingsRepo()

@router.get("/")
def get_all_listings():
    return repo.get_all()

@router.delete("/")
def clear_listings():
    repo.clear()
    return {"status": "cleared"}
