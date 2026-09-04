"""
f1ndr module
Public entrypoint for all search operations.
"""

from f1ndr.core.controller_core import F1ndrController


class f1ndr:
    """
    Main interface for external modules:
    - lisTr
    - sellr
    - watchr
    - frontend
    """

    controller = F1ndrController()

    @staticmethod
    def search(query: str, sources=None, filters=None):
        """
        Public search function.

        Example:
            f1ndr.search("mountain bike", ["kijiji", "facebook"])
        """
        payload = {
            "query": query,
            "sources": sources or ["kijiji"],
            "filters": filters or {}
        }

        return f1ndr.controller.search(payload)
