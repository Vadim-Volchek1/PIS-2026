import pytest
from domain.models.request import Request
from domain.models.group import Group
from domain.models.zone import Zone
from domain.models.request_status import RequestStatus


class TestBugAggregateInvariants:
    def test_should_create_bug_in_draft_status(self):
        zone = Zone("HIGH", (4.0, 24.0, 0.0, 0.0))
        bug = Request("BUG-2026-0001", "qa.petrov", zone)

        assert bug.status == RequestStatus.DRAFT
        assert bug.assigned_group is None

    def test_should_not_activate_bug_without_assignee(self):
        zone = Zone("HIGH", (4.0, 24.0, 0.0, 0.0))
        bug = Request("BUG-2026-0002", "qa.petrov", zone)

        with pytest.raises(ValueError):
            bug.activate()

    def test_should_not_assign_unready_team(self):
        zone = Zone("HIGH", (4.0, 24.0, 0.0, 0.0))
        bug = Request("BUG-2026-0003", "qa.petrov", zone)
        team = Group("TEAM-BACKEND", "lead.ivanov")

        with pytest.raises(ValueError):
            bug.assign_group(team)

    def test_should_change_state_draft_active_completed(self):
        zone = Zone("MEDIUM", (8.0, 72.0, 0.0, 0.0))
        bug = Request("BUG-2026-0004", "qa.petrov", zone)
        team = Group("TEAM-WEB", "lead.sidorov")
        team.add_member("dev.1")
        team.add_member("dev.2")
        team.mark_ready()

        bug.assign_group(team)
        bug.activate()
        bug.complete("RESOLVED")

        assert bug.status == RequestStatus.COMPLETED
