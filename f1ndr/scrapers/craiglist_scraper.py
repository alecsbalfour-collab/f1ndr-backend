import requests
from bs4 import BeautifulSoup

class CraigslistScraper:
    BASE_URL = "https://www.craigslist.org/search/sss?query="

    def fetch_for_query(self, query: str, filters: dict):
        url = self.BASE_URL + query.replace(" ", "+")
        try:
            resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            if resp.status_code != 200:
                return ""
            return resp.text
        except:
            return ""

    def parse(self, html: str):
        return BeautifulSoup(html, "html.parser")

    def extract(self, dom):
        listings = []

        for row in dom.select(".result-row"):
            title_el = row.select_one(".result-title")
            price_el = row.select_one(".result-price")

            title = title_el.get_text(strip=True) if title_el else ""
            price = price_el.get_text(strip=True).replace("$", "") if price_el else ""
            url = title_el["href"] if title_el and title_el.has_attr("href") else ""

            listings.append({
                "title": title,
                "price": price,
                "url": url,
                "platform": "craigslist"
            })

        return listings
