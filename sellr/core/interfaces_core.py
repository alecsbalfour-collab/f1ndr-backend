"""
Interfaces for sellr.
"""

class SellingInterface:
    def create_listing(self, payload: dict):
        raise NotImplementedError

    def update_listing(self, payload: dict):
        raise NotImplementedError

    def remove_listing(self, payload: dict):
        raise NotImplementedError
