"""
GetRequestByIdQuery: запрос бага по ID.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class GetRequestByIdQuery:
    request_id: str

    def __post_init__(self):
        if not self.request_id:
            raise ValueError("request_id обязателен")
