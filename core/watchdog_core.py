import logging
class Watchdog:
    def __init__(self, logger, state, history):
        self.logger = logger or logging.getLogger(__name__)
        self.state = state
        self.history = history
        self.logger.info("Watchdog guard operational.")
