from sqlite3 import connect, Row
from src.models.transaction import Transaction

DATABASE = "./database/data.db"

def get_db_connection():
    conn = connect(DATABASE)
    conn.row_factory = Row
    return conn

def get_transactions(skip: int, limit: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    transactions = cursor.execute(
        "SELECT * FROM transactions LIMIT ? OFFSET ?", (limit, skip)).fetchall()
    cursor.close()
    conn.close()
    return transactions

def get_transaction(transaction_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    transaction = cursor.execute(
        "SELECT * FROM transactions WHERE id = ?", (transaction_id,)).fetchone()
    cursor.close()
    conn.close()
    return transaction

def create_transaction(transaction: Transaction):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (date, description, amount, account_number) VALUES (?, ?, ?, ?)",
        (transaction.date, transaction.description,
         transaction.amount, transaction.account_number)
    )
    lastrowid = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return lastrowid

def update_transaction(transaction_id: int, transaction: Transaction):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE transactions SET date = ?, description = ?, amount = ?, account_number = ? WHERE id = ?",
        (transaction.date, transaction.description,
         transaction.amount, transaction.account_number, transaction_id)
    )
    rowcount = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return rowcount

def delete_transaction(transaction_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    rowcount = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return rowcount
