# from pydantic import BaseModel
# from fastapi import FastAPI

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []

# @app.post("/items/")
# async def create_item(item: Item) -> Item:
#     return item

# @app.get("/items/")
# def read_items() -> list[Item]:
#     return [
#         Item(name = 'Portal Gun', price=42.0),
#         Item(name = 'Plumbus', price = 32.0)
#     ]

from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel

app =FastAPI()

class Note(BaseModel):
    id: int
    title: str
    text: str

notes = [
    {"id": 1, "title": "thank you", "text": "hi!"},
    {"id": 2, "title": "thank you2", "text": "hi!2"},
    {"id": 3, "title": "thank you3", "text": "hi!3"},
]

@app.get("/notes/{note_id}",response_model=Note)
def show_id(note_id: int):
    for note in notes:
        if note_id == note["id"]:
            return note
    raise HTTPException(status_code=404, detail="Заметка не найдена!")

@app.get("/notes",response_model=list[Note])
def show_notes(limit: int=Query(default=10,ge=1,le=50),offset: int=Query(default=0,ge=0)):
    return notes[offset:offset + limit]
