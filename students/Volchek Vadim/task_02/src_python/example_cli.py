"""
CLI example for Bug Service.
"""
from application.port.inbound import CreateBugCommand
from infrastructure.config import get_container


def main():
    print("=" * 60)
    print("Bug Service - Вариант 11")
    print("Гексагональная архитектура")
    print("=" * 60)

    service = get_container().get_bug_service()
    command = CreateBugCommand(
        project_id="PIS-WEB",
        project_name="PIS Web",
        title="Падение при загрузке вложения > 10MB",
        description="HTTP 500 на /api/attachments",
        priority="HIGH",
        assignee_id="dev.volkov",
    )

    bug_id = service.create_bug(command)
    print(f"Создан баг: {bug_id}")


if __name__ == "__main__":
    main()
