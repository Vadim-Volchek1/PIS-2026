"""
Application Layer: inbound port for bug creation.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CreateBugCommand:
    project_id: str
    project_name: str
    title: str
    description: str
    priority: str
    assignee_id: str


class CreateBugUseCase(ABC):
    @abstractmethod
    def create_bug(self, command: CreateBugCommand) -> str:
        """Create bug and return BUG id."""
        pass
