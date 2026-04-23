"""
Unit tests for query handlers.
"""
import pytest
from unittest.mock import Mock

from application.query.get_request_by_id_query import GetRequestByIdQuery
from application.query.handlers.get_request_by_id_handler import GetRequestByIdHandler


class TestGetRequestByIdHandler:
    def test_should_return_bug_dto(self):
        repository = Mock()
        repository.find_by_id.return_value = {
            "request_id": "BUG-2026-0001",
            "reporter_id": "qa.petrov",
            "project_id": "PIS-WEB",
            "title": "Ошибка авторизации",
            "priority": "HIGH",
            "status": "DRAFT",
            "assigned_group_id": None,
            "created_at": None,
        }
        handler = GetRequestByIdHandler(repository)

        result = handler.handle(GetRequestByIdQuery(request_id="BUG-2026-0001"))

        assert result.request_id == "BUG-2026-0001"
        assert result.priority == "HIGH"
        repository.find_by_id.assert_called_once_with("BUG-2026-0001")

    def test_should_raise_for_missing_bug(self):
        repository = Mock()
        repository.find_by_id.return_value = None
        handler = GetRequestByIdHandler(repository)

        with pytest.raises(ValueError):
            handler.handle(GetRequestByIdQuery(request_id="BUG-2026-4040"))
