# Global constants used across the backend

DEFAULT_PLATFORMS = [
    "kijiji",
    "facebook",
    "autotrader",
    "craigslist",
    "marketplace_ca",
    "used_ca"
]

SUPPORTED_CATEGORIES = [
    "vehicles",
    "real_estate",
    "electronics",
    "furniture",
    "general"
]

PIPELINE_STEPS = [
    "scrape",
    "normalize",
    "dedupe",
    "enrich",
    "index"
]
