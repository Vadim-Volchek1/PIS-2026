"""
RequestStatus: статус бага.
"""
from enum import Enum


class RequestStatus(Enum):
    DRAFT = "DRAFT"          # OPEN
    ACTIVE = "ACTIVE"        # IN_PROGRESS
    COMPLETED = "COMPLETED"  # CLOSED
    CANCELLED = "CANCELLED"  # REJECTED

    def can_transition_to(self, new_status: "RequestStatus") -> bool:
        valid = {
            RequestStatus.DRAFT: {RequestStatus.ACTIVE, RequestStatus.CANCELLED},
            RequestStatus.ACTIVE: {RequestStatus.COMPLETED, RequestStatus.CANCELLED},
            RequestStatus.COMPLETED: set(),
            RequestStatus.CANCELLED: set(),
        }
        return new_status in valid[self]
