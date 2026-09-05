# scrapers/scrapers/ebay_scraper.py

import traceback
import httpx
from bs4 import BeautifulSoup

PLATFORM = "ebay"


async def fetch_html(url: str) -> str | None:
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.text
    except Exception:
        traceback.print_exc()
        return None


def parse_html(html: str) -> list[dict]:
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    listings = []

    # TODO: replace selectors with real eBay structure
    for item in soup.select(".s-item"):
        listings.append({
            "title": item.select_one(".s-item__title").get_text(strip=True) if item.select_one(".s-item__title") else None,
            "price": item.select_one(".s-item__price").get_text(strip=True) if item.select_one(".s-item__price") else None,
            "url": item.select_one("a")["href"] if item.select_one("a") else None,
            "image": item.select_one("img")["src"] if item.select_one("img") else None,
            "location": None,
            "posted_at": None,
            "platform": PLATFORM,
        })

    return listings


def build_url(query: str | None) -> str:
    base = "https://www.ebay.com/sch/i.html?_nkw="
    return f"{base}{query or ''}"


async def run(query: str | None = None) -> dict:
    try:
        url = build_url(query)
        html = await fetch_html(url)
        listings = parse_html(html)

        return {
            "success": True,
            "listings": listings,
            "error": None,
        }
    except Exception as e:
        traceback.print_exc()
        return {
            "success": False,
            "listings": [],
            "error": str(e),
        }
