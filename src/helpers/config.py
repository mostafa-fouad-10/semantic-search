from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    embedding_model: str
    top_k: int = 5
    data_path: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


def get_settings() -> Settings:
    return Settings()