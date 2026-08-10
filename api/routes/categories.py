from fastapi import APIRouter

router = APIRouter()

@router.get("/categories")
def get_categories():
    return {
        "categories": [
            "cars",
            "trucks",
            "motorcycles",
            "bicycles",
            "electronics",
            "phones",
            "computers",
            "furniture",
            "appliances",
            "real_estate",
            "rentals",
            "jobs",
            "services",
            "free",
            "misc"
        ]
    }
