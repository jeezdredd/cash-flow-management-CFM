FROM python:3.11-slim

WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py migrate

# Заполнение тестовыми данными БД
RUN if [ -f generate_data.py ]; then python manage.py shell -c "exec(open('generate_data.py', encoding='utf-8').read())"; fi

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]