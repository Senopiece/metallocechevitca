## Dockerized

### Single Container

#### Using docker-compose

There is a prepared docker-compose configuration, so that you can just run

```bash
docker compose up --build
```

Tweak port mapping and environment variables if necessary

## Developing

Install poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

And then the dependencies:
```bash
poetry install
```

Run the server in development mode
```bash
uvicorn app.main:app --host 0.0.0.0 --port 9090 --reload
```