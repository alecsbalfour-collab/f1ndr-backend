def get_source_metadata():
    """
    Returns metadata describing all scraper sources.
    Used by the scraper engine to know which platforms exist,
    their display names, and their internal identifiers.
    """

    return {
        "sources": [
            {
                "id": "kijiji",
                "name": "Kijiji",
                "enabled": True,
            },
            {
                "id": "facebook",
                "name": "Facebook Marketplace",
                "enabled": True,
            },
            {
                "id": "craigslist",
                "name": "Craigslist",
                "enabled": True,
            },
            {
                "id": "autoTrader",
                "name": "AutoTrader",
                "enabled": False,
            },
        ]
    }
