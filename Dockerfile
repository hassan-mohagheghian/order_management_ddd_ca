FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY src ./src
COPY entrypoint.sh ./entrypoint.sh

ENV PYTHONPATH=/app/src

EXPOSE 8000


CMD ["./entrypoint.sh"]

