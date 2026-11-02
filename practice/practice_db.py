from database import get_connection

connection = get_connection()

cursor = connection.execute("SELECT id, title, text FROM notes")

rows = cursor.fetchall()
notes = [dict(row) for row in rows]
connection.close()
print(notes)