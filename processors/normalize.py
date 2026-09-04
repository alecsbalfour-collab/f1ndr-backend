from .config.normalize_config import NormalizeConfig
from .core.normalize_core import NormalizeCore
from .core.base_processor import BaseProcessor
from .db.normalize_db import NormalizeDB


class NormalizeProcessor(BaseProcessor):
    def __init__(
        self,
        config: NormalizeConfig | None = None,
        db: NormalizeDB | None = None
    ):
        config = config or NormalizeConfig()
        core = NormalizeCore(config)
        db = db or NormalizeDB()

        super().__init__(config=config, core=core, db=db)

    def run(self, text: str) -> str:
        self.validate(text)
        normalized = self.core.process(text)
        self.db.save(text, normalized)
        return normalized
