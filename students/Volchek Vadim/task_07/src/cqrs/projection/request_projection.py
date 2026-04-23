"""
Projection handler: events -> bug read model.
"""
from datetime import datetime
from sqlalchemy.orm import Session

from cqrs.read_model.request_view import RequestViewORM


class RequestProjection:
    def __init__(self, session: Session):
        self.session = session

    def on_bug_created(self, event: dict) -> None:
        row = RequestViewORM(
            request_id=event["request_id"],
            status="DRAFT",
            project_id=event["project_id"],
            project_name=event.get("project_name", "Unknown project"),
            reporter_id=event["reporter_id"],
            assignee_id=None,
            priority=event["priority"],
            title=event["title"],
            created_at=event.get("occurred_at", datetime.now()),
            activated_at=None,
            completed_at=None,
            duration_minutes=None,
            sla_hours=float(event.get("sla_hours", 24)),
        )
        self.session.add(row)
        self.session.commit()

    def on_bug_assigned(self, event: dict) -> None:
        row = self.session.query(RequestViewORM).filter_by(request_id=event["request_id"]).first()
        if not row:
            return
        row.assignee_id = event["assignee_id"]
        row.status = "ASSIGNED"
        self.session.commit()

    def on_bug_activated(self, event: dict) -> None:
        row = self.session.query(RequestViewORM).filter_by(request_id=event["request_id"]).first()
        if not row:
            return
        row.status = "ACTIVE"
        row.activated_at = event.get("occurred_at", datetime.now())
        self.session.commit()

    def on_bug_closed(self, event: dict) -> None:
        row = self.session.query(RequestViewORM).filter_by(request_id=event["request_id"]).first()
        if not row:
            return
        closed_at = event.get("occurred_at", datetime.now())
        row.status = "COMPLETED"
        row.completed_at = closed_at
        if row.activated_at:
            row.duration_minutes = int((closed_at - row.activated_at).total_seconds() / 60)
        self.session.commit()
