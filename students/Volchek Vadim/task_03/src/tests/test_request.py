"""
Юнит-тесты агрегата Request (bug lifecycle).
"""
import pytest

from domain.models.request import Request
from domain.models.group import Group
from domain.models.zone import Zone
from domain.events.request_events import GroupAssignedToRequest, RequestActivated


def _ready_group() -> Group:
    group = Group("TEAM-BE", "dev.lead")
    group.add_member("dev.ivanov")
    group.mark_ready()
    return group


def test_should_not_activate_without_group():
    bug = Request("BUG-2026-0001", "qa.petrov", Zone("HIGH", (4.0, 24.0, 0.0, 0.0)))
    with pytest.raises(ValueError, match="без команды"):
        bug.activate()


def test_should_register_event_when_group_assigned():
    bug = Request("BUG-2026-0002", "qa.petrov", Zone("CRITICAL", (1.0, 8.0, 0.0, 0.0)))
    group = _ready_group()
    bug.assign_group(group)
    events = bug.get_events()
    assert len(events) == 1
    assert isinstance(events[0], GroupAssignedToRequest)


def test_should_register_event_when_activated():
    bug = Request("BUG-2026-0003", "qa.petrov", Zone("MEDIUM", (24.0, 72.0, 0.0, 0.0)))
    bug.assign_group(_ready_group())
    bug.activate()
    events = bug.get_events()
    assert any(isinstance(event, RequestActivated) for event in events)


def test_should_not_change_priority_for_completed_bug():
    bug = Request("BUG-2026-0004", "qa.petrov", Zone("LOW", (72.0, 120.0, 0.0, 0.0)))
    bug.assign_group(_ready_group())
    bug.activate()
    bug.complete("RESOLVED")
    with pytest.raises(ValueError, match="закрытого бага"):
        bug.change_zone(Zone("CRITICAL", (1.0, 8.0, 0.0, 0.0)))
