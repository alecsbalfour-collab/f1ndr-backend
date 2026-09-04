from scrapers.config.settings_config import load_scraper_settings
from scrapers.core.rules_core import apply_scraper_rules
from scrapers.data.environment_data import get_environment_data
from scrapers.db.scrapers_db_connection import get_scraper_connection
from scrapers.utils.helpers_utils import generate_scraper_id


def load_scraper_system() -> dict:
    """
    Load all scraper subsystems in a unified structure.
    Mirrors the architecture used across core/data/db/tests.
    """
    return {
        "config": load_scraper_settings(),
        "environment": get_environment_data(),
        "connection": get_scraper_connection(),
        "utils": {"id": generate_scraper_id()},
    }


def run_scraper_pipeline(payload: dict) -> dict:
    """
    Run scraper rule pipeline.
    Applies normalization, validation, and transformation rules.
    """
    return apply_scraper_rules(payload)
