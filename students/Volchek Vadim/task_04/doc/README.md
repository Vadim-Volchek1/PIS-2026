# Лабораторная работа №4

**Студент:** Волчек Вадим Александрович  
**Вариант:** 11 — Баг-трекер "Не баг, а фича?"

## Тема
Уровень приложения: CQRS, команды, запросы, обработчики.

## Реализовано
- Command: `CreateBugCommand`, `AssignBugCommand`.
- Query: `GetBugQuery`.
- Handler'ы для команд и запросов.
- Фасад `BugApplicationService`.
- Unit-тесты для handler'ов.

## Поток обработки команд
`validate -> load/create aggregate -> execute domain method -> save -> return result`.
