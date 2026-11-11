import sqlite3
from sqlite3 import Connection
from datetime import date


def get_connection():
    return sqlite3.connect("investments.db")


def create_tables():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker TEXT NOT NULL UNIQUE,
                company_name TEXT NOT NULL
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                asset_id INTEGER NOT NULL,
                transaction_date DATE NOT NULL,
                quantity REAL NOT NULL,
                price REAL NOT NULL,
                FOREIGN KEY (asset_id) REFERENCES assets(id)
            )
        """)


def save_transaction(
        conn: Connection,
        asset_id: int,
        transaction_date: date,
        quantity: int,
        price: float
) -> None:
    """
    ask for connection and return none if applied
    """
    conn.execute("""
                    INSERT INTO transactions (
                    asset_id,
                    transaction_date,
                    quantity,
                    price
                    )
                    VALUES (?,?,?,?)
                    """,
                 (asset_id,
                  transaction_date.isoformat(),
                  quantity,
                  price)
                 )

    return None


def get_or_create_asset(
        conn: Connection,
        ticker_name: str,
        long_name: str,
) -> int:
    conn.execute("""
             INSERT OR IGNORE INTO assets (ticker, company_name)
             VALUES (?, ?)
             """, (ticker_name, long_name)
                 )
    asset_id = conn.execute(
        """SELECT id FROM assets WHERE ticker = ?""", (
            ticker_name,)
    ).fetchone()[0]

    return asset_id


def create_transaction(ticker_name: str,
                       longname: str,
                       transaction_date: date,
                       quantity: int,
                       price: float
                       ) -> None:
    with get_connection() as conn:
        asset_id: int = get_or_create_asset(conn, ticker_name, longname)
        save_transaction(conn, asset_id, transaction_date, quantity, price)

        return None
