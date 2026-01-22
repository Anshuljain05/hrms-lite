import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use PostgreSQL on Railway, SQLite locally
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hrms.db")

# Handle PostgreSQL URL format
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Connection pooling settings for production
connect_args = {}
pool_settings = {}

if "sqlite" in DATABASE_URL:
    connect_args = {"check_same_thread": False}
    pool_settings = {"connect_args": connect_args}
else:
    pool_settings = {
        "pool_size": 5,
        "max_overflow": 10,
        "pool_pre_ping": True,
        "pool_recycle": 3600
    }

engine = create_engine(
    DATABASE_URL,
    **pool_settings
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
