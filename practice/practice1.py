from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() -> dict[str,str]:
    return {"message": "Hello, World"}

@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str,str | int]:
    return {"item_id": item_id, "name": "Товар", "status": "в наличии"}

@app.get("/hello/{name}")
def greeting(name: str) -> dict[str,str]:
    return {"greeting": f"Hello, {name}"}