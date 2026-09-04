"""
watchr.module
Module entrypoint for the Watchr system.

This module exposes the WatchrController and WatchrService
so other modules (f1ndr, lisTr, sellr, trinn) can interact with
watcher/trigger/event routing without needing internal imports.

Dict‑based architecture. No engines. No processors. No scrapers.
"""

from watchr.core.controller_core import WatchrController
from watchr.core.service_core import WatchrService


class WatchrModule:
    """
    Public-facing module wrapper.
    Other modules import this class to interact with Watchr.
    """

    def __init__(self):
        self.controller = WatchrController()
        self.service = WatchrService()

    # Convenience passthroughs
    def watch(self, key: str, payload: dict):
        return self.controller.watch(key, payload)

    def trigger(self, event: str, data: dict):
        return self.controller.trigger(event, data)

    def subscriptions(self):
        return self.controller.subscriptions()


# Singleton-style instance for global access
watchr = WatchrModule()
