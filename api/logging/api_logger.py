import logging

def get_logger(name: str) -> logging.Logger:
    """
    Unified logger factory for the API layer.
    Ensures consistent formatting and log levels.
    """
    return logging.getLogger(name)

api_logger = get_logger("api")
