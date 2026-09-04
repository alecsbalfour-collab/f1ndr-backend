"""
Module-level settings for watchr.
General configuration flags and options.
"""

def watchr_settings():
    return {
        "enabled": True,
        "log_events": True,
        "max_subscriptions_per_user": 50,
        "allow_custom_intervals": False,
    }
