from fastapi.testclient import TestClient
from practice3 import app

client = TestClient(app)

def test_get_note_invalid_id():
    response = client.get("/notes/abc")
    assert response.status_code == 422
def test_get_note_invalid_limit():
    response = client.get("/notes?limit=0")
    assert response.status_code == 422