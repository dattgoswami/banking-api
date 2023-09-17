from fastapi import APIRouter, HTTPException, Query
from src.services import database
from src.models.transaction import Transaction
from typing import List

router = APIRouter()

@router.get("/transactions/", response_model=List[Transaction])
def read_transactions(skip: int = Query(0, ge=0), limit: int = Query(10, le=1000)):
    return database.get_transactions(skip=skip, limit=limit)

@router.get("/transactions/{transaction_id}", response_model=Transaction)
def read_transaction(transaction_id: int):
    transaction = database.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.post("/transactions/", response_model=Transaction)
def add_transaction(transaction: Transaction):
    transaction_id = database.create_transaction(transaction)
    return get_transaction(transaction_id)

@router.put("/transactions/{transaction_id}", response_model=Transaction)
def update_existing_transaction(transaction_id: int, transaction: Transaction):
    rows_modified = database.update_transaction(transaction_id, transaction)
    if not rows_modified:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return get_transaction(transaction_id)

@router.delete("/transactions/{transaction_id}", response_model=Transaction)
def remove_transaction(transaction_id: int):
    transaction = database.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    database.delete_transaction(transaction_id)
    return transaction
