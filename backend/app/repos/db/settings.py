from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    milvus_uri: AnyUrl = AnyUrl("http://localhost:19530")
    flush_every_time: bool = False

    model_config = SettingsConfigDict(env_file=".env")


settings = DBSettings()
