"""
PhoneNumber: Value Object контакта ответственного.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class PhoneNumber:
    number: str

    def __post_init__(self):
        if not self.number.startswith("+"):
            raise ValueError("Phone must start with '+'")
        digits = self.number[1:]
        if not digits.isdigit():
            raise ValueError("Phone must contain digits only")
        if len(digits) < 10 or len(digits) > 15:
            raise ValueError("Phone length must be in range 10..15")
