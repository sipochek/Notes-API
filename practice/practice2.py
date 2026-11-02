from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    username: str
    age: int
    email: str | None = None
app = FastAPI()

@app.get("/products")
def prod(skip: int=0,limit: int = 10):
    return {"skip": skip, "limit": limit, "status": "ok"}

@app.get("/products/item/{id_item}")
def item(id_item):
    return {"id": id_item}

@app.get("/products/items/item{id_item}")
def item_1(id_item:int) -> dict[str,int | str]:
    return {"response": id_item, "item": f"item{id_item}"}

@app.post("/users")
def user(user: User) -> dict[str, str | int]:
    return {"message": f"Пользователь {user.username} создан", "age_in_10_years": user.age + 10}