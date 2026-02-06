import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)

# Database URL from environment or use SQLite locally
# For production, use DATABASE_URL with PostgreSQL connection string
# For development, defaults to SQLite in current directory
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./hrms.db"
)

logger.info(f"Database: {DATABASE_URL.split('@')[0] if '@' in DATABASE_URL else 'SQLite (local)'}")

# Handle PostgreSQL URL format (Railway uses old postgres:// protocol)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    logger.info("Converted postgres:// to postgresql://")

# Connection pooling and engine configuration
connect_args = {}
pool_settings = {}

# SQLite-specific settings
if "sqlite" in DATABASE_URL:
    connect_args = {"check_same_thread": False}
    pool_settings = {"connect_args": connect_args}
    logger.debug("Using SQLite connection settings")
# PostgreSQL and other database settings
else:
    pool_settings = {
        "pool_size": int(os.getenv("DB_POOL_SIZE", 3)),
        "max_overflow": int(os.getenv("DB_MAX_OVERFLOW", 5)),
        "pool_pre_ping": True,  # Verify connections before using
        "pool_recycle": int(os.getenv("DB_POOL_RECYCLE", 600))  # Recycle connections every 10 mins
    }
    logger.debug(f"Using database pool settings: {pool_settings}")

# Create database engine with configuration
engine = create_engine(
    DATABASE_URL,
    **pool_settings,
    echo=os.getenv("SQL_ECHO", "false").lower() == "true"  # Log all SQL statements if enabled
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency function to get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
