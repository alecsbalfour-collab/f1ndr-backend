from bs4 import BeautifulSoup
from datetime import datetime
from scrapers.engine import fetch

BASE_URL = "https://www.kijiji.ca/b-calgary/"


def scrape():
    listings = []

    html = fetch(BASE_URL)
    if not html:
        return listings

    soup = BeautifulSoup(html, "html.parser")
    items = soup.select(".search-item")

    for item in items:
        try:
            title = item.select_one(".title").get_text(strip=True)
            price = item.select_one(".price").get_text(strip=True)
            location = item.select_one(".location").get_text(strip=True)
            url = "https://www.kijiji.ca" + item.select_one(".title")["href"]

            detail_html = fetch(url)
            description = ""
            if detail_html:
                detail_soup = BeautifulSoup(detail_html, "html.parser")
                desc_tag = detail_soup.select_one(".descriptionContainer")
                description = desc_tag.get_text(strip=True) if desc_tag else ""

            listings.append({
                "title": title,
                "price": price,
                "location": location,
                "url": url,
                "description": description,
                "created_at": datetime.utcnow().isoformat()
            })

        except Exception:
            continue

    return listings
