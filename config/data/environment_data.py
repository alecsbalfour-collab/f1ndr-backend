# config/data/environment.py

import os

ENV = {
    "APP_NAME": "f1ndr-backend",
    "APP_VERSION": "1.0.0",
    "ENVIRONMENT": os.getenv("F1NDR_ENV", "development"),

    "DB_HOST": os.getenv("F1NDR_DB_HOST", "localhost"),
    "DB_PORT": int(os.getenv("F1NDR_DB_PORT", "5432")),
    "DB_USER": os.getenv("F1NDR_DB_USER", "f1ndr"),
    "DB_PASS": os.getenv("F1NDR_DB_PASS", "password"),
    "DB_NAME": os.getenv("F1NDR_DB_NAME", "f1ndr"),

    "LOG_LEVEL": os.getenv("F1NDR_LOG_LEVEL", "INFO"),
    "LOG_FORMAT": "%(asctime)s [%(levelname)s] %(message)s",

    "SEC_SANDBOX": os.getenv("F1NDR_SEC_SANDBOX", "true").lower() == "true",
    "SEC_MAX_REQ": int(os.getenv("F1NDR_SEC_MAX_REQ", "5242880")),  # 5MB

    "PERF_CACHE": os.getenv("F1NDR_PERF_CACHE", "true").lower() == "true",
    "PERF_WORKERS": int(os.getenv("F1NDR_PERF_WORKERS", "4"))
}
