from fastapi import FastAPI
from src.handlers import transactions

app = FastAPI()

app.include_router(transactions.router)
