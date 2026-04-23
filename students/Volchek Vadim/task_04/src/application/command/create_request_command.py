"""
CreateBugCommand: команда создания бага.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class CreateRequestCommand:
    reporter_id: str
    project_id: str
    title: str
    description: str
    priority: str

    def __post_init__(self):
        if not self.reporter_id:
            raise ValueError("reporter_id обязателен")
        if not self.project_id:
            raise ValueError("project_id обязателен")
        if not self.title:
            raise ValueError("title обязателен")
        if self.priority not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
            raise ValueError("priority должен быть LOW|MEDIUM|HIGH|CRITICAL")
