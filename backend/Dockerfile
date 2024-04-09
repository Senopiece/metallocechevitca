FROM python:3.11

WORKDIR /code

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV:-dev} \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.6.1

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml /code/

RUN poetry install $(test "$YOUR_ENV" == production && echo "--only=main") --no-interaction --no-ansi

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
