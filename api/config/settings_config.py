from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database
    MONGO_URI: str

    # JWT / Security
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    # App Environment
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "info"

    # App Metadata
    APP_NAME: str = "F1NDR API"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache
def get_settings() -> Settings:
    return Settings()
