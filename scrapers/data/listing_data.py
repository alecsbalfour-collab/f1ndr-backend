# scrapers/core/data/listing_data.py

def create_listing_record(raw: dict) -> dict:
    """
    Create a normalized listing record from raw scraper output.
    """
    return {
        "title": raw.get("title", "").strip() if isinstance(raw.get("title"), str) else "",
        "price": raw.get("price"),
        "url": raw.get("url"),
        "image": raw.get("image"),
        "location": raw.get("location"),
        "posted_at": raw.get("posted_at"),
        "platform": raw.get("platform"),
        "scraped": raw.get("scraped", False),
    }
