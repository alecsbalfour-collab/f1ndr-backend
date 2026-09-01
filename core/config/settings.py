import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "f1ndr Backend"
    VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    # Scraper settings
    SCRAPER_TIMEOUT = int(os.getenv("SCRAPER_TIMEOUT", 10))
    SCRAPER_USER_AGENT = os.getenv(
        "SCRAPER_USER_AGENT",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    )

    # Pipeline settings
    PIPELINE_ENABLED = True

settings = Settings()
