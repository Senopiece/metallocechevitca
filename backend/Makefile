fix:
	poetry run isort --py 311 app && \
	poetry run black -t py311 app

build:
	docker compose up --build

run:
	docker compose up