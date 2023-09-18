from pydantic import BaseModel
from datetime import date
class Transaction(BaseModel):
    date: date
    description: str
    amount: float
    account_number: str
