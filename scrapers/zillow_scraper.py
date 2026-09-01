import requests

class ZillowScraper:
    BASE_URL = "https://www.zillow.com/search/GetSearchPageState.htm"

    def scrape(self, query: str):
        params = {
            "searchQueryState": f'{{"usersSearchTerm":"{query}"}}',
            "wants": '{"cat1":["listResults"]}',
        }

        resp = requests.get(self.BASE_URL, params=params, headers=self.headers())
        if resp.status_code != 200:
            return []

        try:
            data = resp.json()
        except:
            return []

        results = []
        list_results = (
            data.get("cat1", {})
                .get("searchResults", {})
                .get("listResults", [])
        )

        for item in list_results:
            results.append({
                "id": item.get("zpid"),
                "title": item.get("address"),
                "price": item.get("unformattedPrice", 0),
                "platform": "zillow",
                "url": item.get("detailUrl"),
                "location": item.get("address"),
            })

        return results

    def headers(self):
        return {"User-Agent": "Mozilla/5.0"}
