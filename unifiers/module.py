# f1ndr-backend/unifiers/module.py
"""
Unifiers module initializer.
Wires repos, services, controller, and configs.
"""

from unifiers.db.mongo_client_unifiers import get_unifiers_client
from unifiers.db.unifier_state import UnifierStateRepo
from unifiers.db.normalize_repo import NormalizeRepo
from unifiers.db.transform_repo import TransformRepo

from unifiers.core.service_core import UnifierService
from unifiers.core.controller_core import UnifierController

from unifiers.config.unifier_config import get_unifier_config
from unifiers.config.pipeline_config import get_pipeline_config
from unifiers.config.normalize_config import get_normalize_config
from unifiers.config.transform_config import get_transform_config


class UnifiersModule:
    def __init__(self, mongo_uri: str):
        self.client = get_unifiers_client(mongo_uri)

        # Repos
        self.state_repo = UnifierStateRepo(self.client)
        self.normalize_repo = NormalizeRepo(self.client)
        self.transform_repo = TransformRepo(self.client)

        # Service
        self.service = UnifierService(
            state_repo=self.state_repo,
            normalize_repo=self.normalize_repo,
            transform_repo=self.transform_repo,
        )

        # Controller
        self.controller = UnifierController(self.service)

        # Configs
        self.unifier_config = get_unifier_config()
        self.pipeline_config = get_pipeline_config()
        self.normalize_config = get_normalize_config()
        self.transform_config = get_transform_config()

    def get_controller(self) -> UnifierController:
        return self.controller
