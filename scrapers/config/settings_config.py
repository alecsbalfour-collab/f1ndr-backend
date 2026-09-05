# scrapers/config/settings_config.py

import os

def load_scraper_settings() -> dict:
    return {
        "SCRAPER_ENV": os.getenv("F1NDR_SCRAPER_ENV", "dev"),
        "SCRAPER_DEBUG": os.getenv("F1NDR_SCRAPER_DEBUG", "false").lower() == "true",
        "VERSION": "1.0.0",
    }

def validate_scraper_settings(cfg: dict) -> bool:
    return (
        isinstance(cfg, dict)
        and "SCRAPER_ENV" in cfg
        and "SCRAPER_DEBUG" in cfg
    )
