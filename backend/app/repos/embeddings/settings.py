from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class ClientSettings(BaseSettings):
    url: AnyUrl

    model_config = SettingsConfigDict(env_file=".env", env_prefix="RAY_")


settings = ClientSettings()
