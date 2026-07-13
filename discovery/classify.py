from bs4 import BeautifulSoup


def looks_like_marketplace(soup: BeautifulSoup) -> bool:
    if soup is None:
        return False

    cards = soup.select("div[class*='listing'], div[class*='card'], li[class*='result']")
    if len(cards) < 5:
        return False

    text = soup.get_text(" ", strip=True).lower()
    keywords = ["for sale", "price", "rent", "listing", "classifieds", "marketplace"]
    score = sum(1 for k in keywords if k in text)

    return score >= 2


def extract_item_selector(soup: BeautifulSoup) -> str | None:
    candidates = [
        "div[class*='listing']",
        "div[class*='card']",
        "li[class*='result']",
    ]

    for sel in candidates:
        items = soup.select(sel)
        if len(items) >= 5:
            return sel

    return None
