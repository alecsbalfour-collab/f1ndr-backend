import pytest
from scrapers.utils.test_browser_utils import build_headers

def test_build_headers_returns_dict():
    headers = build_headers()
    assert isinstance(headers, dict)
    assert "User-Agent" in headers
