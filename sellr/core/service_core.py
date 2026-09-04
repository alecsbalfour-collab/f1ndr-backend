"""
sellr service layer.
"""

from sellr.data.listing_data import listing_rules
from sellr.data.update_data import update_rules
from sellr.data.remove_data import remove_rules

from sellr.utils.listing_utils import apply_listing_rules
from sellr.utils.update_utils import apply_update_rules
from sellr.utils.remove_utils import apply_remove_rules

from sellr.db.mongo_client_sellr import SellrMongoClient
from sellr.db.listing_repo import ListingRepo
from sellr.db.update_repo import UpdateRepo
from sellr.db.remove_repo import RemoveRepo


class SellrService:
    def __init__(self):
        client = SellrMongoClient()
        self.listing_repo = ListingRepo(client)
        self.update_repo = UpdateRepo(client)
        self.remove_repo = RemoveRepo(client)

    def create_listing(self, payload: dict):
        rules = listing_rules()
        output = apply_listing_rules(payload, rules)
        return self.listing_repo.log(payload, output)

    def update_listing(self, payload: dict):
        rules = update_rules()
        output = apply_update_rules(payload, rules)
        return self.update_repo.log(payload, output)

    def remove_listing(self, payload: dict):
        rules = remove_rules()
        output = apply_remove_rules(payload, rules)
        return self.remove_repo.log(payload, output)
