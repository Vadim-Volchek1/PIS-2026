"""
Unit tests for value objects.
"""
import pytest

from domain.models.phone_number import PhoneNumber
from domain.models.zone import Zone


class TestZoneValueObject:
    def test_should_create_valid_priority_zone(self):
        zone = Zone("CRITICAL", (1.0, 4.0, 0.0, 0.0))
        assert zone.name == "CRITICAL"
        assert zone.contains_point(2.0) is True

    def test_should_reject_unknown_priority(self):
        with pytest.raises(ValueError):
            Zone("BLOCKER", (1.0, 4.0, 0.0, 0.0))

    def test_should_reject_invalid_sla_window(self):
        with pytest.raises(ValueError):
            Zone("HIGH", (10.0, 5.0, 0.0, 0.0))


class TestPhoneNumberValueObject:
    def test_should_accept_valid_phone(self):
        number = PhoneNumber("+375291112233")
        assert number.number == "+375291112233"

    def test_should_reject_phone_without_plus(self):
        with pytest.raises(ValueError):
            PhoneNumber("375291112233")

    def test_should_reject_phone_with_non_digits(self):
        with pytest.raises(ValueError):
            PhoneNumber("+37529ABC123")
