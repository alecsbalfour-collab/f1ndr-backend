# f1ndr-backend/trinn/config/enrich_config.py
"""
Config for TRINN enrich stage.
"""

def get_enrich_config() -> dict:
    return {
        "enabled": True,
        "max_batch_size": 100,
    }
