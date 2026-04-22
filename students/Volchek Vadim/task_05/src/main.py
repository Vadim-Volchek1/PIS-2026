from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Bug Tracker Infrastructure")
BUGS: dict[str, dict] = {}


class CreateBugDto(BaseModel):
    project_id: str
    title: str
    priority: str


class AssignBugDto(BaseModel):
    group_name: str


@app.post("/api/bugs")
def create_bug(dto: CreateBugDto) -> dict:
    if dto.priority not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
        raise HTTPException(status_code=400, detail="INVALID_PRIORITY")
    bug_id = str(uuid4())
    BUGS[bug_id] = {
        "id": bug_id,
        "project_id": dto.project_id,
        "title": dto.title,
        "priority": dto.priority,
        "status": "OPEN",
        "assigned_group": None,
    }
    return {"bug_id": bug_id}


@app.post("/api/bugs/{bug_id}/assign")
def assign_bug(bug_id: str, dto: AssignBugDto) -> dict:
    bug = BUGS.get(bug_id)
    if not bug:
        raise HTTPException(status_code=404, detail="BUG_NOT_FOUND")
    if bug["status"] == "CLOSED":
        raise HTTPException(status_code=409, detail="BUG_ALREADY_CLOSED")
    bug["assigned_group"] = dto.group_name
    return {"status": "assigned"}


@app.get("/api/bugs/{bug_id}")
def get_bug(bug_id: str) -> dict:
    bug = BUGS.get(bug_id)
    if not bug:
        raise HTTPException(status_code=404, detail="BUG_NOT_FOUND")
    return bug


@app.get("/api/bugs")
def list_bugs() -> list[dict]:
    return list(BUGS.values())
