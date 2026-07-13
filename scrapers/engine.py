import random
import time
import requests
from requests.exceptions import RequestException

# Optional proxy list (leave empty if not using proxies)
PROXIES = [
    # "http://user:pass@proxy1:port",
    # "http://user:pass@proxy2:port",
]

# Rotating user agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Safari/605.1.15",

    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0 Safari/537.36",

    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
]

DEFAULT_TIMEOUT = 10
MAX_RETRIES = 5
RETRY_BACKOFF = 1.5  # seconds


def get_proxy():
    """Return a random proxy or None."""
    if not PROXIES:
        return None
    return {"http": random.choice(PROXIES), "https": random.choice(PROXIES)}


def get_headers():
    """Return randomized headers."""
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "en-US,en;q=0