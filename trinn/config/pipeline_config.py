"""
Pipeline configuration for trinn.
Defines which steps each pipeline uses.
"""

def pipeline_config():
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
