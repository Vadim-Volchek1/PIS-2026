# Лабораторная работа №2

**Студент:** Волчек Вадим Александрович  
**Вариант:** 11 — Баг-трекер "Не баг, а фича?"

## Тема
Гексагональная архитектура (Ports & Adapters).

## Цель
Построить каркас bug-tracker сервиса по Ports & Adapters с изоляцией домена от инфраструктуры.

## Структура
- `src/domain/` — доменные сущности.
- `src/application/port/inbound.py` — входные порты.
- `src/application/port/outbound.py` — выходные порты.
- `src/application/service/bug_service.py` — реализация use-case.
- `src/infrastructure/adapter/in/http_controller.py` — входной HTTP-адаптер.
- `src/infrastructure/adapter/out/in_memory_repo.py` — выходной адаптер репозитория.

## Вывод
Зависимости направлены внутрь: инфраструктура знает о портах, но домен не знает об инфраструктуре.
