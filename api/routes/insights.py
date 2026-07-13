from fastapi import APIRouter
from db.mongo import get_listings_collection

router = APIRouter()


@router.get("/popular")
def popular_categories():
    col = get_listings_collection()
    data = list(col.aggregate([
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]))
    return {"popular_categories": data}


@router.get("/demographics")
def demographics():
    col = get_listings_collection()

    income = list(col.aggregate([
        {"$group": {"_id": "$demographics.income_level", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]))

    demo_groups = list(col.aggregate([
        {"$group": {"_id": "$demographics.likely_demographic", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]))

    return {
        "income_levels": income,
        "likely_demographics": demo_groups
    }


@router.get("/platform_activity")
def platform_activity():
    col = get_listings_collection()
    data = list(col.aggregate([
        {"$group": {"_id": "$platform", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]))
    return {"platform_activity": data}
