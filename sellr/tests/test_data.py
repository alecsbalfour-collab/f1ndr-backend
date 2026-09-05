import pytest
from sellr.data.listing_data import normalize_listing, validate_listing

def test_normalize_listing():
    raw = {"title": "Bike", "price": 100}
    listing = normalize_listing(raw)
    assert listing["title"] == "Bike"
    assert listing["price"] == 100

def test_validate_listing():
    assert validate_listing({"title": "Bike", "price": 100}) is True
    assert validate_listing({"title": "", "price": 100}) is False
