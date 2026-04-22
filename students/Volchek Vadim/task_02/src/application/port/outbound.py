from typing import Protocol


class BugRepositoryPort(Protocol):
    def save(self, bug: dict) -> None:
        ...


class ProjectLookupPort(Protocol):
    def exists(self, project_id: str) -> bool:
        ...
