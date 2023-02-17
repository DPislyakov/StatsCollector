import pathlib

from pydantic import AnyHttpUrl, BaseSettings
from typing import List, Optional


ROOT = pathlib.Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    PROJECT_NAME: str = "StatsCollector"
    PROJECT_VERSION: str = "0.0.1"

    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///./dev.db"

    class Config:
        env_file = './.env'
        case_sensitive = True


settings = Settings()
