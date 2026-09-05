import logging
import os
from datetime import datetime

LOG_ROOT = os.path.join(os.getcwd(), "logs")

# Ensure folder structure exists
FOLDERS = [
    "errors",
    "pipelines",
    "scrapers",
    "scheduler",
]

for folder in FOLDERS:
    path = os.path.join(LOG_ROOT, folder)
    os.makedirs(path, exist_ok=True)


def _build_log_path(folder: str, name: str) -> str:
    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{name}_{date}.log"
    return os.path.join(LOG_ROOT, folder, filename)


def get_logger(name: str, folder: str) -> logging.Logger:
    """
    Unified logger factory for F1NDR subsystems.
    Creates a logger that writes to the correct folder:
    - errors/
    - pipelines/
    - scrapers/
    - scheduler/
    """

    logger = logging.getLogger(f"{folder}.{name}")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        log_path = _build_log_path(folder, name)
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


# Convenience shortcuts
error_logger = get_logger("errors", "errors")
pipeline_logger = get_logger("pipelines", "pipelines")
scraper_logger = get_logger("scrapers", "scrapers")
scheduler_logger = get_logger("scheduler", "scheduler")
