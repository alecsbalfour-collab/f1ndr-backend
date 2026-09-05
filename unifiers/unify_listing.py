# f1ndr-backend/unifiers/unify_listing.py
"""
Entry point for listing unification.
"""

from unifiers.module import UnifiersModule


async def unify_listing(mongo_uri: str, payload: dict) -> dict:
    module = UnifiersModule(mongo_uri)
    controller = module.get_controller()
    return await controller.unify(payload)
