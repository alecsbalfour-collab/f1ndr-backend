import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://www.zillow.com/calgary-ab/"


def scrape():
    listings = []

    html = requests.get(BASE_URL, headers={"User-Agent": "Mozilla/5.0"}).text
    soup = BeautifulSoup(html, "html.parser")

    items = soup.select(".list-card-info")

    for item in items:
        try:
            title = item.select_one(".list-card-addr").get_text(strip=True)
            price = item.select_one(".list-card-price").get_text(strip=True)
            url = item.select_one("a")["href"]

            listings.append({
                "title": title,
                "price": price,
                "location": "Calgary",
                "url": url,
                "description": "",
                "created_at": datetime.utcnow().isoformat()
            })

        except Exception:
            continue

    return listings
