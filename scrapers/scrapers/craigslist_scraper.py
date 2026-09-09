from typing import Dict, List
from bs4 import BeautifulSoup

from scrapers.base_scraper import BaseScraper

BASE_URL = "https://calgary.craigslist.org/search/cta"


class CraigslistScraper(BaseScraper):
    source_name = "craigslist"

    def _run_internal(self) -> List[Dict[str, str]]:
        html = self.fetch_html(BASE_URL, wait_selector=".result-row")
        if not html:
            return []
        return self.parse(html)

    def parse(self, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.select(".result-row")

        listings = []
        for row in rows:
            title_el = row.select_one(".result-title")
            price_el = row.select_one(".result-price")
            link_el = row.select_one("a")

            if not title_el or not price_el or not link_el:
                continue

            listings.append({
                "title": title_el.get_text(strip=True),
                "price": price_el.get_text(strip=True),
                "url": link_el.get("href", "")
            })

        return listings


def run() -> Dict:
    scraper = CraigslistScraper()
    return scraper.run()
