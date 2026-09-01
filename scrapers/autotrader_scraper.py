import requests

class AutotraderScraper:
    BASE_URL = "https://www.autotrader.ca/api/vehicles"

    def scrape(self, query: str):
        params = {"keyword": query}
        response = requests.get(self.BASE_URL, params=params, headers=self.headers())

        if response.status_code != 200:
            return []

        data = response.json()
        results = []

        for item in data.get("results", []):
            results.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "price": item.get("price"),
                "platform": "autotrader",
                "url": item.get("url"),
            })

        return results

    def headers(self):
        return {
            "User-Agent": "Mozilla/5.0"
        }
