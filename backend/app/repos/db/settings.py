from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    milvus_uri: AnyUrl

    model_config = SettingsConfigDict(env_file=".env")


settings = DBSettings()
