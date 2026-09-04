import logging
import logging.config


def configure_logging(settings):
    log_format = (
        '{"level": "%(levelname)s", "time": "%(asctime)s", '
        '"logger": "%(name)s", "message": "%(message)s"}'
        if settings.log_json
        else "%(levelname)s | %(asctime)s | %(name)s | %(message)s"
    )

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {"format": log_format},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            }
        },
        "loggers": {
            "api": {
                "handlers": ["console"],
                "level": settings.log_level,
                "propagate": False,
            }
        },
    }

    logging.config.dictConfig(logging_config)
