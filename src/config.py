from pydantic import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    API_KEY: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=f"./.env")
