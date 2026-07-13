def parse_price(price_str):
    if not price_str:
        return None
    digits = ''.join(c for c in price_str if c.isdigit())
    return int(digits) if digits else None


def normalize_listing(raw, platform):
    return {
        "platform": platform,
        "title": raw.get("title", "").strip(),
        "description": raw.get("description", "").strip(),
        "price": raw.get("price"),
        "price_num": parse_price(raw.get("price")),
        "url": raw.get("url"),
        "location": raw.get("location", "").strip(),
        "created_at": raw.get("created_at"),
        "raw": raw
    }
