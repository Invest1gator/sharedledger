# In appName/src/api/ledgers/schemas.py
from typing import List
from enum import Enum
# core/ledgers/app1_operations.py
from monorepo.core.ledgers.schemas import BaseLedgerOperation


def validate_shared_operations(app_operations: List[Enum]) -> bool:
    # Get all the values from the BaseLedgerOperation Enum
    base_operations = {operation.value for operation in BaseLedgerOperation}

    # Get all values from the app's Enum
    app_operations_values = {operation.value for operation in app_operations}

    # Ensure that all base operations are present in the app's operations
    if not base_operations.issubset(app_operations_values):
        missing_operations = base_operations - app_operations_values
        raise ValueError(f"App is missing shared operations: {', '.join(missing_operations)}")

    return True

# Type Safety as mentioned in the task definition
class App1LedgerOperation(Enum):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"

# Ensure shared operations are included
BaseLedgerOperation.validate_operations(App1LedgerOperation)

'''
FIRST CODE SITUATION IN THE TASK
from enum import Enum

# In appName/src/api/ledgers/schemas.py
class LedgerOperation(Enum):
 # Shared operations
 DAILY_REWARD = "DAILY_REWARD"
 SIGNUP_CREDIT = "SIGNUP_CREDIT"
 CREDIT_SPEND = "CREDIT_SPEND"
 CREDIT_ADD = "CREDIT_ADD"
 # App-specific operations
 CONTENT_CREATION = "CONTENT_CREATION"
 CONTENT_ACCESS = "CONTENT_ACCESS"
'''