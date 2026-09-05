# f1ndr-backend/trinn/module.py
"""
TRINN module initializer.
Wires TRINN repos, services, controllers, and configs.
"""

from trinn.db.mongo_client_trinn import get_trinn_client
from trinn.db.enrich_repo import EnrichRepo
from trinn.db.normalize_repo import NormalizeRepo
from trinn.db.transform_repo import TransformRepo

from trinn.core.service_core import TrinnService
from trinn.core.controller_core import TrinnController

from trinn.config.enrich_config import get_enrich_config
from trinn.config.normalize_config import get_normalize_config
from trinn.config.pipeline_config import get_pipeline_config
from trinn.config.transform_config import get_transform_config


class TrinnModule:
    def __init__(self, mongo_uri: str):
        self.client = get_trinn_client(mongo_uri)

        # Repos
        self.enrich_repo = EnrichRepo(self.client)
        self.normalize_repo = NormalizeRepo(self.client)
        self.transform_repo = TransformRepo(self.client)

        # Service
        self.service = TrinnService(
            enrich_repo=self.enrich_repo,
            normalize_repo=self.normalize_repo,
            transform_repo=self.transform_repo,
        )

        # Controller
        self.controller = TrinnController(self.service)

        # Configs
        self.enrich_config = get_enrich_config()
        self.normalize_config = get_normalize_config()
        self.pipeline_config = get_pipeline_config()
        self.transform_config = get_transform_config()

    def get_controller(self) -> TrinnController:
        return self.controller
