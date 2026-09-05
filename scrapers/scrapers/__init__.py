"""
Scrapers package.

This namespace contains all scraper modules, including:
- individual platform scrapers (kijiji, craigslist, autotrader, etc.)
- the scraper template
- shared scraper utilities
- scraper orchestrator (module.py)

Scrapers are responsible for fetching raw listing data from external platforms
and returning standardized dict structures for pipelines and unifiers.
"""
