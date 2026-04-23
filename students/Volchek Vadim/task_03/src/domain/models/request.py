"""
BugRequest (Aggregate Root): заявка на исправление бага.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from domain.models.group import Group
from domain.models.zone import Zone
from domain.models.request_status import RequestStatus
from domain.events.request_events import (
    GroupAssignedToRequest,
    RequestActivated,
    RequestZoneChanged,
    RequestCompleted,
)


@dataclass
class Request:
    """
    Aggregate Root для бага.

    Инварианты:
    - Нельзя взять баг в работу без назначенной команды.
    - Назначение команды возможно только в статусе DRAFT.
    - Нельзя менять приоритет закрытого бага.
    """

    request_id: str
    coordinator_id: str  # reporter_id
    zone: Zone  # приоритет бага
    status: RequestStatus = field(default_factory=lambda: RequestStatus.DRAFT)
    assigned_group: Optional[Group] = None
    created_at: datetime = field(default_factory=datetime.now)
    activated_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    _events: List = field(default_factory=list, repr=False, compare=False)

    def assign_group(self, group: Group) -> None:
        if self.status != RequestStatus.DRAFT:
            raise ValueError("Нельзя назначить команду не для DRAFT-бага")
        if not group.is_ready():
            raise ValueError("Команда должна содержать 1-3 активных разработчиков")

        self.assigned_group = group
        self._events.append(
            GroupAssignedToRequest(
                request_id=self.request_id,
                group_id=group.group_id,
                occurred_at=datetime.now(),
            )
        )

    def activate(self) -> None:
        if self.assigned_group is None:
            raise ValueError("Нельзя перевести баг в IN_PROGRESS без команды")
        if self.status != RequestStatus.DRAFT:
            raise ValueError(f"Нельзя активировать баг в статусе {self.status.value}")

        self.status = RequestStatus.ACTIVE
        self.activated_at = datetime.now()
        self._events.append(
            RequestActivated(
                request_id=self.request_id,
                group_id=self.assigned_group.group_id,
                zone_name=self.zone.name,
                occurred_at=self.activated_at,
            )
        )

    def change_zone(self, new_zone: Zone) -> None:
        if self.status == RequestStatus.COMPLETED:
            raise ValueError("Нельзя менять приоритет закрытого бага")

        old_zone_name = self.zone.name
        self.zone = new_zone
        self._events.append(
            RequestZoneChanged(
                request_id=self.request_id,
                old_zone=old_zone_name,
                new_zone=new_zone.name,
                occurred_at=datetime.now(),
            )
        )

    def complete(self, outcome: str) -> None:
        if outcome not in ("RESOLVED", "REJECTED"):
            raise ValueError("Outcome должен быть RESOLVED или REJECTED")
        if self.status == RequestStatus.COMPLETED:
            raise ValueError("Баг уже закрыт")

        self.status = RequestStatus.COMPLETED
        self.completed_at = datetime.now()
        self._events.append(
            RequestCompleted(
                request_id=self.request_id,
                outcome=outcome,
                occurred_at=self.completed_at,
            )
        )

    def get_events(self) -> List:
        return self._events.copy()

    def clear_events(self) -> None:
        self._events.clear()

    def __eq__(self, other):
        if not isinstance(other, Request):
            return False
        return self.request_id == other.request_id

    def __hash__(self):
        return hash(self.request_id)
