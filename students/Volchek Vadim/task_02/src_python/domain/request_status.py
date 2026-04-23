"""
Domain Layer: Bug status enum.
"""
from enum import Enum


class BugStatus(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"
