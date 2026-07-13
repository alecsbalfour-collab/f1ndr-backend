import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://www.ebay.ca/sch/i.html?_nkw=&_sacat=0&LH_PrefLoc=1"


def scrape():
    listings = []

    html = requests.get(BASE_URL, headers={"User-Agent": "Mozilla/5.0"}).text
    soup = BeautifulSoup(html, "html.parser")

    items = soup.select(".s-item")

    for item in items:
        try:
            title_tag = item.select_one(".s-item__title")
            price_tag = item.select_one(".s-item__price")
            url_tag = item.select_one(".s-item__link")

            if not title_tag or not price_tag or not url_tag:
                continue

            title = title_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True)
            url = url_tag["href"]

            # Description is not always available on listing page
            description = ""

            listings.append({
                "title": title,
                "price": price,
                "location": "Canada",
                "url": url,
                "description": description,
                "created_at": datetime.utcnow().isoformat()
            })

        except Exception:
            continue

    return listings
