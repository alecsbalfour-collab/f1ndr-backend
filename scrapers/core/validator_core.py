# scrapers/core/validator_core.py

def is_valid_scraper_record(record: dict) -> bool:
    """
    Basic validation: must be dict and contain title.
    """
    return isinstance(record, dict) and "title" in record


def validate_listing(record: dict) -> bool:
    """
    Strong validation for final listing objects.
    """
    return (
        isinstance(record, dict)
        and "title" in record
        and "url" in record
        and isinstance(record["title"], str)
        and isinstance(record["url"], str)
    )
