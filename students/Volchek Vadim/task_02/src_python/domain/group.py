"""
Domain Layer: Project entity.
"""


class Project:
    """Entity: Project."""

    def __init__(self, project_id: str, name: str, active: bool = True):
        if not project_id.strip():
            raise ValueError("project_id обязателен")
        if not name.strip():
            raise ValueError("Название проекта обязательно")

        self._id = project_id.strip()
        self._name = name.strip()
        self._active = active

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_active(self) -> bool:
        return self._active
