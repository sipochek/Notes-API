import sqlite3

def get_connection():
    connection = sqlite3.connect("repeat.db")
    connection.row_factory = sqlite3.Row
    return connection


def ins_tas(title: str, done: int):
    connection = get_connection()
    cursor=connection.execute("INSERT INTO tasks (title, done) VALUES (?,?)",(title,done))
    connection.commit()
    cursor = connection.execute("SELECT * FROM tasks WHERE id>5")
    print(cursor.fetchall())
    connection.close()

def del_tas(id: int):
    connection = get_connection()
    cursor = connection.execute("DELETE FROM tasks WHERE id = ?", (id,))
    connection.commit()
    cursor = connection.execute("SELECT * FROM tasks")
    print(cursor.fetchall())
    connection.close()
def upd_tas(id:int, title:str, done:int):
    connection = get_connection()
    cursor = connection.execute("UPDATE tasks SET title = ?, done = ? WHERE id = ?",(title,done,id))
    connection.commit()
    cursor.execute("SELECT * FROM tasks")
    print(cursor.fetchall())
    connection.close()
def show_id(id:int):
    connection = get_connection()
    cursor = connection.execute("SELECT * FROM tasks WHERE id=?",(id,))
    connection.commit()
    row = cursor.fetchone()
    connection.close()
    if row is None:
        print("Не существует таски с таким id")
        return
    print(row)
def show_all():
    connection = get_connection()
    cursor = connection.execute("SELECT * FROM tasks")
    connection.commit()
    rows = cursor.fetchall()
    connection.close()
    print([dict(row) for row in rows])
show_all()
    
