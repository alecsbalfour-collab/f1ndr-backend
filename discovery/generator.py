import os
from datetime import datetime
from bs4 import BeautifulSoup
from discovery.scan import get_dom
from discovery.classify import looks_like_marketplace, extract_item_selector


SCRAPERS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scrapers")


def safe_name_from_url(url: str) -> str:
    name = url.replace("https://", "").replace("http://", "")
    name = name.split("/")[0]
    name = name.replace(".", "_").replace("-", "_")
    return name


def generate_scraper_file(url: str):
    soup = get_dom(url)
    if not looks_like_marketplace(soup):
        return None

    item_selector = extract_item_selector(soup)
    if not item_selector:
        return None

    platform_name = safe_name_from_url(url)
    filename = os.path.join(SCRAPERS_DIR, f"{platform_name}.py")

    template = f'''import requests
from bs4 import BeautifulSoup
from datetime import datetime


def scrape():
    url = "{url}"
    resp = requests.get(url, headers={{"User-Agent": "Mozilla/5.0"}})
    soup = BeautifulSoup(resp.text, "html.parser")

    listings = []

    for item in soup.select("{item_selector}"):
        title_el = item.select_one("h2, .title, a")
        price_el = item.select_one(".price, [class*='price']")
        loc_el = item.select_one(".location, [class*='location']")

        listings.append({{
            "title": title_el.get_text(strip=True) if title_el else None,
            "price": price_el.get_text(strip=True) if price_el else None,
            "location": loc_el.get_text(strip=True) if loc_el else None,
            "url": title_el["href"] if title_el and title_el.has_attr("href") else "{url}",
            "category": "misc",
            "posted_at": datetime.utcnow().isoformat(),
        }})

    return listings
'''

    os.makedirs(SCRAPERS_DIR, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(template)

    return filename
