import pytest


def validate_priority(priority: str) -> None:
    if priority not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
        raise ValueError("INVALID_PRIORITY")


def test_priority_valid() -> None:
    validate_priority("HIGH")


def test_priority_invalid() -> None:
    with pytest.raises(ValueError):
        validate_priority("URGENT")
