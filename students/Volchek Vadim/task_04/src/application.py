from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class CreateBugCommand:
    project_id: str
    title: str
    priority: str


@dataclass(frozen=True)
class AssignBugCommand:
    bug_id: str
    group_name: str


@dataclass(frozen=True)
class GetBugQuery:
    bug_id: str


class BugRepository:
    def __init__(self) -> None:
        self._items: dict[str, dict] = {}

    def save(self, bug: dict) -> None:
        self._items[bug["id"]] = bug

    def get(self, bug_id: str) -> dict:
        return self._items[bug_id]


class CreateBugHandler:
    def __init__(self, repo: BugRepository):
        self._repo = repo

    def handle(self, command: CreateBugCommand) -> str:
        if command.priority not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
            raise ValueError("INVALID_PRIORITY")
        bug_id = str(uuid4())
        self._repo.save(
            {
                "id": bug_id,
                "project_id": command.project_id,
                "title": command.title,
                "priority": command.priority,
                "status": "OPEN",
                "assigned_group": None,
            }
        )
        return bug_id


class AssignBugHandler:
    def __init__(self, repo: BugRepository):
        self._repo = repo

    def handle(self, command: AssignBugCommand) -> None:
        bug = self._repo.get(command.bug_id)
        if bug["status"] == "CLOSED":
            raise ValueError("BUG_ALREADY_CLOSED")
        bug["assigned_group"] = command.group_name
        self._repo.save(bug)


class GetBugHandler:
    def __init__(self, repo: BugRepository):
        self._repo = repo

    def handle(self, query: GetBugQuery) -> dict:
        return self._repo.get(query.bug_id)


class BugApplicationService:
    def __init__(self) -> None:
        self.repo = BugRepository()
        self.create_handler = CreateBugHandler(self.repo)
        self.assign_handler = AssignBugHandler(self.repo)
        self.get_handler = GetBugHandler(self.repo)
