# f1ndr_backend/api/security/api_keys.py

import time
from typing import Optional

# API key store
# You can rotate keys by adding new ones and setting expiry timestamps.
# Expiry = None → never expires.
API_KEYS: dict[str, dict[str, Optional[float]]] = {
    "dev-key": {"expires": None},
    "prod-key-1": {"expires": None},          # active production key
    # Example rotated key:
    # "prod-key-2": {"expires": 1705000000},  # expires at UNIX timestamp
}


def validate_api_key(key: str) -> bool:
    """
    Validates an API key and checks expiry.
    """
    key_data = API_KEYS.get(key)
    if not key_data:
        return False

    expires = key_data.get("expires")

    # If expiry exists and is in the past → invalid
    if expires is not None and time.time() > expires:
        return False

    return True


def rotate_api_key(old_key: str, new_key: str, expires: Optional[float] = None):
    """
    Rotates an API key by disabling the old one and adding a new one.
    """
    if old_key in API_KEYS:
        API_KEYS.pop(old_key)

    API_KEYS[new_key] = {"expires": expires}
