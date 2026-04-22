def assign_bug_to_group(bug_id: str, group_name: str) -> dict:
    return {
        "event_type": "BugAssigned",
        "bug_id": bug_id,
        "group_name": group_name,
    }
