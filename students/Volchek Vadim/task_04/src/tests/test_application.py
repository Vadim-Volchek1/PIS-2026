import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from application import (
    AssignBugCommand,
    BugApplicationService,
    CreateBugCommand,
    GetBugQuery,
)


def test_create_and_get_bug() -> None:
    app = BugApplicationService()
    bug_id = app.create_handler.handle(CreateBugCommand("PIS-API", "Error 500", "HIGH"))
    loaded = app.get_handler.handle(GetBugQuery(bug_id))
    assert loaded["title"] == "Error 500"


def test_assign_closed_bug_fails() -> None:
    app = BugApplicationService()
    bug_id = app.create_handler.handle(CreateBugCommand("PIS-API", "Error 500", "HIGH"))
    bug = app.repo.get(bug_id)
    bug["status"] = "CLOSED"
    app.repo.save(bug)
    with pytest.raises(ValueError):
        app.assign_handler.handle(AssignBugCommand(bug_id, "Backend"))
