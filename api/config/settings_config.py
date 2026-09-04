from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    api_name: str = Field(default="f1ndr Backend")
    api_version: str = Field(default="1.0.0")

    api_host: str = Field(default="0.0.0.0")
    api_port: int = Field(default=8000)

    log_level: str = Field(default="INFO")
    log_json: bool = Field(default=True)

    cors_allow_origins: list[str] = Field(default=["*"])
    cors_allow_methods: list[str] = Field(default=["GET", "POST", "OPTIONS"])
    cors_allow_headers: list[str] = Field(default=["*"])

    api_key_header_name: str = Field(default="X-API-Key")
    api_key_value: str | None = Field(default=None)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
