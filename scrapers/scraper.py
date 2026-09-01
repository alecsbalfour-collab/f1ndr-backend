import random
import time
import requests

class BaseScraper:
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64)",
    ]

    PROXIES = []  # e.g. ["http://user:pass@host:port", ...]

    def get_headers(self):
        return {
            "User-Agent": random.choice(self.USER_AGENTS),
            "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8",
        }

    def get_proxy(self):
        if not self.PROXIES:
            return None
        return {"http": random.choice(self.PROXIES), "https": random.choice(self.PROXIES)}

    def safe_get(self, url, **kwargs):
        for attempt in range(3):
            try:
                resp = requests.get(
                    url,
                    headers=self.get_headers(),
                    proxies=self.get_proxy(),
                    timeout=10,
                    **kwargs,
                )
                if resp.status_code == 200:
                    return resp
            except Exception:
                time.sleep(1)
        return None
