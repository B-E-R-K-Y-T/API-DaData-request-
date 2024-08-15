from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_KEY: str
    SECRET_KEY: str
    BASE_URL: str

    model_config = SettingsConfigDict(env_file=f"./.env")


settings = Settings()  # type: ignore
