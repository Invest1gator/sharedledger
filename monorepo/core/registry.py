# src/core/registry.py
from monorepo.core.ledgers.model import BaseLedgerOperation
from enum import Enum
# monorepo/core/registry.py
class LedgerOperationRegistry:
    def __init__(self):
        self.registered_operations = set()

    def register_operations(self, operations_enum: Enum):
        """
        Register operations from an Enum class.
        """
        # Validate the operations
        BaseLedgerOperation.validate_operations(operations_enum)

        # Register each operation
        for operation in operations_enum:
            if operation.value in self.registered_operations:
                print(f"Operation '{operation.value}' is already registered.")
            else:
                self.registered_operations.add(operation.value)
                print(f"Operation '{operation.value}' registered successfully.")

    def get_all_operations(self):
        """Retrieve all registered operations as a list."""
        return list(self.registered_operations)