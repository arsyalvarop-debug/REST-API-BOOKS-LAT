
import sqlite3


def get_connection():
    connection = sqlite3.connect("books.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            stock INTEGER NOT NULL DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_table()
    print("Database dan tabel buku berhasil dibuat.")
