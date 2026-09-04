"""
Configuration for transformation rules.
"""

def transform_config():
    return {
        "strip_whitespace": True,
        "lowercase_keys": True,
        "convert_empty_to_none": True,
        "max_length_trim": 500,   # optional safety trim
    }
