import sqlite3
import os
DB_PATH = os.getenv("NOTES_DB_PATH", "notes.db")
def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

connection = sqlite3.connect(DB_PATH)

connection.execute("""
    CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    text TEXT NOT NULL
    )
""")
connection.commit()
connection.close()