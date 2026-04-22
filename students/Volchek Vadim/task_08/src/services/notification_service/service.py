def build_notification(event: dict) -> str:
    if event.get("event_type") == "BugCreated":
        return f"Создан баг {event['bug_id']}: {event['title']}"
    if event.get("event_type") == "BugAssigned":
        return f"Баг {event['bug_id']} назначен на {event['group_name']}"
    return "Неизвестное событие"
