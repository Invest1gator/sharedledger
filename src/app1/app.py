# appName/src/app.py
from monorepo.core.ledgers.model import LedgerEntry
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.

# Ortam değişkeninden DATABASE_URL al
load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

# Now you can use the `LedgerEntry` model here
ledger_entries = session.query(LedgerEntry).filter_by(owner_id="user123").all()
