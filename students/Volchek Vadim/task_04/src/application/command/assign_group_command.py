"""
AssignDeveloperCommand: назначить исполнителя на баг.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class AssignGroupToRequestCommand:
    request_id: str
    assignee_id: str

    def __post_init__(self):
        if not self.request_id:
            raise ValueError("request_id обязателен")
        if not self.assignee_id:
            raise ValueError("assignee_id обязателен")
