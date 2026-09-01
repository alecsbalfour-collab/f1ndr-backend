import requests
from bs4 import BeautifulSoup

class KijijiScraper:
    BASE_URL = "https://www.kijiji.ca/b-search.html"

    def scrape(self, query: str):
        params = {"q": query}
        response = requests.get(self.BASE_URL, params=params, headers=self.headers())

        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        results = []

        for item in soup.select(".search-item"):
            title = item.select_one(".title").get_text(strip=True)
            price = item.select_one(".price").get_text(strip=True)
            url = "https://www.kijiji.ca" + item.select_one("a")["href"]

            results.append({
                "id": url.split("/")[-1],
                "title": title,
                "price": self.parse_price(price),
                "platform": "kijiji",
                "url": url,
            })

        return results

    def parse_price(self, price):
        try:
            return float(price.replace("$", "").replace(",", ""))
        except:
            return 0.0

    def headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
