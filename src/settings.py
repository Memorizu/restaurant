from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / '.env')


class DBConfig(Config):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str


class Settings(BaseSettings):
    DB: DBConfig = DBConfig()


settings = Settings()
