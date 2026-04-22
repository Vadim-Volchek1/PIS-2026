from dataclasses import dataclass


@dataclass(frozen=True)
class BugCreated:
    bug_id: str
    project_id: str
    title: str
    priority: str


@dataclass(frozen=True)
class BugAssigned:
    bug_id: str
    group_name: str


class ReadModelStore:
    def __init__(self) -> None:
        self.rows: dict[str, dict] = {}

    def apply(self, event: object) -> None:
        if isinstance(event, BugCreated):
            self.rows[event.bug_id] = {
                "bug_id": event.bug_id,
                "project_id": event.project_id,
                "title": event.title,
                "priority": event.priority,
                "status": "OPEN",
                "group_name": None,
            }
        if isinstance(event, BugAssigned) and event.bug_id in self.rows:
            self.rows[event.bug_id]["group_name"] = event.group_name

    def find_by_project(self, project_id: str) -> list[dict]:
        return [row for row in self.rows.values() if row["project_id"] == project_id]
