import requests
from bs4 import BeautifulSoup

class RentfasterScraper:
    BASE_URL = "https://www.rentfaster.ca/ab/calgary/rentals/"

    def scrape(self, query: str):
        params = {"search": query}
        resp = requests.get(self.BASE_URL, params=params, headers=self.headers())
        if resp.status_code != 200:
            return []

        soup = BeautifulSoup(resp.text, "html.parser")
        results = []

        for item in soup.select(".listing"):
            title_el = item.select_one(".listing-title")
            price_el = item.select_one(".listing-price")
            link_el = item.select_one("a")

            if not title_el or not link_el:
                continue

            title = title_el.get_text(strip=True)
            price = self.parse_price(price_el.get_text(strip=True)) if price_el else 0
            url = "https://www.rentfaster.ca" + link_el["href"]

            results.append({
                "id": url.split("/")[-1],
                "title": title,
                "price": price,
                "platform": "rentfaster",
                "url": url,
            })

        return results

    def parse_price(self, text: str):
        try:
            return float(text.replace("$", "").replace(",", "").split()[0])
        except:
            return 0.0

    def headers(self):
        return {"User-Agent": "Mozilla/5.0"}
