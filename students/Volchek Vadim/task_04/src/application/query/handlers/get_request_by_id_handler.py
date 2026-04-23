"""
GetRequestByIdHandler: обработчик чтения бага.
"""
from application.query.get_request_by_id_query import GetRequestByIdQuery
from application.query.dto.request_dto import RequestDto


class GetRequestByIdHandler:
    def __init__(self, request_repository):
        self.request_repository = request_repository

    def handle(self, query: GetRequestByIdQuery) -> RequestDto:
        row = self.request_repository.find_by_id(query.request_id)
        if not row:
            raise ValueError(f"Bug {query.request_id} не найден")
        return self._map_to_dto(row)

    def _map_to_dto(self, row: dict) -> RequestDto:
        return RequestDto(
            request_id=row["request_id"],
            reporter_id=row["reporter_id"],
            project_id=row["project_id"],
            title=row["title"],
            priority=row["priority"],
            status=row["status"],
            assigned_group_id=row.get("assigned_group_id"),
            created_at=row.get("created_at"),
        )
