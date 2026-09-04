"""
lisTr service layer.
"""

from listr.data.post_data import post_rules
from listr.data.validate_data import validate_rules
from listr.utils.post_utils import apply_post_rules
from listr.utils.validate_utils import apply_validate_rules
from listr.db.post_repo import PostRepo
from listr.db.validate_repo import ValidateRepo
from listr.db.mongo_client_listr import LisTrMongoClient


class LisTrService:
    def __init__(self):
        client = LisTrMongoClient()
        self.post_repo = PostRepo(client)
        self.validate_repo = ValidateRepo(client)

    def post(self, payload: dict):
        rules = post_rules()
        output = apply_post_rules(payload, rules)
        return self.post_repo.log(payload, output)

    def validate(self, payload: dict):
        rules = validate_rules()
        output = apply_validate_rules(payload, rules)
        return self.validate_repo.log(payload, output)

    def delete(self, payload: dict):
        return {"status": "deleted", "input": payload}

    def update(self, payload: dict):
        return {"status": "updated", "input": payload}
