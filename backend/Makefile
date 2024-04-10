fix:
	poetry run isort --py 311 . && \
	poetry run black -t py311 .

build:
	docker compose up --build

run:
	docker compose up