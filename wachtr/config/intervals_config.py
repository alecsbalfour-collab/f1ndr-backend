# f1ndr-backend/watchr/config/intervals_config.py
"""
Interval configuration for Watchr.
"""

def get_intervals_config() -> dict:
    return {
        "poll_interval_seconds": 30,
        "max_backoff_seconds": 300,
    }
