# utils/test/test_utils.py

from utils.module import normalize
from utils.utils.helpers import clean_text, safe_int

def test_normalize():
    assert normalize("  Hello   World ") == "Hello   World".strip()

def test_clean_text():
    assert clean_text("  BIKE   SALE ") == "bike sale"

def test_safe_int():
    assert safe_int("10") == 10
    assert safe_int("x") is None
