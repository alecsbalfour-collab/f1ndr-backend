import requests
from bs4 import BeautifulSoup

class FacebookScraper:
    BASE_URL = "https://www.facebook.com/marketplace/search/?query="

    def fetch_for_query(self, query: str, filters: dict):
        url = self.BASE_URL + query.replace(" ", "%20")
        try:
            resp = requests.get(
                url,
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

        cards = dom.select("a[href*='/marketplace/item/']")
        for card in cards:
            title = card.get_text(strip=True)
            url = "https://www.facebook.com" + card.get("href", "")

            listings.append({
                "title": title,
                "price": "",
                "url": url,
                "platform": "facebook"
            })

        return listings
