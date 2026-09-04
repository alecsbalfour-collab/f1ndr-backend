import requests
from bs4 import BeautifulSoup

class EbayScraper:
    BASE_URL = "https://www.ebay.ca/sch/i.html?_nkw="

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

        cards = dom.select(".s-item")
        for card in cards:
            title_el = card.select_one(".s-item__title")
            price_el = card.select_one(".s-item__price")
            link_el = card.select_one("a.s-item__link")

            title = title_el.get_text(strip=True) if title_el else ""
            price = price_el.get_text(strip=True).replace("$", "") if price_el else ""
            url = link_el["href"] if link_el and link_el.has_attr("href") else ""

            listings.append({
                "title": title,
                "price": price,
                "url": url,
                "platform": "ebay"
            })

        return listings
