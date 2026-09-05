# scrapers/core/normalization_core.py

def normalize_listing(record: dict) -> dict:
    """
    Normalize basic listing fields.
    """
    normalized = dict(record)

    title = normalized.get("title")
    if isinstance(title, str):
        normalized["title"] = title.strip().title()
    else:
        normalized["title"] = ""

    return normalized
