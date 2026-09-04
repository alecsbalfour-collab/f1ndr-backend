"""
Utilities for enrichment operations.
"""

from typing import Dict, Any
from datetime import datetime


def add_timestamp(data: Dict[str, Any]) -> Dict[str, Any]:
    enriched = data.copy()
    enriched["_timestamp"] = datetime.utcnow().isoformat()
    return enriched


def add_enriched_flag(data: Dict[str, Any]) -> Dict[str, Any]:
    enriched = data.copy()
    enriched["_enriched"] = True
    return enriched


def add_source_tag(data: Dict[str, Any], tag: str = "trinn") -> Dict[str, Any]:
    enriched = data.copy()
    enriched["_source"] = tag
    return enriched
