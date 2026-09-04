import requests
from bs4 import BeautifulSoup

class ZillowScraper:
    BASE_URL = "https://www.zillow.com/homes/for_rent/Calgary-AB_rb/?searchQueryState="

    def fetch_for_query(self, query: str, filters: dict):
        try:
            resp = requests.get(
                self.BASE_URL,
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

        cards = dom.select("article")
        for card in cards:
            title_el = card.select_one("address")
            price_el = card.select_one(".list-card-price")
            link_el = card.select_one("a.list-card-link")

            title = title_el.get_text(strip=True) if title_el else ""
            price = price_el.get_text(strip=True).replace("$", "") if price_el else ""
            url = link_el["href"] if link_el else ""

            listings.append({
                "title": title,
                "price": price,
                "url": url,
                "platform": "zillow"
            })

        return listings
