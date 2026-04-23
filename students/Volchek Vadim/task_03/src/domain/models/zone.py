"""
Zone: Value Object приоритета бага.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Zone:
    """
    Value Object, где name - уровень приоритета,
    bounds - SLA в часах (min, max, _, _).
    """

    name: str
    bounds: tuple[float, float, float, float]

    def __post_init__(self):
        allowed = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
        if self.name not in allowed:
            raise ValueError(f"Unknown priority {self.name}")

        min_h, max_h, _, _ = self.bounds
        if min_h < 0 or max_h < 0 or min_h >= max_h:
            raise ValueError("Некорректное SLA-окно")

    def contains_point(self, value: float, _: float = 0.0) -> bool:
        min_h, max_h, _, _ = self.bounds
        return min_h <= value <= max_h
