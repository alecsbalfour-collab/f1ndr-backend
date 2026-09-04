"""
Validation helpers for f1ndr.
"""

def is_valid_listing(listing: dict):
    return bool(listing.get("title")) and bool(listing.get("url"))
