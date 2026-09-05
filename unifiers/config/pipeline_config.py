# f1ndr-backend/unifiers/config/pipeline_config.py
"""
Config for Unifiers pipeline orchestration.
"""

def get_pipeline_config() -> dict:
    return {
        "stages": ["normalize", "transform"],
        "async": True,
    }
