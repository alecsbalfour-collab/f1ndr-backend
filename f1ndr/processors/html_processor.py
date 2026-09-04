from bs4 import BeautifulSoup

class HtmlProcessor:
    """
    Generic HTML processor for marketplace listings.
    Scrapers pass raw HTML → processor extracts listing dicts.
    """

    def extract_listings(self, dom):
        """
        This is a generic fallback processor.
        Specific scrapers override extraction logic inside their own file.
        """
        listings = []

        # Generic fallback: find any <a> with text and href
        for link in dom.select("a"):
            title = link.get_text(strip=True)
            href = link.get("href", "")

            if title and href:
                listings.append({
                    "title": title,
                    "price": "",
                    "url": href,
                    "platform": "unknown"
                })

        return listings
