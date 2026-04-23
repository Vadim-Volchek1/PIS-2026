"""
RequestDto: read-модель бага.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class RequestDto:
    request_id: str
    reporter_id: str
    project_id: str
    title: str
    priority: str
    status: str
    assigned_group_id: Optional[str]
    created_at: Optional[datetime]
