from pathlib import Path
from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / '.env')


class DBConfig(Config):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str


class Settings(BaseSettings):
    API_V1_PREFIX: str = '/api/v1'
    DB: DBConfig = DBConfig()
    DATABASE_URL: ClassVar[str] = f'postgresql+asyncpg://{DB.DB_USER}:{DB.DB_PASS}@localhost/{DB.DB_NAME}'


settings = Settings()
