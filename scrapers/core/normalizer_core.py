def normalize_listing(record: dict) -> dict:
    normalized = dict(record)
    normalized["title"] = normalized.get("title", "").strip().title()
    return normalized
