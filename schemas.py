from pydantic import BaseModel, Field

class Note(BaseModel):
    id: int
    title: str
    text: str
class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100 )
    text: str = Field(min_length=1)