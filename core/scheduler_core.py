import logging
class SchedulerCore:
    def __init__(self, config, intervals, state, history, logger, time_utils):
        self.config = config
        self.intervals = intervals
        self.state = state
        self.history = history
        self.logger = logger or logging.getLogger(__name__)
        self.time_utils = time_utils
        self.is_running = False
        self.logger.info("SchedulerCore initialized successfully.")
