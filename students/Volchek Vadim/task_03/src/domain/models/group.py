"""
Group: команда разработчиков, назначаемая на баг.
"""
from typing import List


class Group:
    """
    Entity команды.

    Инварианты:
    - Минимум 1 разработчик, максимум 3.
    - Участники уникальны.
    - Нельзя менять состав после статуса READY.
    """

    MIN_MEMBERS = 1
    MAX_MEMBERS = 3

    def __init__(self, group_id: str, leader_id: str):
        if not group_id:
            raise ValueError("Group ID cannot be empty")
        if not leader_id:
            raise ValueError("Leader ID cannot be empty")
        self._id = group_id
        self._leader_id = leader_id
        self._members: List[str] = []
        self._status = "FORMING"

    @property
    def group_id(self) -> str:
        return self._id

    @property
    def member_count(self) -> int:
        return len(self._members)

    def add_member(self, user_id: str) -> None:
        if self._status != "FORMING":
            raise ValueError(f"Cannot modify group in status {self._status}")
        if len(self._members) >= self.MAX_MEMBERS:
            raise ValueError("Too many developers in bug-fix team")
        if user_id in self._members:
            raise ValueError(f"Developer {user_id} already in the team")
        self._members.append(user_id)

    def mark_ready(self) -> None:
        if len(self._members) < self.MIN_MEMBERS:
            raise ValueError("At least one developer must be assigned")
        self._status = "READY"

    def is_ready(self) -> bool:
        return self._status == "READY" and self.MIN_MEMBERS <= len(self._members) <= self.MAX_MEMBERS

    def __eq__(self, other):
        return isinstance(other, Group) and self._id == other._id

    def __hash__(self):
        return hash(self._id)
