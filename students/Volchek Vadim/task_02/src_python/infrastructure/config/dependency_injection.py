"""
Infrastructure Layer: DI configuration.
"""
from fastapi import FastAPI

from application.port.out import BugRepository, NotificationService
from application.service import BugService
from infrastructure.adapter.inbound import BugController
from infrastructure.adapter.out import InMemoryBugRepository, MockNotificationService


class DependencyContainer:
    def __init__(self):
        self._repository: BugRepository = InMemoryBugRepository()
        self._notifications: NotificationService = MockNotificationService()
        self._bug_service = BugService(
            repository=self._repository,
            notifications=self._notifications,
        )

    def get_bug_service(self) -> BugService:
        return self._bug_service

    def configure_web_app(self, app: FastAPI) -> None:
        BugController(app=app, use_case=self._bug_service)


_container: DependencyContainer | None = None


def get_container() -> DependencyContainer:
    global _container
    if _container is None:
        _container = DependencyContainer()
    return _container


def reset_container() -> None:
    global _container
    _container = None
