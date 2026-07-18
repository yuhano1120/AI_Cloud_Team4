from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ask_endpoint_returns_stubbed_answer() -> None:
    response = client.post("/ask", json={"question": "Where can I find academic support at CMU?"})

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "stubbed"
    assert body["provider"].startswith("stub://")
    assert "Where can I find academic support at CMU?" in body["answer"]
    assert body["trace_id"]
    assert body["retrieved_context"]
    assert body["retrieved_context"][0]["source"].startswith("stub://")


def test_ask_endpoint_rejects_empty_question() -> None:
    response = client.post("/ask", json={"question": ""})

    assert response.status_code == 422
