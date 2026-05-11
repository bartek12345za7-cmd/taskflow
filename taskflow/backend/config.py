from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "TaskFlow API"
    DEBUG: bool = False
    
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/taskflow"
    
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    CORS_ORIGINS: list[str] = []
    
    RATE_LIMIT_PER_MINUTE: int = 60
    
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
