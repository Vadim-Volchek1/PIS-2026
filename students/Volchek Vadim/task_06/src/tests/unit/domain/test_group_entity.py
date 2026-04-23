"""
Unit tests for Group entity.
"""
import pytest

from domain.models.group import Group


class TestGroupEntity:
    def test_should_create_group_in_forming_status(self):
        group = Group("TEAM-WEB", "lead.sidorov")
        assert group.group_id == "TEAM-WEB"
        assert group.member_count == 0

    def test_should_add_unique_members(self):
        group = Group("TEAM-BACKEND", "lead.ivanov")
        group.add_member("dev.1")
        group.add_member("dev.2")

        assert group.member_count == 2

    def test_should_not_add_duplicate_member(self):
        group = Group("TEAM-BACKEND", "lead.ivanov")
        group.add_member("dev.1")

        with pytest.raises(ValueError):
            group.add_member("dev.1")

    def test_should_not_exceed_max_members(self):
        group = Group("TEAM-CORE", "lead.petrov")
        group.add_member("dev.1")
        group.add_member("dev.2")
        group.add_member("dev.3")

        with pytest.raises(ValueError):
            group.add_member("dev.4")

    def test_should_mark_group_ready(self):
        group = Group("TEAM-MOBILE", "lead.orlov")
        group.add_member("dev.1")
        group.mark_ready()

        assert group.is_ready() is True
