FROM python:3.10.1-alpine3.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DB_HOST = "192.168.42.154"

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt
RUN pip install cryptography

COPY . /app

CMD ["python", "colegio/manage.py", "runserver", "0.0.0.0:8000"]