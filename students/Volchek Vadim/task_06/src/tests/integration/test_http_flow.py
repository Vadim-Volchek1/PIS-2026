from fastapi import FastAPI
from fastapi.testclient import TestClient


def build_app() -> FastAPI:
    app = FastAPI()
    storage: dict[str, dict] = {}

    @app.post("/bugs")
    def create_bug(payload: dict) -> dict:
        bug_id = "BUG-INT-1"
        storage[bug_id] = {"id": bug_id, **payload, "status": "OPEN"}
        return {"id": bug_id}

    @app.get("/bugs/{bug_id}")
    def get_bug(bug_id: str) -> dict:
        return storage[bug_id]

    return app


def test_http_create_and_get() -> None:
    client = TestClient(build_app())
    created = client.post("/bugs", json={"title": "UI freeze", "priority": "HIGH"})
    bug_id = created.json()["id"]
    loaded = client.get(f"/bugs/{bug_id}")
    assert loaded.json()["title"] == "UI freeze"
