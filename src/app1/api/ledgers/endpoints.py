from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from monorepo.core.ledgers.model import LedgerEntry
from monorepo.core.database import get_db  # Database session dependency
from pydantic import BaseModel
from enum import Enum

# LEDGER_OPERATION_CONFIG dictionary - Defines the impact of each operation on the balance
LEDGER_OPERATION_CONFIG = {
    "DAILY_REWARD": 1,
    "SIGNUP_CREDIT": 3,
    "CREDIT_SPEND": -1,
    "CREDIT_ADD": 10,
    "CONTENT_CREATION": -5,
    "CONTENT_ACCESS": 0,
}

# LedgerOperation enum - Defines valid operations
class LedgerOperation(str, Enum):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"

# LedgerEntryCreate model - Defines the request body for creating a ledger entry
class LedgerEntryCreate(BaseModel):
    owner_id: str
    operation: LedgerOperation
    amount: int
    nonce: str
    created_on: datetime = datetime.utcnow()

router = APIRouter()

# /ledger/{owner_id} - Get current balance for a given owner_id
@router.get("/ledger/{owner_id}")
def get_balance(owner_id: str, db: Session = Depends(get_db)):
    balance = db.query(func.sum(LedgerEntry.amount)).filter(LedgerEntry.owner_id == owner_id).scalar()
    print(balance)
    return {"balance": balance if balance else 0}

# /ledger - Create a new ledger entry
@router.post("/ledger")
def create_ledger_entry(entry: LedgerEntryCreate, db: Session = Depends(get_db)):
    try:
        # Validate the operation type
        if entry.operation not in LEDGER_OPERATION_CONFIG:
            raise HTTPException(status_code=400, detail="Invalid ledger operation")

        # Check if the balance is sufficient
        balance = db.query(func.sum(LedgerEntry.amount)).filter(LedgerEntry.owner_id == entry.owner_id).scalar() or 0
        operation_amount = LEDGER_OPERATION_CONFIG[entry.operation]
        if balance + operation_amount < 0:
            raise HTTPException(status_code=400, detail="Insufficient balance")

        # Check for duplicate nonce
        if db.query(LedgerEntry).filter(LedgerEntry.nonce == entry.nonce).first():
            raise HTTPException(status_code=400, detail="Duplicate transaction nonce")

        # Create and save the ledger entry
        entry.amount = operation_amount  # Set the amount based on the operation
        ledger_entry = LedgerEntry(**entry.dict())
        db.add(ledger_entry)
        db.commit()

        return {"message": "Transaction successful", "entry": entry}

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Database integrity error: {str(e)}")

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")