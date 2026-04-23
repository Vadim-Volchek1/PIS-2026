# gRPC - Быстрый старт

## 1) Установка зависимостей

```bash
pip install -r requirements.txt
```

## 2) Генерация кода из `.proto`

```bash
python -m grpc_tools.protoc \
  -I./proto \
  --python_out=./generated \
  --grpc_python_out=./generated \
  ./proto/request_service.proto
```

Для Windows PowerShell:

```powershell
python -m grpc_tools.protoc `
  -I./proto `
  --python_out=./generated `
  --grpc_python_out=./generated `
  ./proto/request_service.proto
```

## 3) Запуск сервера

```bash
python server/request_service_server.py
```

## 4) Запуск клиента

```bash
python client/request_service_client.py
```

## 5) Streaming

В `client/request_service_client.py` раскомментируйте:

```python
stream_active_requests(stub)
```

и снова запустите клиент.
