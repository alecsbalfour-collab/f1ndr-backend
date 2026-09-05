"""
Scraper Template for f1ndr_backend
All scrapers follow this exact structure.
"""

import traceback
import requests
from bs4 import BeautifulSoup


def fetch_html(url: str) -> str:
    """
    Fetch raw HTML from a URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception:
        return None


def parse_html(html: str) -> list:
    """
    Parse HTML and extract raw listing dicts.
    This function MUST return a list of dicts.
    """
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")

    raw_listings = []

    # Example placeholder — replace with real selectors
    for item in soup.select(".listing"):
        raw_listings.append({
            "title": item.select_one(".title").get_text(strip=True) if item.select_one(".title") else None,
            "price": item.select_one(".price").get_text(strip=True) if item.select_one(".price") else None,
            "url": item.select_one("a")["href"] if item.select_one("a") else None,
            "image": item.select_one("img")["src"] if item.select_one("img") else None,
            "location": item.select_one(".location").get_text(strip=True) if item.select_one(".location") else None,
            "posted_at": None,  # fill in if available
            "platform": "template",
        })

    return raw_listings


def run(query: str = None) -> dict:
    """
    Main scraper entry point.
    MUST return a dict with:
        - success: bool
        - listings: list
        - error: str or None
    """

    try:
        url = build_url(query)
        html = fetch_html(url)
        listings = parse_html(html)

        return {
            "success": True,
            "listings": listings,
            "error": None,
        }

    except Exception as e:
        return {
            "success": False,
            "listings": [],
            "error": str(e),
        }


def build_url(query: str) -> str:
    """
    Build the search URL for the scraper.
    Every scraper implements its own version.
    """
    base = "https://example.com/search?q="
    return f"{base}{query or ''}"
