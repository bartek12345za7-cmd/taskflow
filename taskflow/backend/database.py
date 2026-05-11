from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool, QueuePool
from .config import get_settings

settings = get_settings()
is_production = not settings.DEBUG

ssl_mode = "require" if is_production else "prefer"

engine = create_engine(
    settings.DATABASE_URL,
    poolclass=QueuePool if is_production else NullPool,
    pool_size=10 if is_production else 5,
    max_overflow=20 if is_production else 10,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_timeout=30,
    connect_args={"sslmode": ssl_mode} if is_production else {},
    echo=False,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
