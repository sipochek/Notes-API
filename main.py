from fastapi import FastAPI, Query, HTTPException
from database import get_connection
from schemas import Note, NoteCreate
app =FastAPI()

      
@app.post("/notes", response_model=Note, status_code=201)
def create_note(note_data: NoteCreate):
    connection = get_connection()

    cursor = connection.execute(
        "INSERT INTO notes (title, text) VALUES (?,?)",
        (note_data.title,note_data.text)
    )
    connection.commit()

    new_id = cursor.lastrowid
    connection.close()
    return {
        "id": new_id,
        "title": note_data.title,
        "text": note_data.text,
    }

@app.put("/notes/{note_id}",response_model=Note)
def update_note(note_id:int,note_data: NoteCreate):
    connection = get_connection()
    cursor = connection.execute(
        "UPDATE notes SET title = ? , text = ? WHERE id = ?",
        (note_data.title,note_data.text,note_id)
    )
    connection.commit()
    upd_count = cursor.rowcount
    connection.close()
    if upd_count==0:
        raise HTTPException(status_code=404, detail="Заметки с таким id нету")
    return {
        "id": note_id,
        "title": note_data.title,
        "text": note_data.text
    }

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id:int):
    connection = get_connection()
    cursor = connection.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )
    connection.commit()
    upd_count = cursor.rowcount
    connection.close()
    if upd_count==0:
        raise HTTPException(status_code=404, detail="Заметки с таким id не существует!")
    return

@app.get("/notes/{note_id}",response_model=Note)
def show_id(note_id: int):
    connection = get_connection()
    cursor = connection.execute(
        "SELECT id, title, text FROM notes WHERE id= ?",
        (note_id,)
    )
    row = cursor.fetchone()
    connection.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    return dict(row)

@app.get("/notes",response_model=list[Note])
def show_notes(limit: int=Query(default=10,ge=1,le=50),offset: int=Query(default=0,ge=0),search: str = "",):
    connection = get_connection()
    if search == "":
        cursor = connection.execute(
            "SELECT * FROM notes ORDER BY id LIMIT ? OFFSET ?",
            (limit, offset),
        )
    else:
        pattern = f"%{search}%"
        cursor = connection.execute(
            "SELECT * FROM notes WHERE title LIKE ? ORDER BY id LIMIT ? OFFSET ?",
            (pattern,limit, offset)
        )
    rows = cursor.fetchall()
    connection.close()
    return [dict(row) for row in rows]