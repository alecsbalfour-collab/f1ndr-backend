from f1ndr.processors.html_processor import HtmlProcessor
from bs4 import BeautifulSoup

def test_html_processor_extract():
    processor = HtmlProcessor()
    dom = BeautifulSoup("<a href='/item'>Item</a>", "html.parser")
    listings = processor.extract_listings(dom)
    assert len(listings) >= 1
    assert listings[0]["title"] == "Item"
