from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_schools():
    response = client.get('/api/school')
    assert response.status_code == 200
    assert "data" in response.json()


def test_students():
    response = client.get("/api/student")
    assert response.status_code == 200
    assert "data" in response.json()


def test_get_student():
    response = client.get("/api/student/Muhammadqodir")
    assert response.status_code == 200
    assert "data" in response.json()
    assert response.json()["data"]["email"] == "qodir@gmail.com"
    assert response.json()["data"]["name"] == "Muhammadqodir"


def test_get_school():
    response = client.get("/api/school/IT School")
    assert response.status_code == 200
    assert "data" in response.json()
    assert response.json()["data"]["room"] == [421, 122, 231]
    assert response.json()["data"]["teacher"] == ["Bekzod", "Akbar", "Ali"]
