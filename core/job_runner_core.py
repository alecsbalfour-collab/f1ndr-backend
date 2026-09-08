import logging
class JobRunner:
    def __init__(self, metadata, logger, retry_utils):
        self.metadata = metadata
        self.logger = logger or logging.getLogger(__name__)
        self.retry_utils = retry_utils
        self.logger.info("JobRunner engine initialized successfully.")
