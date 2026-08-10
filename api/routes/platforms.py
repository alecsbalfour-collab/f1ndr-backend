from fastapi import APIRouter

router = APIRouter()

@router.get("/platforms")
def get_platforms():
    return {
        "platforms": [
            "kijiji",
            "craigslist",
            "facebook",
            "ebay",
            "autotrader",
            "used",
            "used_ca",
            "realtor",
            "zillow",
            "rent-faster"
        ]
    }
