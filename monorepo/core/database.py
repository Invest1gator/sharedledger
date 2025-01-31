from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
from pathlib import Path
# Load environment variables from .env file
load_dotenv(dotenv_path='C:\\Users\\sek\\shared-ledger\\.env')

# Debug: Print the DATABASE_URL to verify it's loaded
print("DATABASE_URL:", os.getenv('DATABASE_URL'))

# Create the SQLAlchemy engine
engine = create_engine(os.getenv('DATABASE_URL'))
# Test the connection

with engine.connect() as connection:
    print("Database connection successful!")

# Session yönetimi
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy Base Model
Base = declarative_base()

# Veritabanı Bağlantı Dependency'si (FastAPI için)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
