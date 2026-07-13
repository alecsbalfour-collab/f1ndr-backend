import requests
from bs4 import BeautifulSoup

SEARCH_QUERIES = [
    "classifieds calgary",
    "used cars marketplace",
    "rental listings calgary",
    "local buy and sell",
    "online marketplace canada",
]


def search_google(query: string):
    # Placeholder: in production you'd use a real search API.
    # For now, this is a stub you can later wire to SerpAPI, etc.
    return []


def find_candidate_sites():
    candidates = set()

    for q in SEARCH_QUERIES:
        results = search_google(q)
        for r in results:
            url = r.get("url")
            if not url:
                continue
            if any(x in url for x in ["facebook.com", "kijiji.ca", "craigslist.org"]):
                continue
            candidates.add(url)

    return list(candidates)


def fetch_html(url: str):
    try:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if resp.status_code != 200:
            return None
        return resp.text
    except Exception:
        return None


def get_dom(url: str):
    html = fetch_html(url)
    if not html:
        return None
    return BeautifulSoup(html, "html.parser")
