from fastapi.testclient import TestClient
from main import app
import sqlite3
import pytest
import main

@pytest.fixture(autouse=True)
def test_database(tmp_path, monkeypatch):
    db_path = tmp_path / "test_notes.db"
    def get_test_connection():
        connection = sqlite3.connect(db_path)
        connection.row_factory = sqlite3.Row
        return connection
    connection = get_test_connection()
    connection.execute("""
        CREATE TABLE notes (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        text TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()
    monkeypatch.setattr(
        main,
        "get_connection",
        get_test_connection,
    )
client = TestClient(app)

def test_create_note_empty_title():
    data = {
    "title": "",
    "text": "123123"
    }
    response = client.post("/notes", json=data)
    assert response.status_code == 422
    g_response = client.get("/notes")
    assert g_response.status_code==200
    assert g_response.json() == []
def test_update_missing_note():
    data = {
        "title": "fdaffsf",
        "text": "123123"
        }
    response = client.put("/notes/999", json=data)
    assert response.status_code==404
    
    g_response = client.get("/notes/999")
    assert g_response.status_code==404


def test_get_note_invalid_lm_off():
    response = client.get("/notes?limit=-31?offset=-1")
    assert response.status_code==422
def test_get_note_invalid_id():
    response = client.get("/notes/abc")
    assert response.status_code == 422
def test_get_note_invalid_limit():
    response = client.get("/notes?limit=0")
    assert response.status_code == 422
def test_create_note():
    data = {
        "title": "test",
        "text": "test1",
    }
    response = client.post("/notes", json=data)
    assert response.status_code ==201
    created = response.json()
    assert created["title"]==data["title"]
    assert created["text"]==data["text"]
    assert isinstance(created["id"],int)

    note_id = created["id"]
    get_response = client.get(f"/notes/{note_id}")
    assert get_response.status_code==200
    assert get_response.json()==created
def test_delete_note():
    response = client.post("/notes",json={"title": "for delete","text": "for delete1"})
    assert response.status_code ==201
    note_id = response.json()["id"]

    d_response = client.delete(f"/notes/{note_id}")
    assert d_response.status_code == 204
    assert d_response.content == b""
    d_g_response = client.get(f"/notes/{note_id}")
    assert d_g_response.status_code == 404
    repeat_response = client.delete(f"/notes/{note_id}")
    assert repeat_response.status_code == 404

def test_update_note():
    response = client.post("/notes",json={"title": "for delete","text": "for delete1"})
    assert response.status_code == 201
    note_id = response.json()["id"]
    p_response = client.put(f"/notes/{note_id}",json={"title": "gangbang","text": "gangholdonbang"})
    assert p_response.status_code == 200
    assert p_response.json() == {
        "id": note_id,
        "title": "gangbang",
        "text": "gangholdonbang"
    }
    gp_response = client.get(f"/notes/{note_id}")
    assert gp_response.status_code == 200
    gp_j_response = gp_response.json()
    assert gp_j_response["id"] == note_id
    assert gp_j_response["title"] == "gangbang"
    assert gp_j_response["text"]=="gangholdonbang"
