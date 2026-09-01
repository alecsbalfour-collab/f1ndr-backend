import requests

class MarketplaceCaScraper:
    BASE_URL = "https://www.marketplace.ca/api/search"

    def scrape(self, query: str):
        params = {"q": query}
        response = requests.get(self.BASE_URL, params=params, headers=self.headers())

        if response.status_code != 200:
            return []

        data = response.json()
        results = []

        for item in data.get("items", []):
            results.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "price": item.get("price"),
                "platform": "marketplace_ca",
                "url": item.get("url"),
            })

        return results

    def headers(self):
        return {
            "User-Agent": "Mozilla/5.0"
        }
