"""
Routing helpers for watchr.
Used to resolve trigger routes and dispatch targets.
"""

from typing import Dict, Any


def resolve_route(event: str, routing_table: Dict[str, str]) -> str:
    """
    Return the route for a given event.
    """
    return routing_table.get(event.lower(), "unknown.route")
