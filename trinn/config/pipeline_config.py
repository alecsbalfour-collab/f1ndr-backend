# f1ndr-backend/trinn/config/pipeline_config.py
"""
Config for TRINN pipeline orchestration.
"""

def get_pipeline_config() -> dict:
    return {
        "stages": ["enrich", "normalize", "transform"],
        "async": True,
    }
