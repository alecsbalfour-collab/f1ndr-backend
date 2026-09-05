# scrapers/config/marketplace_config.py

def get_marketplace_config() -> dict:
    return {
        "facebook": {"enabled": True, "rate_limit": 2},
        "kijiji": {"enabled": True, "rate_limit": 3},
        "craigslist": {"enabled": True, "rate_limit": 1},
        "ebay": {"enabled": True, "rate_limit": 5},
        "amazon": {"enabled": True, "rate_limit": 10},
    }
