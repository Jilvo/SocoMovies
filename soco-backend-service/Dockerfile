FROM python:3.12-slim

ENV POETRY_VERSION=2.1.0 \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION" \
    && poetry env activate \
    && poetry lock \
    && poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]