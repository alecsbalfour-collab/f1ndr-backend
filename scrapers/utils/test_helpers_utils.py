import pytest
from scrapers.utils.test_helpers_utils import safe_get

def test_safe_get_existing_key():
    data = {"a": 1}
    assert safe_get(data, "a") == 1

def test_safe_get_missing_key():
    data = {"a": 1}
    assert safe_get(data, "b") is None
