from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_and_get_task():
    response = client.post("/tasks", json={"title": "Learn Kubernetes"})
    assert response.status_code == 201
    task = response.json()
    assert task["title"] == "Learn Kubernetes"

    response = client.get("/tasks")
    assert response.status_code == 200
    assert any(t["title"] == "Learn Kubernetes" for t in response.json())
