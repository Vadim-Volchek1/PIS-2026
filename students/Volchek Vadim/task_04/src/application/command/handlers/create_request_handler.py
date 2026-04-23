"""
CreateRequestHandler: обработчик команды создания бага.
"""
from datetime import datetime

from application.command.create_request_command import CreateRequestCommand


class CreateRequestHandler:
    """
    Pipeline:
    1) validate command
    2) create write-model
    3) persist via repository
    4) publish events (optional)
    """

    def __init__(self, request_repository, event_publisher=None):
        self.request_repository = request_repository
        self.event_publisher = event_publisher

    def handle(self, command: CreateRequestCommand) -> str:
        bug_id = self._generate_request_id()
        bug_write_model = {
            "request_id": bug_id,
            "reporter_id": command.reporter_id,
            "project_id": command.project_id,
            "title": command.title,
            "description": command.description,
            "priority": command.priority,
            "status": "DRAFT",
            "created_at": datetime.now(),
            "assigned_group_id": None,
        }

        self.request_repository.save(bug_write_model)
        if self.event_publisher:
            self.event_publisher.publish(
                {"event_type": "BugCreated", "request_id": bug_id, "project_id": command.project_id}
            )
        return bug_id

    def _generate_request_id(self) -> str:
        year = datetime.now().year
        return f"BUG-{year}-0001"
