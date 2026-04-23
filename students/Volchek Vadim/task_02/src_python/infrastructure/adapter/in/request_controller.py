"""
Infrastructure Layer: REST controller (inbound adapter).
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from application.port.inbound import CreateBugUseCase, CreateBugCommand


class CreateBugDto(BaseModel):
    project_id: str
    project_name: str
    title: str
    description: str
    priority: str
    assignee_id: str


class CreateBugResponseDto(BaseModel):
    bug_id: str


class BugController:
    def __init__(self, app: FastAPI, use_case: CreateBugUseCase):
        self._use_case = use_case

        @app.post("/api/bugs", response_model=CreateBugResponseDto)
        async def create_bug(dto: CreateBugDto):
            try:
                command = CreateBugCommand(
                    project_id=dto.project_id,
                    project_name=dto.project_name,
                    title=dto.title,
                    description=dto.description,
                    priority=dto.priority,
                    assignee_id=dto.assignee_id,
                )
                bug_id = self._use_case.create_bug(command)
                return CreateBugResponseDto(bug_id=bug_id)
            except ValueError as exc:
                raise HTTPException(status_code=400, detail=str(exc))

        @app.get("/api/health")
        async def health_check():
            return {"status": "OK", "service": "Bug Service"}
