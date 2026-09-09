from typing import Dict, List

from bs4 import BeautifulSoup

from scrapers.base_scraper import BaseScraper

BASE_URL = "https://www.kijiji.ca/b-cars-vehicles/calgary/c27l1700199"


class KijijiScraper(BaseScraper):
    source_name = "kijiji"

    def _run_internal(self) -> List[Dict[str, str]]:
        html = self.fetch_html(BASE_URL, wait_selector=".search-item")
        if not html:
            return []
        return self.parse(html)

    def parse(self, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, "html.parser")
        cards = soup.select(".search-item")

        listings: List[Dict[str, str]] = []
        for card in cards:
            title_el = card.select_one(".title")
            price_el = card.select_one(".price")
            link_el = card.select_one("a")

            if not title_el or not price_el or not link_el:
                continue

            listings.append(
                {
                    "title": title_el.get_text(strip=True),
                    "price": price_el.get_text(strip=True),
                    "url": "https://www.kijiji.ca" + (link_el.get("href") or ""),
                }
            )

        return listings


def run() -> Dict:
    """
    Adapter for existing scheduler / backend call style.
    """
    scraper = KijijiScraper()
    return scraper.run()
