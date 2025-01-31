# monorepo/core/ledgers/schemas.py
from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class BaseLedgerOperation(Enum):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"
    

    # Enforcement of app-specific operations metioned in the task
    @classmethod
    def validate_operations(cls, app_operations: Enum):
        """
        Validates that app-specific operations include all shared operations from BaseLedgerOperation.
        """
        shared_operations = {operation.value for operation in cls}
        app_operations_values = {operation.value for operation in app_operations}

        missing_operations = shared_operations - app_operations_values
        if missing_operations:
            raise ValueError(f"Missing shared operations in {app_operations.__name__}: {', '.join(missing_operations)}")



class LedgerEntryCreate(BaseModel):
    owner_id: str
    operation: BaseLedgerOperation
    amount: int
    nonce: str
    created_on: datetime

    class Config:
        from_attributes = True

