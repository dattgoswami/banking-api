from pydantic import BaseModel

class Transaction(BaseModel):
    date: str
    description: str
    amount: float
    account_number: str
