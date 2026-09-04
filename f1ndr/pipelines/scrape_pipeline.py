"""
Scrape Pipeline
Runs only the scraping + extraction portion.
Useful for debugging scrapers.
"""

from bs4 import BeautifulSoup


class ScrapePipeline:
    def __init__(self, scraper):
        self.scraper = scraper

    def run(self, query: str, filters: dict):
        raw_html = self.scraper.fetch_for_query(query, filters)
        if not raw_html:
            return []

        dom = BeautifulSoup(raw_html, "html.parser")
        return self.scraper.extract(dom)
