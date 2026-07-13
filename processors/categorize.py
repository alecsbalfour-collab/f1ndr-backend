def categorize_listing(listing):
    title = listing.get("title", "").lower()
    desc = listing.get("description", "").lower()

    if any(x in title or x in desc for x in ["car", "truck", "suv", "vehicle", "auto"]):
        listing["category"] = "vehicles"

    elif any(x in title or x in desc for x in ["rent", "apartment", "house", "condo", "room"]):
        listing["category"] = "housing"

    elif any(x in title or x in desc for x in ["iphone", "samsung", "laptop", "pc", "tablet", "electronics"]):
        listing["category"] = "electronics"

    elif any(x in title or x in desc for x in ["job", "hiring", "career", "position"]):
        listing["category"] = "jobs"

    else:
        listing["category"] = "misc"

    return listing
