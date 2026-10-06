from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Local AI API"
    app_version: str = "1.0.0"
    environment: str = "development"

    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"


    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )   


@lru_cache
def get_settings() -> Settings:
    return Settings()