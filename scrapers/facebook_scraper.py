import requests

class FacebookScraper:
    BASE_URL = "https://www.facebook.com/marketplace/search/?query="

    def scrape(self, query: str):
        url = self.BASE_URL + query.replace(" ", "%20")
        response = requests.get(url, headers=self.headers())

        if response.status_code != 200:
            return []

        try:
            data = response.json()
        except:
            return []

        results = []

        for item in data.get("data", []):
            results.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "price": item.get("price", 0),
                "platform": "facebook",
                "url": item.get("url"),
            })

        return results

    def headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
        }
