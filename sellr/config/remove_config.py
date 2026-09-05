"""
Config for listing removal.
"""

def get_remove_config() -> dict:
    return {
        "allow_bulk_remove": True,
        "max_remove_batch": 100,
    }
