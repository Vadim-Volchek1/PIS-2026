from unittest.mock import Mock
from application.command.create_request_command import CreateRequestCommand
from application.command.handlers.create_request_handler import CreateRequestHandler


class TestCreateBugHandler:
    def test_should_create_and_save_bug(self):
        repository = Mock()
        publisher = Mock()
        handler = CreateRequestHandler(repository, publisher)

        command = CreateRequestCommand(
            reporter_id="qa.petrov",
            project_id="PIS-WEB",
            title="Не работает авторизация",
            description="500 на /api/auth/login",
            priority="HIGH",
        )

        bug_id = handler.handle(command)

        assert bug_id.startswith("BUG-")
        repository.save.assert_called_once()

    def test_should_propagate_repository_error(self):
        repository = Mock()
        repository.save.side_effect = RuntimeError("DB unavailable")
        handler = CreateRequestHandler(repository, None)

        command = CreateRequestCommand(
            reporter_id="qa.petrov",
            project_id="PIS-WEB",
            title="Не работает авторизация",
            description="500 на /api/auth/login",
            priority="HIGH",
        )

        try:
            handler.handle(command)
            assert False, "Expected RuntimeError"
        except RuntimeError as exc:
            assert "DB unavailable" in str(exc)
