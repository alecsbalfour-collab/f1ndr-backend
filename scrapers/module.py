# scrapers/module.py

import asyncio

from scrapers.scrapers.autotrader_scraper import run as run_autotrader
from scrapers.scrapers.craigslist_scraper import run as run_craigslist
from scrapers.scrapers.ebay_scraper import run as run_ebay
from scrapers.scrapers.facebook_scraper import run as run_facebook
from scrapers.scrapers.kijiji_scraper import run as run_kijiji
from scrapers.scrapers.marketplace_scraper import run as run_marketplace
from scrapers.scrapers.rentals_scraper import run as run_rentals
from scrapers.scrapers.rentfaster_scraper import run as run_rentfaster
from scrapers.scrapers.used_scraper import run as run_used
from scrapers.scrapers.usedca_scraper import run as run_usedca
from scrapers.scrapers.realtor_scraper import run as run_realtor
from scrapers.scrapers.zillow_scraper import run as run_zillow


SCRAPERS = {
    "autotrader": run_autotrader,
    "craigslist": run_craigslist,
    "ebay": run_ebay,
    "facebook": run_facebook,
    "kijiji": run_kijiji,
    "marketplace": run_marketplace,
    "rentals": run_rentals,
    "rentfaster": run_rentfaster,
    "used": run_used,
    "usedca": run_usedca,
    "realtor": run_realtor,
    "zillow": run_zillow,
}


async def run_all(query: str):
    tasks = []

    for name, scraper in SCRAPERS.items():
        tasks.append(_run_single(name, scraper, query))

    results = await asyncio.gather(*tasks)

    return {
        "query": query,
        "results": {r["platform"]: r for r in results},
    }


async def _run_single(name: str, scraper_func, query: str):
    try:
        result = await scraper_func(query)
        return {
            "platform": name,
            "success": result.get("success", False),
            "listings": result.get("listings", []),
            "error": result.get("error"),
        }
    except Exception as e:
        return {
            "platform": name,
            "success": False,
            "listings": [],
            "error": str(e),
        }
