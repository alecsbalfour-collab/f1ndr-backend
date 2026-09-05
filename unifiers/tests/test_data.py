# f1ndr-backend/unifiers/tests/test_data.py
from unifiers.data.unifier_data import build_unified_listing


def test_build_unified_listing():
    transformed = {"id": 1, "title": "Test", "price": 10, "location": "Calgary", "canonical_source": "Kijiji"}
    unified = build_unified_listing(transformed)
    assert unified["id"] == 1
    assert unified["platform"] == "kijiji"
