from uuid import uuid4

from application.port.inbound import CreateBugCommand, CreateBugUseCase
from application.port.outbound import BugRepositoryPort, ProjectLookupPort


class BugService(CreateBugUseCase):
    def __init__(self, repo: BugRepositoryPort, projects: ProjectLookupPort):
        self._repo = repo
        self._projects = projects

    def create_bug(self, command: CreateBugCommand) -> str:
        if not self._projects.exists(command.project_id):
            raise ValueError("PROJECT_NOT_FOUND")
        if command.priority not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
            raise ValueError("INVALID_PRIORITY")
        bug_id = str(uuid4())
        self._repo.save(
            {
                "id": bug_id,
                "project_id": command.project_id,
                "title": command.title,
                "description": command.description,
                "priority": command.priority,
                "status": "OPEN",
            }
        )
        return bug_id
