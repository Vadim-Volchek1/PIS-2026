# Лабораторная работа №3

**Студент:** Волчек Вадим Александрович  
**Вариант:** 11 — Баг-трекер "Не баг, а фича?"

## Тема
Доменный слой (Entity, Value Object, Aggregate, Domain Events).

## Реализовано
- Value Objects: `BugTitle`, `Priority`, `BugStatus`, `Attachment`.
- Entity: `Bug`.
- Aggregate Root: `BugAggregate`.
- Domain Event: `BugAssigned`.
- Unit-тесты инвариантов.

## Инварианты
1. Заголовок бага не пустой.
2. Приоритет только из допустимого списка.
3. Закрытый баг нельзя назначать на группу.
