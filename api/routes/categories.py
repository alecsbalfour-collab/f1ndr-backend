from fastapi import APIRouter

router = APIRouter()

DEFAULT_CATEGORIES = [
    "vehicles",
    "housing",
    "electronics",
    "jobs",
    "services",
    "misc"
]


@router.get("/")
def list_categories():
    return {"categories": DEFAULT_CATEGORIES}
