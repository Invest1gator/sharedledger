# src/core/operations.py
from typing import List, Union
from monorepo.core.ledgers.schemas import BaseLedgerOperation
from src.app1.api.ledgers.schemas import App1LedgerOperation
from enum import Enum


def get_combined_operations(app_operations_enum: Enum) -> list:
    """
    Combines operations from BaseLedgerOperation and app-specific operations,
    ensuring no duplicates.
    """
    # Get values from BaseLedgerOperation
    base_operations = {operation.value for operation in BaseLedgerOperation}

    # Get values from app-specific operations
    app_operations = {operation.value for operation in app_operations_enum}

    # Combine and deduplicate using a set
    combined_operations = base_operations.union(app_operations)

    # Convert the set back to a list
    return list(combined_operations)

# Usage
#app1_operations = get_combined_operations(App1LedgerOperation)
#print(app1_operations)
# Output: ['DAILY_REWARD', 'SIGNUP_CREDIT', 'CREDIT_SPEND', 'CREDIT_ADD', 'CONTENT_CREATION', 'CONTENT_ACCESS']
