from dataclasses import dataclass


@dataclass
class Bug:
    bug_id: str
    project_id: str
    title: str
    priority: str
    status: str = "OPEN"


class BugGrpcServerStub:
    def __init__(self) -> None:
        self._bugs: dict[str, Bug] = {}

    def CreateBug(self, project_id: str, title: str, priority: str) -> str:
        bug_id = f"BUG-{len(self._bugs) + 1}"
        self._bugs[bug_id] = Bug(bug_id, project_id, title, priority)
        return bug_id

    def GetBug(self, bug_id: str) -> Bug:
        return self._bugs[bug_id]

    def ListActiveBugs(self, project_id: str) -> list[Bug]:
        return [b for b in self._bugs.values() if b.project_id == project_id and b.status != "CLOSED"]
