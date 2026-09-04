"""
Registry of available pipelines in trinn.
Each pipeline is a dict describing its steps.
"""

from typing import Dict, Any


def pipeline_registry() -> Dict[str, Any]:
    return {
        "default": {
            "steps": ["normalize", "transform", "enrich"],
            "description": "Standard trinn pipeline",
        },
        "normalize_only": {
            "steps": ["normalize"],
            "description": "Key/value normalization only",
        },
        "transform_only": {
            "steps": ["transform"],
            "description": "Basic transformation only",
        },
        "enrich_only": {
            "steps": ["enrich"],
            "description": "Metadata enrichment only",
        },
    }
