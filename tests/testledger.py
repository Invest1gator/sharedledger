from fastapi.testclient import TestClient
from main import app  # Import the FastAPI app
import pytest
import sys
import os

client = TestClient(app)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from main import app  # FastAPI uygulamanızı buraya ekleyin


def test_get_balance():
    """Test: Get current balance for a given owner_id"""
    response = client.get("/ledger/test_owner_id")
    assert response.status_code == 200
    assert "balance" in response.json()
    assert isinstance(response.json()["balance"], int)

def test_create_ledger_entry_valid():
    """Test: Create ledger entry with valid data"""
    response = client.post("/ledger", json={
        "owner_id": "test_owner_id",
        "operation": "DAILY_REWARD",
        "amount": 5,
        "nonce": "unique_nonce_123",
        "created_on": "2025-01-01T00:00:00"
    })
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Transaction successful"

def test_create_ledger_entry_insufficient_balance():
    """Test: Fail when creating a ledger entry with insufficient balance"""
    response = client.post("/ledger", json={
        "owner_id": "test_owner_id",
        "operation": "CREDIT_SPEND",
        "amount": -100,
        "nonce": "unique_nonce_456",
        "created_on": "2025-01-01T00:00:00"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Insufficient balance"

def test_create_ledger_entry_duplicate_nonce():
    """Test: Fail when creating a ledger entry with a duplicate nonce"""
    # First, create a valid entry
    client.post("/ledger", json={
        "owner_id": "test_owner_id",
        "operation": "DAILY_REWARD",
        "amount": 5,
        "nonce": "unique_nonce_789",
        "created_on": "2025-01-01T00:00:00"
    })
    # Try to create a duplicate entry with the same nonce
    response = client.post("/ledger", json={
        "owner_id": "test_owner_id",
        "operation": "CREDIT_ADD",
        "amount": 10,
        "nonce": "unique_nonce_789",
        "created_on": "2025-01-02T00:00:00"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Duplicate transaction nonce"

def test_create_ledger_entry_invalid_operation():
    """Test: Fail when creating a ledger entry with an invalid operation"""
    response = client.post("/ledger", json={
        "owner_id": "test_owner_id",
        "operation": "INVALID_OPERATION",
        "amount": 10,
        "nonce": "unique_nonce_101",
        "created_on": "2025-01-01T00:00:00"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid ledger operation"

def test_get_balance_edge_case():
    """Test: Edge case for get_balance when no entries exist"""
    response = client.get("/ledger/non_existing_owner")
    assert response.status_code == 200
    assert response.json()["balance"] == 0

def test_create_ledger_entry_zero_amount():
    """Test: Create ledger entry with zero amount"""
    response = client.post("/ledger", json={
        "owner_id": "test_owner_id",
        "operation": "CONTENT_ACCESS",
        "amount": 0,
        "nonce": "unique_nonce_102",
        "created_on": "2025-01-01T00:00:00"
    })
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Transaction successful"