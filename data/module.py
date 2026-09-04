# data/module.py
from .listing import ListingDTO

schemas = {
    "ListingDTO": ListingDTO,
}

__all__ = ["schemas", "ListingDTO"]
