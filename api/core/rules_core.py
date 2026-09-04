from typing import Any, Dict, List

from api.schemas.search_schema import SearchRequest
from scraper.scrapers.kijiji_scraper import fetch_kijiji_results
from scraper.scrapers.marketplace_scraper import fetch_marketplace_results
from scraper.scrapers.autotrader_scraper import fetch_autotrader_results
# ... you can add more imports as you implement each scraper


async def apply_search_rules(payload: SearchRequest) -> List[Dict[str, Any]]:
    """
    Core search orchestration and rule application.

    This is where you:
    - fan out to scrapers
    - normalize results
    - apply ranking / filtering rules
    - merge into a single list
    """

    results: List[Dict[str, Any]] = []

    kijiji = await fetch_kijiji_results(payload)
    marketplace = await fetch_marketplace_results(payload)
    autotrader = await fetch_autotrader_results(payload)

    results.extend(kijiji)
    results.extend(marketplace)
    results.extend(autotrader)

    # Example rule: sort by price ascending when available
    results.sort(key=lambda r: (r.get("price") is None, r.get("price", 0.0)))

    return results
