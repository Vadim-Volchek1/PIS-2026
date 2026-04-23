# Infrastructure Layer - Bug Service

Примеры реализации инфраструктурного слоя для системы:
**Баг-трекер «Не баг, а фича?»**

---

## Структура

```text
src/
├── infrastructure/
│   ├── adapter/
│   │   ├── in/
│   │   │   └── request_controller.py
│   │   └── out/
│   │       ├── request_repository_impl.py
│   │       └── event_publisher_impl.py
│   ├── config/
│   │   └── database.py
│   └── orm/
│       └── models.py
└── docker-compose.yml
```

---

## Что реализовано

- REST контроллер для сценариев работы с багами.
- Outbound-адаптеры: repository и event publisher.
- ORM-модели PostgreSQL для багов, приоритетов и команд.
- Конфигурация подключения к БД.
- Docker Compose окружение: `app`, `db`, `rabbitmq`, `pgadmin`.
