import requests
from bs4 import BeautifulSoup

class RentFasterScraper:
    BASE_URL = "https://www.rentfaster.ca/ab/calgary/search/?keywords="

    def fetch_for_query(self, query: str, filters: dict):
        url = self.BASE_URL + query.replace(" ", "%20")
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

        cards = dom.select(".listing")
        for card in cards:
            title_el = card.select_one(".address")
            price_el = card.select_one(".price")
            link_el = card.select_one("a")

            title = title_el.get_text(strip=True) if title_el else ""
            price = price_el.get_text(strip=True).replace("$", "") if price_el else ""
            url = "https://www.rentfaster.ca" + link_el["href"] if link_el else ""

            listings.append({
                "title": title,
                "price": price,
                "url": url,
                "platform": "rentfaster"
            })

        return listings
