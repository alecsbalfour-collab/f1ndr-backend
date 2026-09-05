import pytest
from f1ndr.unifiers.listing_unifier import unify_listing

def test_unify_listing_basic():
    raw = {
        "title": "Toyota Corolla",
        "price": 8000,
        "platform": "kijiji",
        "url": "http://example.com",
        "images": ["img.jpg"],
        "location": "Calgary",
        "posted_at": "2026-01-03"
    }

    unified = unify_listing(raw)

    assert unified["title"] == "Toyota Corolla"
    assert unified["platform"] == "kijiji"
    assert unified["price"] == 8000
    assert "raw" in unified

def test_unify_listing_missing_fields():
    raw = {
        "title": "Unknown Car",
        "platform": "craigslist",
        "url": "http://example.com"
    }

    unified = unify_listing(raw)

    assert unified["title"] == "Unknown Car"
    assert unified["platform"] == "craigslist"
    assert unified["price"] is None or unified["price"] == raw.get("price")
    assert "raw" in unified
