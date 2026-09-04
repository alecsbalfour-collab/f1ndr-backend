"""
Configuration for enrichment rules.
"""

def enrich_config():
    return {
        "add_timestamp": True,
        "add_enriched_flag": True,
        "add_source_tag": True,
        "source_tag_value": "trinn",
    }
