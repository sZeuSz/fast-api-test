FROM python:3.12.8-alpine AS builder

WORKDIR /app

RUN apk add --no-cache \
    gcc musl-dev libffi-dev build-base python3-dev postgresql-dev

ENV POETRY_VERSION="2.0.1"
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-interaction --no-ansi

COPY ./app /app/app
COPY alembic.ini ./
COPY ./database ./database

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
