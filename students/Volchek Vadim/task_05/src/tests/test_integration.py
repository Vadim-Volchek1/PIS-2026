from fastapi.testclient import TestClient

from main import app


def test_create_and_get_bug() -> None:
    client = TestClient(app)
    response = client.post(
        "/api/bugs",
        json={"project_id": "PIS-API", "title": "Cannot upload file", "priority": "HIGH"},
    )
    assert response.status_code == 200
    bug_id = response.json()["bug_id"]
    loaded = client.get(f"/api/bugs/{bug_id}")
    assert loaded.status_code == 200
    assert loaded.json()["title"] == "Cannot upload file"
