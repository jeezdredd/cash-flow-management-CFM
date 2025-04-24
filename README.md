# Руководство по проекту Cash Flow

## 1. Установка зависимостей

```bash
# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
# Для Windows:
venv\Scripts\activate
# Для Linux/Mac:
# source venv/bin/activate

# Установка Django
pip install django
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
