from bs4 import BeautifulSoup
from datetime import datetime
from scrapers.engine import fetch

BASE_URL = "https://www.autotrader.ca/cars/ab/calgary/"


def scrape():
    listings = []

    html = fetch(BASE_URL)
    if not html:
        return listings

    soup = BeautifulSoup(html, "html.parser")
    items = soup.select(".result-item")

    for item in items:
        try:
            title = item.select_one(".result-title").get_text(strip=True)
            price = item.select_one(".price-amount").get_text(strip=True)
            url = "https://www.autotrader.ca" + item.select_one("a")["href"]

            detail_html = fetch(url)
            description = ""
            if detail_html:
                detail_soup = BeautifulSoup(detail_html, "html.parser")
                desc_tag = detail_soup.select_one(".listing-description")
                description = desc_tag.get_text(strip=True) if desc_tag else ""

            listings.append({
                "title": title,
                "price": price,
                "location": "Calgary",
                "url": url,
                "description": description,
                "created_at": datetime.utcnow().isoformat()
            })

        except Exception:
            continue

    return listings
