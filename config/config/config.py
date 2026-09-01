from backend.config.environment import env

class Config:
    MONGO_URI = env.MONGO_URI

    ENABLED_PLATFORMS = [
        "kijiji",
        "facebook",
        "autotrader",
        "craigslist",
        "usedca",
        "marketplace_ca",
        "ebay",
        "realtor",
        "rentfaster",
        "zillow"
    ]

config = Config()
