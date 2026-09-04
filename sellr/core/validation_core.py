"""
Validation helpers.
"""

def is_valid_price(price):
    try:
        return float(price) >= 0
    except:
        return False
