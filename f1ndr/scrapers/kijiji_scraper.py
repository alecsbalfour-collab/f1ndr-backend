import requests
from bs4 import BeautifulSoup

class KijijiScraper:
    BASE_URL = "https://www.kijiji.ca/b-search.html"

    def fetch_for_query(self, query: str, filters: dict):
        params = {
            "dc": True,
            "q": query,
        }
        params.update(filters)

        try:
            resp = requests.get(
                self.BASE_URL,
                params=params,
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=10
            )
            if resp.status_code != 200:
                return ""
            return resp.text
        except:
            return ""

    def parse(self, html: str):
        return BeautifulSoup(html, "html.parser")

    def extract(self, dom):
        listings = []

        cards = dom.select(".search-item")
        for card in cards:
            title_el = card.select_one(".title")
            price_el = card.select_one(".price")
            link_el = card.select_one("a")

            title = title_el.get_text(strip=True) if title_el else ""
            price = price_el.get_text(strip=True).replace("$", "") if price_el else ""
            url = (
                "https://www.kijiji.ca" + link_el["href"]
                if link_el and link_el.has_attr("href")
                else ""
            )

            listings.append({
                "title": title,
                "price": price,
                "url": url,
                "platform": "kijiji"
            })

        return listings
