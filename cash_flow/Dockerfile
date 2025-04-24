FROM python:3.11-slim

WORKDIR /app
COPY . /app/

RUN pip install django

RUN python manage.py migrate
RUN python manage.py shell -c "exec(open('generate_data.py', encoding='utf-8').read())"

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]