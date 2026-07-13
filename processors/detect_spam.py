def is_spam(listing):
    title = listing.get("title", "").lower()
    desc = listing.get("description", "").lower()

    spam_words = [
        "click here",
        "visit site",
        "promo",
        "discount",
        "free money",
        "work from home",
        "crypto investment",
        "guaranteed profit"
    ]

    if any(word in title or word in desc for word in spam_words):
        return True

    if len(desc) < 10:
        return True

    return False
