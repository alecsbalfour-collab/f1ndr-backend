from abc import ABC, abstractmethod

class ScraperInterface(ABC):
    """Base interface for all scrapers."""

    @abstractmethod
    def scrape(self, query: str):
        """Scrape listings based on a query."""
        pass
