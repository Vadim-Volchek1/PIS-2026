### Инварианты агрегата BugRequest

| **Инвариант** | **Проверка** | **Где выполняется** | **Исключение** |
|---------------|--------------|----------------------|-----------------|
| Нельзя назначить команду для бага не в статусе DRAFT | `if self.status != RequestStatus.DRAFT` | `Request.assign_group()` | `ValueError("Нельзя назначить команду не для DRAFT-бага")` |
| Команда должна быть готова перед назначением | `if not group.is_ready()` | `Request.assign_group()` | `ValueError("Команда должна содержать 1-3 активных разработчиков")` |
| Нельзя перевести баг в работу без назначенной команды | `if self.assigned_group is None` | `Request.activate()` | `ValueError("Нельзя перевести баг в IN_PROGRESS без команды")` |
| Нельзя активировать баг из статуса, отличного от DRAFT | `if self.status != RequestStatus.DRAFT` | `Request.activate()` | `ValueError("Нельзя активировать баг в статусе ...")` |
| Нельзя менять приоритет у закрытого бага | `if self.status == RequestStatus.COMPLETED` | `Request.change_zone()` | `ValueError("Нельзя менять приоритет закрытого бага")` |
| Закрытие бага допускает только валидный outcome | `if outcome not in ("RESOLVED", "REJECTED")` | `Request.complete()` | `ValueError("Outcome должен быть RESOLVED или REJECTED")` |
| Нельзя закрыть уже закрытый баг | `if self.status == RequestStatus.COMPLETED` | `Request.complete()` | `ValueError("Баг уже закрыт")` |
| Размер команды исправления ограничен | `MIN_MEMBERS <= len(_members) <= MAX_MEMBERS` | `Group.add_member()`, `Group.mark_ready()` | `ValueError` |
| Разработчик в команде должен быть уникальным | `if user_id in self._members` | `Group.add_member()` | `ValueError("Developer ... already in the team")` |
| Приоритет бага должен быть из фиксированного набора | `if self.name not in {"LOW","MEDIUM","HIGH","CRITICAL"}` | `Zone.__post_init__()` | `ValueError("Unknown priority ...")` |
# Инварианты агрегата `Bug`

## Aggregate Root
Корень агрегата: `Bug` (`src/domain/models/bug.py`).

## Назначение агрегата
Агрегат инкапсулирует жизненный цикл дефекта: создание, назначение исполнителя, смену статусов и управление вложениями. Внешний код не должен обходить публичные методы агрегата.

## Инварианты

| N | Инвариант | Нарушение | Реакция |
|---|-----------|-----------|---------|
| 1 | Закрытый баг нельзя назначать | `status == CLOSED` и вызов `assign_to()` | `DomainException("Cannot assign closed bug")` |
| 2 | Разрешены только корректные переходы статусов | переход отсутствует в карте переходов | `DomainException("Invalid status transition ...")` |
| 3 | Максимум 10 вложений на один баг | `len(attachments) >= 10` | `DomainException("Cannot attach more than 10 files")` |
| 4 | Заголовок бага не может быть пустым | пустая строка в `BugTitle` | `DomainException("Bug title cannot be empty")` |
| 5 | Приоритет должен быть валидным | значение вне LOW/MEDIUM/HIGH/CRITICAL | `DomainException("Priority must be one of ...")` |

## Где реализованы проверки

- `src/domain/models/bug.py`
  - `assign_to()` - инвариант 1
  - `change_status()` - инвариант 2
  - `add_attachment()` - инвариант 3
- `src/domain/value_objects/bug_title.py` - инвариант 4
- `src/domain/value_objects/priority_value.py` - инвариант 5

## Фрагмент кода

```python
def add_attachment(self, attachment: AttachmentRef) -> None:
    if len(self.attachments) >= 10:
        raise DomainException("Cannot attach more than 10 files")
    self.attachments.append(attachment)
```

## Проверка инвариантов тестами

Файл: `src/tests/test_bug_invariants.py`

- `test_closed_bug_cannot_be_assigned`
- `test_status_transition_should_follow_flow`
- `test_bug_accepts_no_more_than_10_attachments`
- `test_bug_title_cannot_be_empty`
- `test_priority_should_be_from_allowed_set`

## Вывод
Инварианты зафиксированы на уровне доменной модели и не зависят от инфраструктуры. Это позволяет безопасно переиспользовать доменную логику в разных адаптерах (REST, gRPC, batch).

