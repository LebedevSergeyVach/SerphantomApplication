FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.4.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Add Poetry to PATH
ENV PATH="/opt/poetry/bin:$PATH"

RUN apk update && \
    apk upgrade && \
    apk --no-cache add curl

WORKDIR /app

COPY . .

RUN curl -sSL https://install.python-poetry.org/ | python3 - && \
    poetry install --no-interaction --no-cache \

# Collect static files
RUN poetry run python3 ./advertisements/manage.py collectstatic --noinput

EXPOSE 443

ENTRYPOINT ["poetry", "run", "python3", "./advertisements/manage.py", "runserver_plus", "0.0.0.0:443", "--cert-file", "./certificates/fullchain.crt"]
