from fastapi.testclient import TestClient
from src.api.routes import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_query_endpoint():
    response = client.post(
        "/query",
        json={"question": "What is the average age of users?"}
    )
    assert response.status_code == 200
    assert "sql_query" in response.json()
    assert "results" in response.json()
    assert "natural_response" in response.json()
