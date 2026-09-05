from .core.pipeline_core import PipelineCore
from .utils.pipeline_logger_utils import pipeline_logger_utils
from .config.pipeline_config import pipeline_config
from .data.pipeline_data import PIPELINE_DATA
from .db.pipeline_state import pipeline_state


class ingestPipeline:
    def __init__(self):
        self.core = PipelineCore(
            config=pipeline_config,
            data=PIPELINE_DATA,
            state=pipeline_state,
            logger=pipeline_logger_utils.logger,
        )

    def run(self, payload: dict) -> dict:
        pipeline_logger_utils.logger.info("Starting ingest pipeline")
        return self.core.process(payload)
