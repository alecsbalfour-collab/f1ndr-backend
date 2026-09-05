"""
Config for listing updates.
"""

def get_update_config() -> dict:
    return {
        "max_update_batch": 50,
        "allow_partial_updates": True,
    }
