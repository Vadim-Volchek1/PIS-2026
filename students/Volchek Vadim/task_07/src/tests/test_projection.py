import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from cqrs import BugAssigned, BugCreated, ReadModelStore


def test_projection_updates_read_model() -> None:
    store = ReadModelStore()
    store.apply(BugCreated("BUG-7-1", "PIS-API", "Crash on save", "HIGH"))
    store.apply(BugAssigned("BUG-7-1", "Backend"))
    row = store.rows["BUG-7-1"]
    assert row["group_name"] == "Backend"
