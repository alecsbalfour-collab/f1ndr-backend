from logs.logging import pipeline_logger as processors_logger


class LoggerUtils:
    def __init__(self):
        self.logger = processors_logger


logger_utils = LoggerUtils()
