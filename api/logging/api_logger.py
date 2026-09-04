import logging

def get_api_logger():
    """
    Central API logger used across middleware, controllers, and backend.
    """
    logger = logging.getLogger("f1ndr_api")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
