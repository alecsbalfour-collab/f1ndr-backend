"""
Tests for WatchrController.
"""

from watchr.core.controller_core import WatchrController


def test_watch_event():
    controller = WatchrController()
    result = controller.watch("price_change", {"id": "123", "old": 10, "new": 12})

    assert result["watch_key"] == "price_change"
    assert result["received"]["id"] == "123"
    assert result["status"] == "watch_event_processed"


def test_trigger_event():
    controller = WatchrController()
    result = controller.trigger("new_listing", {"id": "999", "title": "Bike"})

    assert result["event"] == "new_listing"
    assert result["data"]["id"] == "999"
    assert result["status"] == "trigger_dispatched"
