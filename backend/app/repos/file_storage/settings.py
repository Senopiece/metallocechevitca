from pydantic_settings import BaseSettings, SettingsConfigDict


class MinIOSettings(BaseSettings):
    access_key: str
    secret_key: str
    endpoint: str
    bucket_name: str

    model_config = SettingsConfigDict(env_file=".env", env_prefix="MINIO_")


settings = MinIOSettings()
