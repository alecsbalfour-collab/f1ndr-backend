import requests

class RealtorScraper:
    BASE_URL = "https://api.realtor.ca/Listing.svc/PropertySearch_Post"

    def scrape(self, query: str):
        payload = {
            "CultureId": 1,
            "ApplicationId": 1,
            "PropertySearchTypeId": 1,
            "Keyword": query,
        }

        resp = requests.post(self.BASE_URL, json=payload, headers=self.headers())
        if resp.status_code != 200:
            return []

        data = resp.json()
        results = []

        for item in data.get("Results", []):
            results.append({
                "id": item.get("Id"),
                "title": item.get("MlsNumber"),
                "price": item.get("Price", 0),
                "platform": "realtor",
                "url": item.get("RelativeDetailsURL"),
                "location": item.get("Property", {}).get("Address", {}).get("AddressText"),
            })

        return results

    def headers(self):
        return {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json",
        }
