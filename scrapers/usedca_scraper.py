import requests
from bs4 import BeautifulSoup

class UsedCaScraper:
    BASE_URL = "https://www.used.ca/search/"

    def scrape(self, query: str):
        url = self.BASE_URL + query.replace(" ", "%20")
        resp = requests.get(url, headers=self.headers())

        if resp.status_code != 200:
            return []

        soup = BeautifulSoup(resp.text, "html.parser")
        results = []

        for item in soup.select(".result"):
            title_el = item.select_one(".title")
            price_el = item.select_one(".price")
            link_el = item.select_one("a")

            if not title_el or not link_el:
                continue

            title = title_el.get_text(strip=True)
            price = self.parse_price(price_el.get_text(strip=True)) if price_el else 0
            url = link_el["href"]

            results.append({
                "id": url.split("/")[-1],
                "title": title,
                "price": price,
                "platform": "usedca",
                "url": url,
            })

        return results

    def parse_price(self, text: str):
        try:
            return float(
                text.replace("$", "")
                    .replace(",", "")
                    .split()[0]
            )
        except Exception:
            return 0.0

    def headers(self):
        return {
            "User-Agent": "Mozilla/5.0"
        }
