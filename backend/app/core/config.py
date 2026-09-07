from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


ENV_FILE = Path(__file__).resolve().parents[1] / ".env"


class Settings(BaseSettings):
    ticketmaster_api_key: str
    ticketmaster_base_url: str = "https://app.ticketmaster.com/discovery/v2"

    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")


settings = Settings()