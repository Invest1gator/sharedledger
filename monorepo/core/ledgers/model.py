from sqlalchemy import Column, Integer, String, Enum as SAEnum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from monorepo.core.ledgers.schemas import BaseLedgerOperation

Base = declarative_base()

class LedgerEntry(Base):
    __tablename__ = "ledger_entries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # We use a string-based Enum type for the operation column
    operation = Column(SAEnum(*[op.value for op in BaseLedgerOperation]), nullable=False)  
    amount = Column(Integer, nullable=False)
    nonce = Column(String, nullable=False, unique=True)
    owner_id = Column(String, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow, nullable=False)