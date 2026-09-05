from pydantic import BaseModel
from functools import lru_cache

class Settings(BaseModel):
    """
    Centralized application settings.
    """
    app_name: str = "F1NDR API"
    version: str = "1.0.0"
    environment: str = "development"
    debug: bool = True

@lru_cache
def get_settings() -> Settings:
    """
    Cached settings instance.
    """
    return Settings()
