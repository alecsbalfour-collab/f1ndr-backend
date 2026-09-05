# scrapers/core/data/source_data.py

def get_source_info(platform: str) -> dict:
    """
    Return metadata for a scraper source/platform.
    """
    return {
        "platform": platform,
        "active": True,
        "type": "marketplace",
    }
