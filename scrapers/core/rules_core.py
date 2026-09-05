# scrapers/core/rules_core.py

def apply_scraper_rules(record: dict) -> dict:
    """
    Apply cleanup rules to raw scraper output.
    """
    cleaned = dict(record)

    # Title cleanup
    if "title" in cleaned and isinstance(cleaned["title"], str):
        cleaned["title"] = cleaned["title"].strip()

    # Price normalization
    if "price" in cleaned:
        try:
            cleaned["price"] = float(cleaned["price"])
        except Exception:
            cleaned["price"] = None

    cleaned["scraped"] = True
    return cleaned
