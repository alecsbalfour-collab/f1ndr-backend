import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://www.usedcalgary.com/classifieds/all"


def scrape():
    listings = []

    html = requests.get(BASE_URL, headers={"User-Agent": "Mozilla/5.0"}).text
    soup = BeautifulSoup(html, "html.parser")

    items = soup.select(".listing")

    for item in items:
        try:
            title = item.select_one(".title").get_text(strip=True)
            price = item.select_one(".price").get_text(strip=True)
            url = "https://www.usedcalgary.com" + item.select_one("a")["href"]

            detail_html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text
            detail_soup = BeautifulSoup(detail_html, "html.parser")

            desc_tag = detail_soup.select_one(".description")
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
