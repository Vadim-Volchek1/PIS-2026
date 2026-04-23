"""
Domain events for bug lifecycle.
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class GroupAssignedToRequest:
    request_id: str
    group_id: str
    occurred_at: datetime


@dataclass(frozen=True)
class RequestActivated:
    request_id: str
    group_id: str
    zone_name: str
    occurred_at: datetime


@dataclass(frozen=True)
class RequestZoneChanged:
    request_id: str
    old_zone: str
    new_zone: str
    occurred_at: datetime


@dataclass(frozen=True)
class RequestCompleted:
    request_id: str
    outcome: str  # RESOLVED, REJECTED
    occurred_at: datetime
