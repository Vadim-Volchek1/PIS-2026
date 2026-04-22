from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class CreateBugCommand:
    project_id: str
    title: str
    description: str
    priority: str


class CreateBugUseCase(Protocol):
    def create_bug(self, command: CreateBugCommand) -> str:
        ...
