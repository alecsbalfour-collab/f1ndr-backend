def validate_listing(record: dict) -> bool:
    return (
        isinstance(record, dict)
        and "title" in record
        and "url" in record
        and isinstance(record["title"], str)
        and isinstance(record["url"], str)
    )
