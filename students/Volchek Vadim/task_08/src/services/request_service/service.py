def create_bug_event_payload(bug_id: str, project_id: str, title: str, priority: str) -> dict:
    return {
        "event_type": "BugCreated",
        "bug_id": bug_id,
        "project_id": project_id,
        "title": title,
        "priority": priority,
    }
