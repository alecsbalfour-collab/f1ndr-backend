def score_listing(listing):
    score = 0

    # Price scoring
    price = listing.get("price_num")
    if price:
        if price < 100:
            score += 1
        elif price < 500:
            score += 2
        elif price < 2000:
            score += 3
        else:
            score += 4

    # Category scoring
    cat = listing.get("category")
    if cat == "vehicles":
        score += 3
    elif cat == "housing":
        score += 4
    elif cat == "electronics":
        score += 2
    elif cat == "jobs":
        score += 1

    listing["score"] = score
    return listing
