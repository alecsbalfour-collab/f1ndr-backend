"""
Interfaces for lisTr.
"""

class PostingInterface:
    def post(self, payload: dict):
        raise NotImplementedError

    def validate(self, payload: dict):
        raise NotImplementedError
