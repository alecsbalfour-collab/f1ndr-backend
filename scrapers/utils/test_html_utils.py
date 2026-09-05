import pytest
from scrapers.utils.html_utils import clean_text

def test_clean_text_basic():
    assert clean_text("  hello  ") == "hello"

def test_clean_text_none():
    assert clean_text(None) is None
