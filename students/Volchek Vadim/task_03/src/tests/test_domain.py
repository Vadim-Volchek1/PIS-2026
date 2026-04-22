import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from domain import Bug, BugAggregate, BugStatus, BugTitle, Priority


def test_title_cannot_be_empty() -> None:
    with pytest.raises(ValueError):
        BugTitle("   ")


def test_closed_bug_cannot_be_assigned() -> None:
    bug = Bug("BUG-1", "PIS-API", BugTitle("File upload fails"), Priority.HIGH, BugStatus.CLOSED)
    aggregate = BugAggregate(bug)
    with pytest.raises(ValueError):
        aggregate.assign("Backend")


def test_assign_generates_event() -> None:
    bug = Bug("BUG-2", "PIS-API", BugTitle("Crash on login"), Priority.CRITICAL)
    aggregate = BugAggregate(bug)
    aggregate.assign("Backend")
    assert len(aggregate.events) == 1
