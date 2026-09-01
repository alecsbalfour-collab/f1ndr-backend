import requests
from bs4 import BeautifulSoup

class CraigslistScraper:
    BASE_URL = "https://www.craigslist.org/search/sss"

    def scrape(self, query: str):
        params = {"query": query}
        response = requests.get(self.BASE_URL, params=params, headers=self.headers())

        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        results = []

        for item in soup.select(".result-row"):
            title = item.select_one(".result-title").get_text(strip=True)
            price = item.select_one(".result-price")
            url = item.select_one(".result-title")["href"]

            results.append({
                "id": item["data-pid"],
                "title": title,
                "price": float(price.get_text(strip=True).replace("$", "")) if price else 0,
                "platform": "craigslist",
                "url": url,
            })

        return results

    def headers(self):
        return {
            "User-Agent": "Mozilla/5.0"
        }
