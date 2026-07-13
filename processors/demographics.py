def infer_demographics(listing):
    demo = {}

    # Income level from price
    price = listing.get("price_num")
    if price:
        if price < 500:
            demo["income_level"] = "low"
        elif price < 5000:
            demo["income_level"] = "middle"
        else:
            demo["income_level"] = "high"
    else:
        demo["income_level"] = "unknown"

    # Seller type (simple version)
    demo["seller_type"] = "individual"

    # Category-based demographic inference
    cat = listing.get("category", "").lower()
    if cat == "vehicles":
        demo["likely_demographic"] = "adult male"
    elif cat == "housing":
        demo["likely_demographic"] = "mixed adults"
    elif cat == "electronics":
        demo["likely_demographic"] = "younger adults"
    elif cat == "jobs":
        demo["likely_demographic"] = "working adults"
    else:
        demo["likely_demographic"] = "general population"

    listing["demographics"] = demo
    return listing
