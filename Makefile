build:
	docker compose build

start:
	docker compose up

run: build start;

clear:
	docker compose down --remove-orphans