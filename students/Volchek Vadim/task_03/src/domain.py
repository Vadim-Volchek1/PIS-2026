from dataclasses import dataclass, field
from enum import Enum
from typing import List


class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class BugStatus(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"


@dataclass(frozen=True)
class BugTitle:
    value: str

    def __post_init__(self) -> None:
        if not self.value.strip():
            raise ValueError("EMPTY_TITLE")


@dataclass(frozen=True)
class Attachment:
    filename: str
    content_type: str


@dataclass
class Bug:
    bug_id: str
    project_id: str
    title: BugTitle
    priority: Priority
    status: BugStatus = BugStatus.OPEN
    assigned_group: str | None = None
    attachments: List[Attachment] = field(default_factory=list)


@dataclass(frozen=True)
class BugAssigned:
    bug_id: str
    group_name: str


class BugAggregate:
    def __init__(self, bug: Bug):
        self.bug = bug
        self.events: list[object] = []

    def assign(self, group_name: str) -> None:
        if self.bug.status == BugStatus.CLOSED:
            raise ValueError("BUG_ALREADY_CLOSED")
        self.bug.assigned_group = group_name
        self.events.append(BugAssigned(bug_id=self.bug.bug_id, group_name=group_name))
