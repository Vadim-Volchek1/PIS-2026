"""
Domain Layer: Bug aggregate.
"""
from datetime import datetime
import random

from .group import Project
from .zone import Priority
from .request_status import BugStatus


class Bug:
    """Aggregate root: Bug."""

    def __init__(self, project: Project, title: str, description: str, priority: Priority):
        if not title.strip():
            raise ValueError("Заголовок бага обязателен")

        self._id = self._generate_bug_id()
        self._project = project
        self._title = title.strip()
        self._description = description.strip()
        self._priority = priority
        self._status = BugStatus.OPEN
        self._assignee_id: str | None = None
        self._created_at = datetime.now()

    def assign(self, assignee_id: str) -> None:
        if not assignee_id.strip():
            raise ValueError("Исполнитель обязателен")
        self._assignee_id = assignee_id
        self._status = BugStatus.IN_PROGRESS

    def mark_resolved(self) -> None:
        if self._status != BugStatus.IN_PROGRESS:
            raise ValueError("Решить можно только баг в статусе IN_PROGRESS")
        self._status = BugStatus.RESOLVED

    def close(self) -> None:
        if self._status != BugStatus.RESOLVED:
            raise ValueError("Закрыть можно только баг в статусе RESOLVED")
        self._status = BugStatus.CLOSED

    @staticmethod
    def _generate_bug_id() -> str:
        year = datetime.now().year
        random_num = random.randint(0, 9999)
        return f"BUG-{year}-{random_num:04d}"

    @property
    def id(self) -> str:
        return self._id

    @property
    def project(self) -> Project:
        return self._project

    @property
    def priority(self) -> Priority:
        return self._priority

    @property
    def status(self) -> BugStatus:
        return self._status

    @property
    def assignee_id(self) -> str | None:
        return self._assignee_id
