"""
Rules for creating listings.
"""

def listing_rules():
    return {
        "strip_whitespace": True,
        "require_title": True,
        "require_price": True,
        "default_status": "active"
    }
