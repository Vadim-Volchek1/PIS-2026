from dataclasses import dataclass


@dataclass
class Bug:
    bug_id: str
    title: str
    status: str
    group: str | None = None


def test_e2e_lifecycle() -> None:
    bug = Bug("BUG-E2E-1", "Cannot attach screenshot", "OPEN")
    bug.group = "Backend"
    bug.status = "IN_PROGRESS"
    assert bug.group == "Backend"
    assert bug.status == "IN_PROGRESS"
