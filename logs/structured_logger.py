import logging
import json
import sys

class StructuredLogger:
    def __init__(self, name="f1ndr_backend"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, message, **kwargs):
        self.logger.info(json.dumps({"message": message, **kwargs}))

    def error(self, message, **kwargs):
        self.logger.error(json.dumps({"message": message, **kwargs}))

# Expose the expected active class reference hooks
structured_logger = StructuredLogger()
StructuredLogger.logger = structured_logger.logger
