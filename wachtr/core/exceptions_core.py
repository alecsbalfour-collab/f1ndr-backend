"""
Custom exceptions for watchr core.
"""


class WatchrError(Exception):
    """Base watcher/trigger exception."""
    pass


class UnknownEventError(WatchrError):
    """Raised when an unsupported event is triggered."""
    def __init__(self, event: str):
        super().__init__(f"Unknown event type: {event}")
