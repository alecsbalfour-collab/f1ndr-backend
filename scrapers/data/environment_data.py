# scrapers/core/data/environment_data.py

import os

def get_environment() -> dict:
    """
    Return scraper environment settings.
    """
    return {
        "env": os.getenv("f1ndr_SCRAPER_ENV", "dev"),
        "debug": os.getenv("f1ndr_SCRAPER_DEBUG", "false").lower() == "true",
        "version": "1.0.0",
    }
