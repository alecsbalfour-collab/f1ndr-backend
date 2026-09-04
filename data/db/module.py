# db/module.py
from .session import get_db_session
from .models import Listing
from .repositories.listing_repository import ListingRepository

db_session = get_db_session
repositories = {
    "ListingRepository": ListingRepository,
}

models = {
    "Listing": Listing,
}

__all__ = ["db_session", "repositories", "models"]
