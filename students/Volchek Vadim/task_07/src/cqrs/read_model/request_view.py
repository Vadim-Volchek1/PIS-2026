"""
Read model for bug tracker (denormalized projection).
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import declarative_base


@dataclass
class RequestView:
    request_id: str
    status: str
    project_id: str
    project_name: str
    reporter_id: str
    assignee_id: Optional[str]
    priority: str
    title: str
    created_at: datetime
    activated_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    duration_minutes: Optional[int] = None


Base = declarative_base()


class RequestViewORM(Base):
    __tablename__ = "bug_view"

    request_id = Column(String(50), primary_key=True, index=True)
    status = Column(String(20), nullable=False, index=True)
    project_id = Column(String(50), nullable=False, index=True)
    project_name = Column(String(255), nullable=False)
    reporter_id = Column(String(50), nullable=False)
    assignee_id = Column(String(50), nullable=True, index=True)
    priority = Column(String(20), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    activated_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    sla_hours = Column(Float, nullable=True)
