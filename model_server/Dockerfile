FROM python:3.11

WORKDIR /code

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV:-production} \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.6.1

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml /code/

RUN poetry install $(test "$YOUR_ENV" == production && echo "--only=main") --no-interaction --no-ansi
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/clip-ViT-B-32-multilingual-v1'); SentenceTransformer('clip-ViT-B-32')"

COPY ./app /code/app
COPY ./serve-config.yaml /code

EXPOSE 8000
EXPOSE 8265
CMD ["sh" , "-c", "ray start --dashboard-host 0.0.0.0 --head && serve run serve-config.yaml"]
