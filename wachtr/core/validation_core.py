"""
Dict‑model validation for watchr.
No Pydantic. No class‑models.
"""

from typing import Dict, Any


def validate_event_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": data.get("id"),
        "type": data.get("type"),
        "payload": data.get("payload", {}),
    }
