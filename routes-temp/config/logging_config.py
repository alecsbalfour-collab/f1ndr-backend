import logging
from logging.config import dictConfig

def setup_logging() -> None:
    """
    Configure application-wide logging using dictConfig.
    """
    dictConfig({
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["console"],
        },
    })

    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
