"""
Enrichment rules for trinn.
Defines metadata and computed fields to add.
"""

from typing import Dict, Any


def enrich_rules() -> Dict[str, Any]:
    return {
        "add_timestamp": True,
        "add_enriched_flag": True,
        "add_source_tag": True,
    }
