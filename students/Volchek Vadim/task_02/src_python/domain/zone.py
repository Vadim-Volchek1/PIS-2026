"""
Domain Layer: Priority value object.
"""
from enum import Enum


class Priority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

    @classmethod
    def from_string(cls, raw: str) -> "Priority":
        raw_upper = raw.upper().strip()
        for item in cls:
            if item.value == raw_upper:
                return item
        raise ValueError("Допустимые приоритеты: LOW, MEDIUM, HIGH, CRITICAL")
