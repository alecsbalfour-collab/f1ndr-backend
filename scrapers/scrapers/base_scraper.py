from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from playwright.sync_api import sync_playwright, Browser
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger("scraper")

class ScraperResult(Dict[str, Any]):
    """
    Standardized scraper result for the entire F1NDR backend.
    """

    @classmethod
    def success(cls, source: str, items: List[Dict[str, Any]]) -> "ScraperResult":
        return cls(source=source, success=True, items=items, error=None)

    @classmethod
    def failure(cls, source: str, error: str) -> "ScraperResult":
        return cls(source=source, success=False, items=[], error=error)


class BaseScraper(ABC):
    """
    Base class for all scrapers.
    Handles Playwright lifecycle, logging, and result normalization.
    """

    source_name: str

    def __init__(self) -> None:
        self._browser: Optional[Browser] = None

    def _launch_browser(self) -> Browser:
        if self._browser is None:
            self._browser = sync_playwright().start().chromium.launch(headless=True)
        return self._browser

    def _close_browser(self) -> None:
        if self._browser is not None:
            try:
                self._browser.close()
            except Exception:
                pass
            self._browser = None

    def fetch_html(self, url: str, wait_selector: Optional[str] = None) -> Optional[str]:
        """
        Centralized JS-rendered fetch using Playwright.
        """
        browser = self._launch_browser()
        page = browser.new_page()
        page.set_extra_http_headers({"User-Agent": "Mozilla/5.0"})

        try:
            page.goto(url, wait_until="networkidle", timeout=45000)
            if wait_selector:
                page.wait_for_selector(wait_selector, timeout=15000)
            return page.content()
        except Exception as e:
            logger.error(f"{self.source_name}: Playwright load failed: {e}")
            return None
        finally:
            page.close()

    @abstractmethod
    def parse(self, html: str) -> List[Dict[str, Any]]:
        """
        Implement site-specific parsing in subclasses.
        """
        raise NotImplementedError

    def run(self) -> ScraperResult:
        """
        Public entrypoint used by scheduler / backend.
        """
        try:
            items = self._run_internal()
            return ScraperResult.success(self.source_name, items)
        except Exception as e:
            logger.exception(f"{self.source_name}: scraper failure: {e}")
            return ScraperResult.failure(self.source_name, str(e))
        finally:
            self._close_browser()

    @abstractmethod
    def _run_internal(self) -> List[Dict[str, Any]]:
        """
        Implement site-specific orchestration (URL building + fetch + parse).
        """
        raise NotImplementedError
