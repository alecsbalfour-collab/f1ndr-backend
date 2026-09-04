"""
Tests for WatchrService.
"""

from watchr.core.service_core import WatchrService
from watchr.core.exceptions_core import UnknownEventError


def test_handle_watch_event():
    service = WatchrService()
    result = service.handle_watch_event("match_found", {"id": "abc"})

    assert result["watch_key"] == "match_found"
    assert result["received"]["id"] == "abc"
    assert result["status"] == "watch_event_processed"


def test_trigger_event_valid():
    service = WatchrService()
    result = service.trigger_event("listing_update", {"id": "xyz"})

    assert result["event"] == "listing_update"
    assert result["data"]["id"] == "xyz"
    assert result["status"] == "trigger_dispatched"


def test_trigger_event_invalid():
    service = WatchrService()
    try:
        service.trigger_event("invalid_event", {})
        assert False, "Expected UnknownEventError"
    except UnknownEventError:
        assert True
