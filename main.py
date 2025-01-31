# main.py
from monorepo.core.registry import LedgerOperationRegistry
from monorepo.core.ledgers.schemas import BaseLedgerOperation
from monorepo.core.ledgers.operations import get_combined_operations
from src.app1.api.ledgers.schemas import App1LedgerOperation
from fastapi import FastAPI
from src.app1.api.ledgers.endpoints import router as ledger_router  # Import the router
from monorepo.core.database import Base
app = FastAPI()

# Include the ledger router
app.include_router(ledger_router)

def initialize_app_operations():
    try:
        BaseLedgerOperation.validate_operations(App1LedgerOperation)

        print("App operations validated successfully!")
    except ValueError as e:
        print(f"Error validating operations: {e}")
        # Handle the error (e.g., abort app startup, log the issue)


def main():
    registry = LedgerOperationRegistry()

    # Register core operations
    print("Registering core operations...")
    registry.register_operations(BaseLedgerOperation)  # Pass the Enum class
    
    # App1 işlemleri kaydet
    print("Registering app-specific operations...")
    registry.register_operations(App1LedgerOperation)

    # Initialize app operations and validate them
    initialize_app_operations()  # <-- Add this line

    # App1 özel işlemleri al ve yazdır
    app1_operations = get_combined_operations(App1LedgerOperation)
    print("App1 Operations:", app1_operations)

    # Kayıtlı işlemleri yazdirir, eger ucuncu bir uygulama olsaydi veya gelecekte eklenirse onun da operationlari buradan goruntulenebilecek.
    print("All registered operations:", registry.get_all_operations())
if __name__ == "__main__":
    main()
