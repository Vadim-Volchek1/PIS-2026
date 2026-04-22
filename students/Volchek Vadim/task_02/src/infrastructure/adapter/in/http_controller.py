from application.port.inbound import CreateBugCommand
from application.service.bug_service import BugService
from infrastructure.adapter.out.in_memory_repo import (
    InMemoryBugRepository,
    InMemoryProjectLookup,
)


def create_bug_http(payload: dict) -> dict:
    service = BugService(InMemoryBugRepository(), InMemoryProjectLookup())
    command = CreateBugCommand(
        project_id=payload["project_id"],
        title=payload["title"],
        description=payload["description"],
        priority=payload["priority"],
    )
    bug_id = service.create_bug(command)
    return {"bug_id": bug_id}
