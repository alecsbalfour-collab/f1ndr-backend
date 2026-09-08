import logging
class SchedulerLoggerUtils:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("scheduler")

scheduler_logger_utils = SchedulerLoggerUtils()
