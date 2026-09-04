from bs4 import BeautifulSoup

def to_dom(html: str):
    """
    Convert raw HTML → BeautifulSoup DOM safely.
    """
    if not html:
        return None
    return BeautifulSoup(html, "html.parser")
