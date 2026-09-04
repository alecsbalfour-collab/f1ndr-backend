import logging


class LoggerUtils:
    """
    Enterprise-level logger setup for processors.
    """

    @staticmethod
    def get_logger(name: str = "processors"):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("[%(levelname)s] %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger
