"""
Tests for watchr.utils.
"""

from watchr.utils.diff_utils import diff_dict
from watchr.utils.routing_utils import resolve_route
from watchr.utils.dict_utils import merge_dicts


def test_diff_dict():
    old = {"price": 10, "title": "Bike"}
    new = {"price": 12, "title": "Bike"}

    diff = diff_dict(old, new)

    assert "price" in diff
    assert diff["price"]["old"] == 10
    assert diff["price"]["new"] == 12
    assert "title" not in diff


def test_resolve_route():
    routing = {"new_listing": "f1ndr.refresh"}
    assert resolve_route("new_listing", routing) == "f1ndr.refresh"
    assert resolve_route("unknown", routing) == "unknown.route"


def test_merge_dicts():
    a = {"x": 1}
    b = {"y": 2}
    merged = merge_dicts(a, b)

    assert merged["x"] == 1
    assert merged["y"] == 2
