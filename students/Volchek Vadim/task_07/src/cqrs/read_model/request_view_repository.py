"""
Repository for reading denormalized bug view.
"""
from datetime import datetime, timedelta
from typing import List, Optional

from sqlalchemy.orm import Session

from cqrs.read_model.request_view import RequestView, RequestViewORM


class RequestViewRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_by_id(self, request_id: str) -> Optional[RequestView]:
        row = self.session.query(RequestViewORM).filter_by(request_id=request_id).first()
        return self._to_dto(row) if row else None

    def find_active_requests(self, limit: int = 100) -> List[RequestView]:
        rows = (
            self.session.query(RequestViewORM)
            .filter_by(status="ACTIVE")
            .order_by(RequestViewORM.created_at.desc())
            .limit(limit)
            .all()
        )
        return [self._to_dto(row) for row in rows]

    def find_by_project(self, project_id: str) -> List[RequestView]:
        rows = self.session.query(RequestViewORM).filter_by(project_id=project_id).all()
        return [self._to_dto(row) for row in rows]

    def find_closed_in_last_days(self, days: int) -> List[RequestView]:
        since = datetime.now() - timedelta(days=days)
        rows = (
            self.session.query(RequestViewORM)
            .filter(
                RequestViewORM.status == "COMPLETED",
                RequestViewORM.completed_at >= since,
            )
            .all()
        )
        return [self._to_dto(row) for row in rows]

    def _to_dto(self, row: RequestViewORM) -> RequestView:
        return RequestView(
            request_id=row.request_id,
            status=row.status,
            project_id=row.project_id,
            project_name=row.project_name,
            reporter_id=row.reporter_id,
            assignee_id=row.assignee_id,
            priority=row.priority,
            title=row.title,
            created_at=row.created_at,
            activated_at=row.activated_at,
            completed_at=row.completed_at,
            duration_minutes=row.duration_minutes,
        )
