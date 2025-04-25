# Руководство по проекту Cash Flow

## 1. Установка зависимостей

```bash
# Создание виртуального окружения
python -m venv venv
# Активация виртуального окружения
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Установка зависимостей
pip install -r requirements.txt
```

## 2. Настройка базы данных

В проекте используется SQLite, поэтому дополнительная установка СУБД не требуется:

```bash
# Создание структуры базы данных
python manage.py migrate

# Создание суперпользователя для доступа к админ-панели
python manage.py createsuperuser
```

### Наполнение базы тестовыми данными

```bash
# Запуск Django shell
python manage.py shell

# В открывшейся консоли вставьте код из файла generate_data.py
# или выполните:
exec(open('generate_data.py', encoding='utf-8').read())
```

## 3. Запуск веб-сервиса

```bash
python manage.py runserver
```

После запуска приложение будет доступно по адресу: http://127.0.0.1:8000/

## 4. Создание демо-версии

### Вариант с Docker

1. Убедитесь, что Docker установлен
2. Выполните команды:

```bash
# Сборка Docker-образа
docker build -t cash-flow-demo .

# Запуск контейнера
docker run -p 8000:8000 cash-flow-demo
```

После запуска контейнера демо-версия будет доступна по адресу: http://localhost:8000/

## Тестирование через Postman
### 1. Установка Postman
- Установите Postman 
- Создайте новый запрос
- Для получения данных используйте метод GET, для создания - POST

### Пример запроса:
- Создание транзакции:
```http
POST http://127.0.0.1:8000/api/transactions/
```
```json
{
  "created_at": "2024-06-01",
  "date": "2024-06-10",
  "status": 7,
  "type": 4,
  "category": 5,
  "subcategory": 6,
  "amount": "1500.00",
  "comment": "Тестовая транзакция"
}
```

