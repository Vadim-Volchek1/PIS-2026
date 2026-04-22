# Лабораторная работа №5

**Студент:** Волчек Вадим Александрович  
**Вариант:** 11 — Баг-трекер "Не баг, а фича?"

## Тема
Инфраструктурный слой: API, БД, адаптеры, конфигурация.

## Реализовано
- HTTP API (FastAPI) для создания/чтения/назначения багов.
- SQLAlchemy-модель `BugModel`.
- Репозиторий `SqlAlchemyBugRepository`.
- Конфигурация PostgreSQL через `DATABASE_URL`.
- `docker-compose.yml` для локального запуска PostgreSQL.

## Эндпоинты
- `POST /api/bugs`
- `POST /api/bugs/{bug_id}/assign`
- `GET /api/bugs/{bug_id}`
- `GET /api/bugs`
