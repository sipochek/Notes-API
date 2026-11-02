import sqlite3

def get_connection():
    connection = sqlite3.connect("notes.db")
    connection.row_factory = sqlite3.Row
    return connection

connection = sqlite3.connect("notes.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    text TEXT NOT NULL
    )
""")
connection.commit()
connection.close()