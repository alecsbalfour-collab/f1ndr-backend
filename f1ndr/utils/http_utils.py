import requests

def fetch(url: str, params=None, headers=None, timeout=10):
    """
    Generic HTTP fetch helper.
    Scrapers may use this instead of repeating requests.get().
    """
    try:
        resp = requests.get(
            url,
            params=params or {},
            headers=headers or {"User-Agent": "Mozilla/5.0"},
            timeout=timeout
        )
        if resp.status_code != 200:
            return ""
        return resp.text
    except:
        return ""
