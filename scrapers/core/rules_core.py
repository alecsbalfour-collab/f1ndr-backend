def apply_scraper_rules(record: dict) -> dict:
    cleaned = dict(record)

    if "title" in cleaned:
        cleaned["title"] = cleaned["title"].strip()

    if "price" in cleaned:
        try:
            cleaned["price"] = float(cleaned["price"])
        except Exception:
            cleaned["price"] = None

    cleaned["scraped"] = True
    return cleaned

def is_valid_scraper_record(record: dict) -> bool:
    return isinstance(record, dict) and "title" in record
