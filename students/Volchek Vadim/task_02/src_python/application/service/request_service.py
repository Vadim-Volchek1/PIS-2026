"""
Application Layer: BugService.
"""
from application.port.inbound import CreateBugUseCase, CreateBugCommand
from application.port.out import BugRepository, NotificationService
from domain import Bug, Project, Priority


class BugService(CreateBugUseCase):
    """Use-case implementation."""

    def __init__(self, repository: BugRepository, notifications: NotificationService):
        self._repository = repository
        self._notifications = notifications

    def create_bug(self, command: CreateBugCommand) -> str:
        project = Project(project_id=command.project_id, name=command.project_name, active=True)
        priority = Priority.from_string(command.priority)
        bug = Bug(
            project=project,
            title=command.title,
            description=command.description,
            priority=priority,
        )
        bug.assign(command.assignee_id)
        self._repository.save(bug)
        self._notifications.send_assigned_notification(command.assignee_id, bug.id)
        return bug.id
