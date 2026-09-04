"""
Formatting utilities for watchr.
Used to format event logs, watcher output, and subscription entries.
"""

from typing import Dict, Any


def format_event_log(event: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "event": event.lower(),
        "data": data,
        "formatted": True,
    }


def format_subscription(user_id: str, event: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "user_id": user_id,
        "event": event.lower(),
        "payload": payload,
        "status": "active",
    }
