# Banking API

A FastAPI service for managing banking transactions. This service is built using FastAPI and SQLite as the backend database.

## Project Structure

```
banking-api
│
├── venv                # Virtual environment for dependencies
│
├── database
│   └── data.db         # SQLite database file
│
└── src                 # Source code directory
    ├── handlers
    │   └── transactions.py    # Endpoint handlers for transactions
    │
    ├── models
    │   └── transaction.py     # Data model for a transaction
    │
    ├── services
    │   └── database.py        # Database related operations
    │
    └── main.py         # Entry point for the API
```

## Routes

### 1. Get Transactions

- **Endpoint**: `/transactions/`
- **Method**: `GET`
- **Query Parameters**:
  - `skip`: Number of records to skip (Default = 0)
  - `limit`: Number of records to fetch (Default = 10, Max = 1000)
- **Response Model**: List of transactions

### 2. Get Specific Transaction

- **Endpoint**: `/transactions/{transaction_id}`
- **Method**: `GET`
- **Response Model**: Specific transaction based on given ID

### 3. Add Transaction

- **Endpoint**: `/transactions/`
- **Method**: `POST`
- **Request Body**: Transaction details
- **Response Model**: Added transaction

### 4. Update Transaction

- **Endpoint**: `/transactions/{transaction_id}`
- **Method**: `PUT`
- **Request Body**: New details for the specified transaction
- **Response Model**: Updated transaction

### 5. Delete Transaction

- **Endpoint**: `/transactions/{transaction_id}`
- **Method**: `DELETE`
- **Response Model**: Removed transaction

## Setup & Run

1. **Setup virtual environment**:

   ```
   python3 -m venv bank_api_env
   source bank_api_env/bin/activate
    # On Windows, use 'bank_api_env\Scripts\activate'
   ```

2. **Install dependencies**:

   ```
   pip install -r requirements.txt
   ```

3. **Run the API**:

   ```
   uvicorn src.main:app --reload
   ```

   This will run the app on http://127.0.0.1:8000/ , send a GET request to http://127.0.0.1:8000/transactions/ .

   If you want to start it on port 5000, then use this:

   ```
   uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload
   ```

## Notes

Ensure that you have proper permissions to access the SQLite database file (`database/data.db`).
