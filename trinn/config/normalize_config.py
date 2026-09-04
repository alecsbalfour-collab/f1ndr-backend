"""
Configuration for normalization rules.
"""

def normalize_config():
    return {
        "key_case": "lower",
        "trim_strings": True,
        "collapse_spaces": True,
        "remove_special_chars": False,
    }
